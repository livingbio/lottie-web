import json
from os.path import dirname, join

from ..annoate import analy, annotate

test_file = join(dirname(__file__), "data.json")
opath = test_file + ".schema.json"


def test_analy(snapshot):
    schemas = analy("#/animation")
    snapshot.assert_match(schemas.cache)


def test_annotate(snapshot):
    annotate(test_file, opath=opath)

    with open(opath) as ifile:
        snapshot.assert_match(json.load(ifile))

