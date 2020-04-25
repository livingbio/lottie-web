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

snapshots['test_validate_basic 1'] = {
    '$match': True,
    '$path': '#/foo',
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'properties': {
        'ix': {
            '$match': True,
            'description': 'Property Index. Used for expressions.',
            'extended_name': 'Property Index',
            'type': 'string'
        },
        'k': {
            '$match': True,
            'description': 'Property Value',
            'extended_name': 'Value',
            'type': 'number'
        },
        'x': {
            '$match': True,
            'description': 'Property Expression. An AE expression that modifies the value.',
            'extended_name': 'Expression',
            'type': 'string'
        }
    },
    'title': '#/foo',
    'type': 'object'
}

snapshots['test_validate_with_depth 1'] = {
    '$match': True,
    '$path': '#/foo',
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'properties': {
        'i': {
            '$match': True,
            'properties': {
                'x': {
                    '$match': True,
                    'description': 'bezier x axis. Array of numbers.',
                    'extended_name': 'X axis',
                    'type': 'number'
                },
                'y': {
                    '$match': True,
                    'description': 'bezier y axis. Array of numbers.',
                    'extended_name': 'Y axis',
                    'type': 'number'
                }
            },
            'type': 'object'
        },
        't': {
            '$match': True,
            'description': 'Start time of keyframe segment.',
            'extended_name': 'Time',
            'type': 'number'
        }
    },
    'title': '#/foo',
    'type': 'object'
}

snapshots['test_validate_with_ref 1'] = {
    '$match': True,
    '$path': '#/valueKeyframed',
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'properties': {
        'k': {
            '$match': True,
            'description': 'Property Value keyframes',
            'extended_name': 'Keyframes',
            'items': [
                {
                    '$match': True,
                    '$path': '#/properties/valueKeyframe',
                    '$schema': 'http://json-schema.org/draft-04/schema',
                    'properties': {
                        's': {
                            '$match': True,
                            'description': 'Start value of keyframe segment.',
                            'extended_name': 'Start',
                            'type': 'number'
                        },
                        't': {
                            '$match': True,
                            'description': 'Start time of keyframe segment.',
                            'extended_name': 'Time',
                            'type': 'number'
                        }
                    },
                    'title': '#/properties/valueKeyframe',
                    'type': 'object'
                }
            ],
            'type': 'array'
        }
    },
    'title': '#/valueKeyframed',
    'type': 'object'
}

snapshots['test_validate_with_strict 1'] = {
    '$match': True,
    '$path': '#/valueKeyframed',
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'properties': {
        'x': {
            '$match': True,
            'description': 'Property Expression. An AE expression that modifies the value.',
            'extended_name': 'Expression',
            'type': 'string'
        }
    },
    'title': '#/valueKeyframed',
    'type': 'object'
}

snapshots['test_validate_with_depth 2'] = {
    '$path': '#/foo',
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'properties': {
        'i': {
            'description': 'Bezier curve interpolation in value.',
            'extended_name': 'In Value',
            'oneOf': [
                {
                    'properties': {
                        'x': {
                            'description': 'bezier x axis. Array of numbers.',
                            'extended_name': 'X axis',
                            'type': 'array'
                        },
                        'y': {
                            'description': 'bezier y axis. Array of numbers.',
                            'extended_name': 'Y axis',
                            'type': 'array'
                        }
                    },
                    'type': 'object'
                },
                {
                    'properties': {
                        'x': {
                            'description': 'bezier x axis. Array of numbers.',
                            'extended_name': 'X axis',
                            'type': 'number'
                        },
                        'y': {
                            'description': 'bezier y axis. Array of numbers.',
                            'extended_name': 'Y axis',
                            'type': 'number'
                        }
                    },
                    'type': 'object'
                }
            ],
            'type': 'object'
        },
        's': {
            'description': 'Start value of keyframe segment.',
            'extended_name': 'Start',
            'items': {
                'type': 'number'
            },
            'type': 'array'
        },
        't': {
            'description': 'Start time of keyframe segment.',
            'extended_name': 'Time',
            'type': 'number'
        }
    },
    'title': '#/foo',
    'type': 'object'
}

snapshots['test_validate_with_const 1'] = {
    '$match': True,
    '$path': '#/valueKeyframed',
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'properties': {
        'x': {
            '$match': True,
            'const': '123',
            'description': 'Property Expression. An AE expression that modifies the value.',
            'extended_name': 'Expression',
            'type': 'string'
        }
    },
    'title': '#/valueKeyframed',
    'type': 'object'
}
