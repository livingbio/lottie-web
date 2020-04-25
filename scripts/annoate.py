import json
import logging
from collections import defaultdict
from copy import deepcopy
from glob import glob
from os.path import basename, join, realpath
from pprint import pprint
from schema import Schema

import fire


def read(folder, type):
    with open(f"{folder}{type[1:]}.json") as ifile:
        return json.load(ifile)


def analy(root, folder="../docs/json"):
    schema = Schema()
    queue = [root]

    while queue:
        type = queue.pop()
        schema.add(type, read(folder, type))

        for ref in schema.search("$ref", type):
            if schema.has(ref):
                continue

            assert isinstance(ref, str)
            assert ref.startswith("#/")
            queue.append(ref)

    return schema


def annotate(ifilepath, opath=None, strict=False):
    schema = analy("#/animation")

    with open(ifilepath) as ifile:
        icontent = json.load(ifile)

    resolved_schema = schema.validate(icontent, "#/animation", strict=strict)
    opath = opath or ifilepath.rstrip(".json") + ".schema.json"

    with open(opath, "w") as ofile:
        json.dump(resolved_schema, ofile, indent=2)

    icontent["$schema"] = "./" + basename(opath)

    with open(ifilepath, "w") as ofile:
        json.dump(icontent, ofile, indent=2)


if __name__ == "__main__":
    fire.Fire(annotate)
