import json
from glob import glob
from os.path import join, realpath

folder = "./docs/json"


def read(type):

    with open(f"{folder}{type[1:]}.json") as ifile:
        return json.load(ifile)


def search(node, key):
    if isinstance(node, dict):
        if key in node:
            yield node[key]

        for k in node:
            yield from search(node[k], key)

    elif isinstance(node, list):
        for v in node:
            yield from search(v, key)


def all_defined_types():
    for p in glob(f"{folder}/**/*.json"):
        p = "#/" + p.split("json/")[1].replace(".json", "")
        yield p


def analysis(root):
    schemas = {root: read(root)}

    queue = [root]

    while queue:
        type = queue.pop()
        schemas[type] = read(type)

        print(f"load {type}")

        for ref in search(schemas[type], "$ref"):
            if ref in schemas:
                continue

            assert isinstance(ref, str)
            assert ref.startswith("#")
            queue.append(ref)

    for defined_type in all_defined_types():
        if defined_type not in schemas:
            print(f"WARNING {defined_type} not used")

    return schemas


# def guess_type(obj, accept_types, schemas):
#     try:
#         if len(accept_types) == 1:
#             schema = accept_types[0]
#         elif "ty" in obj:
#             ty = obj["ty"]

#             for t in accept_types:
#                 if ty == schemas[t]["properties"]["ty"].get("const") or ty == schemas[
#                     t
#                 ]["properties"]["ty"].get("value"):
#                     schema = t
#         else:
#             schema = max(
#                 accept_types,
#                 key=lambda t: set(obj.keys()) & set(schemas[t]["properties"].keys()),
#             )

#         for prop in obj:
#             if prop.startswith("$"):
#                 continue

#             if prop in known_error_props:
#                 continue

#             t = schemas[schema]["properties"][prop]

#             if t["type"] == "object":
#                 if "oneOf" in t:
#                     guess_type(obj[prop], [k["$ref"] for k in t["oneOf"]], schemas)
#                 else:
#                     raise Exception()
#             elif t["type"] == "array":
#                 if "items" not in t:
#                     continue

#                 if "oneOf" in t["items"]:
#                     _types = [k["$ref"] for k in t["items"]["oneOf"]]
#                 else:
#                     raise Exception()

#                 for v in obj[prop]:
#                     guess_type(v, _types, schemas)

#         obj["$schema"] = realpath(schema.replace("#", folder)) + ".json"
#     except Exception as e:
#         print(f"process {obj} fail due {e}")


# def update_schema(node):
#     if not "$shema" in node:
#         return

#     schema = schemas[node["$schema"]]

#     for p in node:
#         if isinstance(node[p], list):
#             sub_schema = [update_schema(k) for k in node[p]]
#         elif isinstance(node[p], dict):
#             sub_schema = {k: update_schema(node[p][k]) for k in node[p]}


# def annotate(p):
#     with open(p) as ifile:
#         icontent = json.load(ifile)

#         guess_type(icontent, ["#/animation"], schemas)

#     # with open(p + ".schema.json", "w") as ofile:


analysis("#/animation")


# annotate("./demo/adrock/data.json")
