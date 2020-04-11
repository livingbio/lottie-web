import json
from os.path import join, realpath
from glob import glob
import yaml

folder = "./docs/json"

schemas = {}

known_error = [
    # "#/effects/layerIndex",
    # "#/shapes/roundedCorners",
    # "#/layers/comp",
    "#/properties/const",
    # "#/properties/constKeyframed",
    # "#/helpers/textBased",
]

known_error_props = ["bounds", "shapes"]


def check_add(t):
    if t.startswith("#") and t not in schemas and t not in known_error:
        check(t)


def find_refs(node):
    # print(node)
    if isinstance(node, dict):
        for key in node:
            if key == "$ref":
                check_add(node[key])
            else:
                find_refs(node[key])

    elif isinstance(node, list):
        for v in node:
            find_refs(v)


def check(type):
    print(f"process {type}")

    path = type.replace("#", folder) + ".json"

    with open(path) as ifile:
        icontent = json.load(ifile)

        schemas[type] = icontent

        find_refs(icontent)


def check_not_ref_types():
    for p in glob(f"{folder}/**/*.json"):
        p = "#/" + p.split("json/")[1].replace(".json", "")
        if p not in schemas:
            print(f"not passed {p}")


def guess_type(obj, accept_types, schemas):
    try:
        if len(accept_types) == 1:
            schema = accept_types[0]
        elif "ty" in obj:
            ty = obj["ty"]

            for t in accept_types:
                if ty == schemas[t]["properties"]["ty"].get("const") or ty == schemas[
                    t
                ]["properties"]["ty"].get("value"):
                    schema = t
        else:
            schema = max(
                accept_types,
                key=lambda t: set(obj.keys()) & set(schemas[t]["properties"].keys()),
            )

        for prop in obj:
            if prop.startswith("$"):
                continue

            if prop in known_error_props:
                continue

            t = schemas[schema]["properties"][prop]

            if t["type"] == "object":
                if "oneOf" in t:
                    guess_type(obj[prop], [k["$ref"] for k in t["oneOf"]], schemas)
                else:
                    raise Exception()
            elif t["type"] == "array":
                if "items" not in t:
                    continue

                if "oneOf" in t["items"]:
                    _types = [k["$ref"] for k in t["items"]["oneOf"]]
                else:
                    raise Exception()

                for v in obj[prop]:
                    guess_type(v, _types, schemas)

        obj["$schema"] = realpath(schema.replace("#", folder)) + ".json"
    except Exception as e:
        print(f"process {obj} fail due {e}")


def annotate(p):
    with open(p) as ifile:
        icontent = json.load(ifile)

        guess_type(icontent, ["#/animation"], schemas)

    with open(p, "w") as ofile:
        json.dump(icontent, ofile, indent=4, sort_keys=True)


check("#/animation")
check_not_ref_types()


annotate("./demo/adrock/data.json")
