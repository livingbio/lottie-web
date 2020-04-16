# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get 1'] = {
    'foo': {
        '$path': '#/foo',
        'bar': 123,
        'title': '#/foo'
    }
}

snapshots['test_get 2'] = 123

snapshots['test_get 3'] = {
    '$path': '#/foo',
    'bar': 123,
    'title': '#/foo'
}

snapshots['test_add 1'] = {
    'foo': {
        '$path': '#/foo',
        'bar': {
            '$path': '#/foo/bar',
            '1': {
                '2': {
                    '3': {
                        '$path': '#/foo/bar/1/2/3',
                        'a': 'b',
                        'title': '#/foo/bar/1/2/3'
                    }
                }
            },
            'a': 'b',
            'title': '#/foo/bar'
        },
        'title': '#/foo'
    }
}

snapshots['test_match 1'] = {
    '$path': '#/foo3',
    'properties': {
        'a': {
            '$path': '#/foo1',
            'properties': {
                'k': {
                    'type': 'string'
                }
            },
            'title': '#/foo1',
            'type': 'object'
        }
    },
    'title': '#/foo3',
    'type': 'object'
}

snapshots['test_match 2'] = {
    '$path': '#/foo5',
    'items': [
        {
            '$path': '#/foo1',
            'properties': {
                'k': {
                    'type': 'string'
                }
            },
            'title': '#/foo1',
            'type': 'object'
        },
        {
            '$path': '#/foo2',
            'properties': {
                'k': {
                    'type': 'number'
                }
            },
            'title': '#/foo2',
            'type': 'object'
        },
        {
            '$path': '#/foo1',
            'properties': {
                'k': {
                    'type': 'string'
                }
            },
            'title': '#/foo1',
            'type': 'object'
        }
    ],
    'title': '#/foo5',
    'type': 'array'
}
