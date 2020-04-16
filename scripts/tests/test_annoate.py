import json
from os.path import dirname, join

import pytest

from ..annoate import Schema, analy, annotate

test_file = join(dirname(__file__), "data.json")
opath = test_file + ".schema.json"




def test_analy(snapshot):
    schemas = analy("#/animation")
    snapshot.assert_match(schemas.cache)


def test_annotate(snapshot):
    annotate(test_file, opath=opath)

    with open(opath) as ifile:
        snapshot.assert_match(json.load(ifile))


def test_validate_basic():
    schema = Schema(folder="")
    schema.cache = {
        "type": "object",
        "properties": {
            "foo": {
                "type": "object",
                "properties": {
                    "bar1": {
                        "type": "number"
                    },
                    "bar2": {
                        "type": "string"
                    }
                }
            }
        }
    }

    assert schema.validate({
        "foo": {"bar1": 10}
    })

    with pytest.raises(Exception):
        assert schema.validate({
            "foo": {"bar1": "123"}
        })


def test_validate_oneOf():
    schema = Schema(folder="")
    schema.cache = {
        "type": "object",
        "properties": {
            "foo": {
                "oneOf": [{
                    "type": "number"
                }, {
                    "type": "string"
                }]
            }
        }
    }

    assert schema.validate({
        "foo": 10
    })

    assert schema.validate({
        "foo": "xxx"
    })


def test_ref_with_oneOf():
    schema = Schema(folder="")
    schema.cache = {
        "definations": {
            "helpers": {
                "boolean": {
                    "type": "number",
                    "oneOf": [
                        {
                            "standsFor": False,
                            "const": 0
                        },
                        {
                            "standsFor": True,
                            "const": 1
                        }
                    ]
                }
            }
        },
        "oneOf": [{"$ref": "#/helpers/boolean"}]
    }

    assert schema.validate(0)


def test_validate_transform():
    schema = analy("#/animation")

    assert schema.validate({'k': [{'i': {'x': 0.833, 'y': 0.833}, 'o': {'x': 0.167, 'y': 0.167}, 'n': '0p833_0p833_0p167_0p167', 't': 339, 's': [35.965, -1024.97, 0], 'e': [35.965, -104.97, 0], 'to': [0, 153.33332824707, 0], 'ti': [0, -153.33332824707, 0]}, {'t': 359}]}, {'$ref': '#/properties/multiDimensionalKeyframed'})
    assert schema.validate({'o': {'k': 100}, 'r': {'k': 0}, 'p': {'k': [{'i': {'x': 0.833, 'y': 0.833}, 'o': {'x': 0.167, 'y': 0.167}, 'n': '0p833_0p833_0p167_0p167', 't': 339, 's': [35.965, -1024.97, 0], 'e': [35.965,
                                                                                                                                                                                                                   -104.97, 0], 'to': [0, 153.33332824707, 0], 'ti': [0, -153.33332824707, 0]}, {'t': 359}]}, 'a': {'k': [345.25, 456.75, 0]}, 's': {'k': [100, 100, 100]}}, {"$ref": '#/helpers/transform'})


def test_validate_ref():
    schema = Schema(folder="")
    schema.cache = {
        "definations": {
            "aaaa": {
                "type": "object",
                "properties": {
                    "foo": {"type": 'string'},
                    "bar": {"type": "number"}
                }
            }
        },
        "type": "object",
        "properties": {
            "foo": {
                "$ref": "#/aaaa"
            }
        }
    }

    assert schema.validate({
        "foo": {
            "foo": "123",
            "bar": 456
        }
    })
