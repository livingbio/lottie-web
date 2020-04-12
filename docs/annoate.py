import json
from glob import glob
from os.path import join, realpath
from pprint import pprint
import jsonschema
from collections import defaultdict
from copy import deepcopy

# def all_defined_types():
#     for p in glob(f"{folder}/**/*.json"):
#         p = "#/" + p.split("json/")[1].replace(".json", "")
#         yield p

class Schema(object):
    def __init__(self, folder):
        self.folder =  folder
        nested_dict = lambda: defaultdict(nested_dict)
        self.cache = nested_dict()

    def read(self, type):
        with open(f"{self.folder}{type[1:]}.json") as ifile:
            return json.load(ifile)

    def search(self, key, node=None):
        print(f'{key} {node}')
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
        for p in path.lstrip('#/').split('/'):
            node = node[p]

        return node

    def has(self, path):
        assert path.startswith("#/")

        node = self.cache
        for p in path.lstrip('#/').split('/'):
            if p not in node:
                return False
            node = node[p]

        return True

    def validate(self, data, node=None):
        if node is None:
            node = self.cache

        jsonschema.validate(data, node)


    def match(self, data, node = None):
        if node is None:
            node = deepcopy(self.cache)

        self.validate(data, node)



def analy(root):
    schemas = Schema(folder = "../docs/json")
    queue = [root]

    while queue:
        type = queue.pop()
        schemas.add(type)

        print(f"load {type}")

        for ref in schemas.search("$ref", schemas.get(type)):
            if schemas.has(ref):
                print('skip')
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



if __name__ == "__main__":
    schemas = analy
    pprint(schemas.cache)
    annotate("../demo/adrock/data.json", schemas)
