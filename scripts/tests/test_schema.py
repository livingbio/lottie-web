import pytest

from ..schema import Schema


def test_add(snapshot):
    schema = Schema()

    schema.add("#/foo", {"bar": {"type": "array", "items": [123]}})
    schema.add("#/foo/bar", {"a": "b"})
    schema.add("#/foo/bar/1/2/3", {"a": "b"})

    snapshot.assert_match(schema.cache)


def test_get(snapshot):
    schema = Schema()

    schema.add("#/foo", {"bar": 123})

    snapshot.assert_match(schema.get("#"))
    snapshot.assert_match(schema.get("#/foo/bar"))
    snapshot.assert_match(schema.get("#/foo"))

    with pytest.raises(Exception):
        snapshot.assert_match(schema.get("#/foo/bar1"))


def test_has():
    schema = Schema()

    schema.add("#/foo", {"bar": {"type": "array", "items": [123]}})
    schema.add("#/foo/bar", {"a": "b"})
    schema.add("#/foo/bar/1/2/3", {"a": "b"})

    assert schema.has("#/foo")
    assert schema.has("#/foo/bar")
    assert schema.has("#/foo/bar/1/2/3")
    assert not schema.has("#/foo/1/4")


def test_validate_basic(snapshot):
    schema = Schema()

    schema.add(
        "#/foo",
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "k": {
                    "description": "Property Value",
                    "extended_name": "Value",
                    "type": "number",
                },
                "x": {
                    "description": "Property Expression. An AE expression that modifies the value.",
                    "extended_name": "Expression",
                    "type": "string",
                },
                "ix": {
                    "description": "Property Index. Used for expressions.",
                    "extended_name": "Property Index",
                    "type": "string",
                },
            },
        },
    )

    snapshot.assert_match(schema.validate({"k": 1, "x": "123", "ix": "456"}, "#/foo"))
    with pytest.raises(Exception):
        schema.validate({"k": 1, "x": "123", "ix": "456"}, "#/f")


def test_search():
    schema = Schema()

    schema.add(
        "#/foo2",
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "k": {
                    "description": "Property Value",
                    "extended_name": "Value",
                    "type": "number",
                },
            },
        },
    )
    schema.add(
        "#/foo1",
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "o": {
                    "description": "Property Value",
                    "extended_name": "Value",
                    "type": "number",
                },
                "p": [{"x": 1}],
            },
        },
    )

    assert list(schema.search("o"))
    assert list(schema.search("o", "#/foo1"))
    assert not list(schema.search("o", "#/foo2"))
    assert list(schema.search("x", "#/foo1"))


def test_validate_with_depth(snapshot):
    schema = Schema()

    schema.add(
        "#/foo",
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "s": {
                    "description": "Start value of keyframe segment.",
                    "extended_name": "Start",
                    "items": {"type": "number"},
                    "type": "array",
                },
                "t": {
                    "description": "Start time of keyframe segment.",
                    "extended_name": "Time",
                    "type": "number",
                },
                "i": {
                    "description": "Bezier curve interpolation in value.",
                    "extended_name": "In Value",
                    "oneOf": [
                        {
                            "type": "object",
                            "properties": {
                                "x": {
                                    "description": "bezier x axis. Array of numbers.",
                                    "extended_name": "X axis",
                                    "type": "array",
                                },
                                "y": {
                                    "description": "bezier y axis. Array of numbers.",
                                    "extended_name": "Y axis",
                                    "type": "array",
                                },
                            },
                        },
                        {
                            "type": "object",
                            "properties": {
                                "x": {
                                    "description": "bezier x axis. Array of numbers.",
                                    "extended_name": "X axis",
                                    "type": "number",
                                },
                                "y": {
                                    "description": "bezier y axis. Array of numbers.",
                                    "extended_name": "Y axis",
                                    "type": "number",
                                },
                            },
                        },
                    ],
                    "type": "object",
                },
            },
        },
    )

    snapshot.assert_match(schema.validate({"t": 1, "i": {"x": 1, "y": 2}}, "#/foo"))

    with pytest.raises(Exception):
        schema.validate({"t": 1, "i": {"x": 1, "y": "2"}}, "#/foo", strict=True)

    snapshot.assert_match(
        schema.validate({"t": 1, "i": {"x": 1, "y": "2"}}, "#/foo", depth=1)
    )


