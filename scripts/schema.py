import logging
from copy import deepcopy


class Schema(object):
    def __init__(self):
        self.cache = {}

    def get(self, path):
        if path == "#":
            return self.cache

        assert path.startswith("#/")

        node = self.cache
        for p in path.lstrip("#/").split("/"):
            node = node[p]

        return node

    def search(self, key, path=None, node=None):
        if path is not None:
            node = self.get(path)

        if node is None:
            node = self.get("#")

        if isinstance(node, dict):
            if key in node:
                yield node[key]

            for k in node:
                yield from self.search(key, node=node[k])

        elif isinstance(node, list):
            for v in node:
                yield from self.search(key, node=v)

    def add(self, path, code):
        assert path.startswith("#/")

        node = self.cache

        for p in path.split("/")[:-1]:
            if p == "#":
                node = self.cache
            else:
                if p not in node:
                    node[p] = {}

                node = node[p]

        code["$path"] = path
        if "title" not in code:
            code["title"] = path

        node[path.rsplit("/", 1)[1]] = code

    def has(self, path):
        try:
            self.get(path)
            return True
        except:
            return False

    def validate(self, data, path, node=None, depth=None, strict=False):
        def score(node):
            if isinstance(node, dict):
                if "$match" in node:
                    return 1 + sum(score(v) for v in node.values())
                return sum(score(v) for v in node.values())
            elif isinstance(node, list):
                return sum(score(v) for v in node)
            return 0

        if depth is None:
            depth = 99999

        if node is None:
            node = self.get(path)

        if not depth > 1:
            # don't validate anymore
            return node

        node = deepcopy(node)
        match = False

        if "$ref" in node:
            return self.validate(data, node["$ref"], depth=depth - 1, strict=strict)

        if "oneOf" in node:
            return max(
                (
                    self.validate(data, path, node=k, depth=depth - 1, strict=strict)
                    for k in node["oneOf"]
                ),
                key=score,
            )

        assert (
            "type" in node or "const" in node
        ), f"node {path} doesn't contain type info"

        if isinstance(data, dict) and node["type"] == "object":
            properties = {}
            for key in data:
                if key.startswith("$"):
                    continue

                if key not in node["properties"]:
                    logging.warn(f"{key} not in {path}")
                    # NOTE: some data properties not in schema
                    assert not strict, f"{key} not belong to {path}"
                    continue

                properties[key] = self.validate(
                    data[key],
                    path=f"{path}.{key}",
                    node=node["properties"][key],
                    depth=depth - 1,
                    strict=strict,
                )

            node["properties"] = properties
            match = True
        elif isinstance(data, list) and node["type"] == "array" and "items" in node:
            node["items"] = [
                self.validate(
                    k,
                    path=f"{path}[{ind}]",
                    node=node["items"],
                    depth=depth - 1,
                    strict=strict,
                )
                for ind, k in enumerate(data)
            ]
            match = True
        else:
            if "const" in node:
                if node["const"] == data:
                    match = True
            elif node["type"] == "number" and isinstance(data, (float, int)):
                match = True
            elif node["type"] == "string" and isinstance(data, str):
                match = True
            elif node["type"] == "boolean" and isinstance(data, bool):
                match = True

        assert not strict or match, f"{data} not match {path}"

        if match:
            node["$match"] = True

        return node
