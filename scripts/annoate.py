import json
import logging
from collections import defaultdict
from copy import deepcopy
from glob import glob
from os.path import basename, join, realpath
from pprint import pprint

import fire


class Schema(object):
    def __init__(self, folder):
        self.folder = folder
        self.cache = {"definations": {}}

    def read(self, type):
        with open(f"{self.folder}{type[1:]}.json") as ifile:
            return json.load(ifile)

    def search(self, key, node=None):
        if node is None:
            node = self.cache

        if isinstance(node, dict):
            if key in node:
                yield node[key]

            for k in node:
                yield from self.search(key, node[k])

        elif isinstance(node, list):
            for v in node:
                yield from self.search(key, v)

    def add(self, path):
        assert path.startswith("#/")

        node = self.cache

        for p in path.split("/")[:-1]:
            if p == "#":
                node = self.cache["definations"]
            else:
                if p not in node:
                    node[p] = {}

                node = node[p]

        node[path.rsplit("/", 1)[1]] = self.read(path)

    def get(self, path):
        if path == "#":
            return self.cache

        assert path.startswith("#/")

        node = self.cache["definations"]
        for p in path.lstrip("#/").split("/"):
            node = node[p]

        return node

    def has(self, path):
        try:
            self.get(path)
            return True
        except:
            return False

    def validate(self, data, node=None):
        if node is None:
            node = self.get("#")

        if "$ref" in node:
            return self.validate(data, self.get(node["$ref"]))

        if "oneOf" in node:
            for k in node["oneOf"]:
                try:
                    return self.validate(data, k)
                except:
                    pass

            raise Exception(f"non of {node['oneOf']} match {data}")

        if "const" in node:
            assert node["const"] == data
            return True

        assert "type" in node, f"node {node} doesn't contain type info"

        if isinstance(data, dict):
            assert node["type"] == "object"

            for key in data:
                if key.startswith("$"):
                    continue

                if key not in node["properties"]:
                    logging.warn(f"{key} not in {node}")
                    # NOTE: some data properties not in schema
                    continue

                assert self.validate(data[key], node["properties"][key])
            return True
        elif isinstance(data, list):
            assert node["type"] == "array" and "items" in node
            return all(self.validate(k, node["items"]) for k in data)
        else:
            if node["type"] == "number":
                assert isinstance(data, (float, int))
            elif node["type"] == "string":
                assert isinstance(data, str)
            elif node["type"] == "boolean":
                assert isinstance(data, bool)
            else:
                raise Exception(
                    f"data type {type(data)} expect {node['type']}")

            return True

        raise Exception("unknown")

    def __choose_schema(self, data, node, fuzzy=True):
        if fuzzy:
            return self.__choose_schema_fuzzy(data, node)

        for s in node["oneOf"]:
            try:
                self.validate(data, s)

                return s.get("ref"), deepcopy(s)
            except:
                pass

        raise Exception(f"Cannot Find Match Schema {node} for {data}")

    def __choose_schema_fuzzy(self, data, node):
        # choose best match schema
        if "ty" in data:
            for s in node["oneOf"]:
                if "$ref" in s:
                    r = self.get(s["$ref"])

                if r["properties"]["ty"]["const"] == data["ty"]:
                    return s["$ref"], deepcopy(r)

            raise Exception()

        keys = set(data.keys())

        pps = []
        for s in node["oneOf"]:
            if "$ref" in s:
                r = self.get(s["$ref"])

            props = r["properties"].keys()
            pps.append((r, s, set(props)))

        r, s, p = max(pps, key=lambda k: len(k[2] & keys) / len(k[2] | keys))
        return s["$ref"], deepcopy(r)

    def match(self, data, node=None):
        if node is None:
            node = deepcopy(self.get("#/animation"))

        # TODO: check it works?
        # self.validate(data, node)

        node_type = None
        if "$ref" in node:
            node_type = node["$ref"]
            node = deepcopy(self.get(node["$ref"]))

        if "oneOf" in node:
            node_type, node = self.__choose_schema(data, node)

        keys = list(node.get("properties", {}).keys())
        for key in keys:
            if key not in data:
                del node["properties"][key]
                continue

            if key == "ddd":
                node["properties"][key] = {
                    "title": "3d Layer",
                    "description": "3d layer flag",
                    "type": "number",
                    "default": 0,
                }
                continue

            type = node["properties"][key]["type"]

            if type == "object":
                node["properties"][key] = self.match(
                    data[key], node["properties"][key])
            elif type == "array" and "items" in node["properties"][key]:
                node["properties"][key]["items"] = [
                    self.match(k, node["properties"][key]["items"]) for k in data[key]
                ]

        if "title" not in node and node_type:
            node["title"] = node_type

        return node


def analy(root):
    schemas = Schema(folder="../docs/json")
    queue = [root]

    while queue:
        type = queue.pop()
        schemas.add(type)

        for ref in schemas.search("$ref", schemas.get(type)):
            if schemas.has(ref):
                continue

            assert isinstance(ref, str)
            assert ref.startswith("#/")
            queue.append(ref)

    return schemas


def annotate(ifilepath, opath=None):
    schemas = analy("#/animation")

    with open(ifilepath) as ifile:
        icontent = json.load(ifile)

    resolved_schema = schemas.match(icontent)

    opath = opath or ifilepath.rstrip(".json") + ".schema.json"

    with open(opath, "w") as ofile:
        json.dump(resolved_schema, ofile, indent=2)

    icontent["$schema"] = "./" + basename(opath)

    with open(ifilepath, 'w') as ofile:
        json.dump(icontent, ofile, indent=2)


if __name__ == "__main__":
    fire.Fire(annotate)