def test_validate_with_ref(snapshot):
    schema = Schema()

    schema.add(
        "#/valueKeyframed",
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "k": {
                    "description": "Property Value keyframes",
                    "extended_name": "Keyframes",
                    "type": "array",
                    "items": {"type": "object", "$ref": "#/properties/valueKeyframe"},
                },
                "x": {
                    "description": "Property Expression. An AE expression that modifies the value.",
                    "extended_name": "Expression",
                    "type": "string",
                },
                "ix": {
                    "description": "Property Index. Used for expressions.",
                    "extended_name": "Property Index",
                    "type": "string",
                },
            },
        },
    )

    schema.add(
        "#/properties/valueKeyframe",
        {
            "$schema": "http://json-schema.org/draft-04/schema",
            "type": "object",
            "properties": {
                "s": {
                    "oneOf": [
                        {
                            "description": "Start value of keyframe segment.",
                            "extended_name": "Start",
                            "type": "number",
                        },
                        {
                            "description": "Start value of keyframe segment.",
                            "extended_name": "Start",
                            "items": {"type": "number"},
                            "type": "array",
                        },
                    ]
                },
                "t": {
                    "description": "Start time of keyframe segment.",
                    "extended_name": "Time",
                    "type": "number",
                },
            },
        },
    )

    snapshot.assert_match(
        schema.validate({"k": [{"s": 0, "t": 1}]}, "#/valueKeyframed")
    )

    with pytest.raises(Exception):
        schema.validate({"k": [{"s": "0", "t": 1}]}, "#/valueKeyframed", strict=True)


def test_validate_with_strict(snapshot):
    schema = Schema()

    schema.add(
        "#/valueKeyframed",
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "k": {
                    "description": "Property Value keyframes",
                    "extended_name": "Keyframes",
                    "type": "array",
                    "items": {"type": "object", "$ref": "#/properties/valueKeyframe"},
                },
                "x": {
                    "description": "Property Expression. An AE expression that modifies the value.",
                    "extended_name": "Expression",
                    "type": "string",
                },
                "ix": {
                    "description": "Property Index. Used for expressions.",
                    "extended_name": "Property Index",
                    "type": "string",
                },
            },
        },
    )

    snapshot.assert_match(
        schema.validate({"a": "b", "x": "foo", "$schema": "bar"}, "#/valueKeyframed")
    )

    with pytest.raises(Exception):
        schema.validate({"a": "b", "x": "foo"}, "#/valueKeyframed", strict=True)


def test_validate_with_const(snapshot):
    schema = Schema()

    schema.add(
        "#/valueKeyframed",
        {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "k": {
                    "description": "Property Value keyframes",
                    "extended_name": "Keyframes",
                    "type": "array",
                    "items": {"type": "object", "$ref": "#/properties/valueKeyframe"},
                },
                "x": {
                    "description": "Property Expression. An AE expression that modifies the value.",
                    "extended_name": "Expression",
                    "type": "string",
                    "const": "123",
                },
                "ix": {
                    "description": "Property Index. Used for expressions.",
                    "extended_name": "Property Index",
                    "type": "string",
                },
            },
        },
    )

    with pytest.raises(Exception):
        assert schema.validate(
            {"a": "b", "x": "foo", "$schema": "bar"}, "#/valueKeyframed", strict=True
        )

    snapshot.assert_match(
        schema.validate({"a": "b", "x": "123", "$schema": "bar"}, "#/valueKeyframed")
    )
