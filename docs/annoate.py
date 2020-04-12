import json
from collections import defaultdict
from copy import deepcopy
from glob import glob
from os.path import join, realpath
from pprint import pprint

import jsonschema

# def all_defined_types():
#     for p in glob(f"{folder}/**/*.json"):
#         p = "#/" + p.split("json/")[1].replace(".json", "")
#         yield p


class Schema(object):
    def __init__(self, folder):
        self.folder = folder
        nested_dict = lambda: defaultdict(nested_dict)
        self.cache = nested_dict()

    def read(self, type):
        with open(f"{self.folder}{type[1:]}.json") as ifile:
            return json.load(ifile)

    def search(self, key, node=None):
        print(f"{key} {node}")
        if node is None:
            node = self.cache

        if isinstance(node, dict):
            if key in node:
                yield node[key]

            for k in node:
                # print(k)
                yield from self.search(key, node[k])

        elif isinstance(node, list):
            for v in node:
                yield from self.search(key, v)

    def add(self, path):
        assert path.startswith("#/")

        parent = self.get(path.rsplit("/", 1)[0])
        parent[path.rsplit("/", 1)[1]] = self.read(path)

    def get(self, path):
        if path == "#":
            return self.cache

        assert path.startswith("#/")

        node = self.cache
        for p in path.lstrip("#/").split("/"):
            node = node[p]

        return node

    def has(self, path):
        assert path.startswith("#/")

        node = self.cache
        for p in path.lstrip("#/").split("/"):
            if p not in node:
                return False
            node = node[p]

        return True

    def validate(self, data, node=None):
        if node is None:
            node = self.cache

        jsonschema.validate(data, node)

    def __choose_schema(self, data, node):
        # choose best match schema
        if "ty" in data:
            for s in node["oneOf"]:
                if "$ref" in s:
                    r = self.get(s["$ref"])

                if r["properties"]["ty"]["const"] == data["ty"]:
                    return s["$ref"], deepcopy(r)

            raise Exception()

        keys = set(data.keys())

        pps = {}
        for s in node["oneOf"]:
            if "$ref" in s:
                s = self.get(s["$ref"])

            props = s["properties"].keys()
            pps[s] = set(props)

        pick = max(pps, key=lambda i: (pps[i] & keys) / (pps[i] | keys))
        return pick, pps[pick]

    def match(self, data, node=None):
        if node is None:
            node = deepcopy(self.get("#/animation"))

        # TODO: check it works?
        # self.validate(data, node)

        if "$ref" in node:
            node = deepcopy(self.get(node["$ref"]))

        if "oneOf" in node:
            _, node = self.__choose_schema(data, node)

        for key in node.get("properties", {}):
            if key not in data:
                continue

            type = node["properties"][key]["type"]

            if type == "object":
                node["properties"][key] = self.match(data[key], node["properties"][key])
            elif type == "array" and "items" in node["properties"][key]:
                node["properties"][key] = [
                    self.match(k, node["properties"][key]["items"]) for k in data[key]
                ]

        return node


def analy(root):
    schemas = Schema(folder="../docs/json")
    queue = [root]

    while queue:
        type = queue.pop()
        schemas.add(type)

        print(f"load {type}")

        for ref in schemas.search("$ref", schemas.get(type)):
            if schemas.has(ref):
                print("skip")
                continue

            assert isinstance(ref, str)
            assert ref.startswith("#/")
            queue.append(ref)

    return schemas


def annotate(ifilepath, schemas):
    with open(ifilepath) as ifile:
        icontent = json.load(ifile)

    # NOTE: really?
    schemas.validate(icontent)
    pprint(schemas.match(icontent))


if __name__ == "__main__":
    schemas = analy("#/animation")
    pprint(schemas.cache)
    annotate("../demo/adrock/data.json", schemas)
