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
        if depth is None:
            depth = 99999

        if node is None:
            node = self.get(path)

        if not depth > 1:
            # don't validate anymore
            return node

        node = deepcopy(node)

        if "$ref" in node:
            return self.validate(data, node["$ref"], depth=depth - 1, strict=strict)

        if "oneOf" in node:
            for k in node["oneOf"]:
                try:
                    return self.validate(
                        data, path, node=k, depth=depth - 1, strict=strict
                    )
                except:
                    pass

            raise Exception(f"non of {node['oneOf']} match {data}")

        if "const" in node:
            assert node["const"] == data
            return node

        assert "type" in node, f"node {path} doesn't contain type info"

        if isinstance(data, dict):
            assert node["type"] == "object", f"node {path} != {node['type']}"

            for key in data:
                if key.startswith("$"):
                    continue

                if key not in node["properties"]:
                    logging.warn(f"{key} not in {path}")

                    assert not strict, f"{key} not belong to {path}"
                    # NOTE: some data properties not in schema
                    continue

                node["properties"][key] = self.validate(
                    data[key],
                    path=f"{path}.{key}",
                    node=node["properties"][key],
                    depth=depth - 1,
                    strict=strict,
                )
            return node
        elif isinstance(data, list):
            assert node["type"] == "array" and "items" in node

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
            return node

        else:
            if node["type"] == "number":
                assert isinstance(data, (float, int))
            elif node["type"] == "string":
                assert isinstance(data, str)
            elif node["type"] == "boolean":
                assert isinstance(data, bool)
            else:
                raise Exception(f"data type {type(data)} != {node['type']}")

            return node

        raise Exception(f"unknown {data} {path}")

    def _choose_schema(self, data, nodes, fuzzy=False, depth=None):
        if fuzzy and depth is None:
            depth = 1

        candidates = []

        for s in nodes:
            try:
                self.validate(data, s.get("$path", ""), s, depth, strict=not fuzzy)
                candidates.append((s.get("$path", ""), s))
            except:
                pass

        assert candidates, f"No Candidate {data} {nodes}"

        if len(candidates) == 1:
            return candidates[0]

        assert fuzzy, f"there are more than one candidate {data} {nodes} {candidates}"

        return self._choose_schema(data, nodes, fuzzy, depth + 1)
