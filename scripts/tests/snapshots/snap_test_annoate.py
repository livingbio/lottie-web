# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_analy 1'] = {
    'definations': {
        'animation': {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'properties': {
                'assets': {
                    'description': 'source items that can be used in multiple places. Comps and Images for now.',
                    'items': {
                        'oneOf': [
                            {
                                '$ref': '#/sources/image'
                            },
                            {
                                '$ref': '#/sources/precomp'
                            }
                        ],
                        'type': 'object'
                    },
                    'title': 'Assets',
                    'type': 'array'
                },
                'chars': {
                    'description': 'source chars for text layers',
                    'items': {
                        'oneOf': [
                            {
                                '$ref': '#/sources/chars'
                            }
                        ],
                        'type': 'object'
                    },
                    'title': 'Chars',
                    'type': 'array'
                },
                'ddd': {
                    'description': 'Composition has 3-D layers',
                    'enum': [
                        0,
                        1
                    ],
                    'title': '3-D',
                    'type': 'number'
                },
                'fr': {
                    'description': 'Frame Rate',
                    'title': 'Frame Rate',
                    'type': 'number'
                },
                'h': {
                    'description': 'Composition Height',
                    'title': 'Height',
                    'type': 'number'
                },
                'ip': {
                    'description': 'In Point of the Time Ruler. Sets the initial Frame of the animation.',
                    'title': 'In Point',
                    'type': 'number'
                },
                'layers': {
                    'description': 'List of Composition Layers',
                    'items': {
                        'oneOf': [
                            {
                                '$ref': '#/layers/shape'
                            },
                            {
                                '$ref': '#/layers/solid'
                            },
                            {
                                '$ref': '#/layers/comp'
                            },
                            {
                                '$ref': '#/layers/image'
                            },
                            {
                                '$ref': '#/layers/null'
                            },
                            {
                                '$ref': '#/layers/text'
                            }
                        ],
                        'type': 'object'
                    },
                    'title': 'Layers',
                    'type': 'array'
                },
                'nm': {
                    'description': 'Composition name',
                    'title': 'Name',
                    'type': 'string'
                },
                'op': {
                    'description': 'Out Point of the Time Ruler. Sets the final Frame of the animation',
                    'title': 'Out Point',
                    'type': 'number'
                },
                'v': {
                    'description': 'Bodymovin Version',
                    'title': 'Version',
                    'type': 'string'
                },
                'w': {
                    'description': 'Composition Width',
                    'title': 'Width',
                    'type': 'number'
                }
            },
            'type': 'object'
        },
        'effects': {
            'angle': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ix': {
                        'description': 'Effect Index. Used for expressions. NOT USED. EQUALS SLIDER.',
                        'title': 'Effect Index',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'ty': {
                        'const': 1,
                        'description': 'Effect type.',
                        'title': 'Type',
                        'type': 'number'
                    },
                    'v': {
                        'description': 'Effect value.',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Value',
                        'type': 'object'
                    }
                },
                'type': 'object'
            },
            'checkbox': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ix': {
                        'description': 'Effect Index. Used for expressions.',
                        'title': 'Effect Index',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'ty': {
                        'const': 7,
                        'description': 'Effect type.',
                        'title': 'Type',
                        'type': 'number'
                    },
                    'v': {
                        'description': 'Effect value.',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Value',
                        'type': 'object'
                    }
                },
                'type': 'object'
            },
            'color': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ix': {
                        'description': 'Effect Index. Used for expressions.',
                        'title': 'Effect Index',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'ty': {
                        'const': 2,
                        'description': 'Effect type.',
                        'title': 'Type',
                        'type': 'number'
                    },
                    'v': {
                        'description': 'Effect value.',
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Value',
                        'type': 'object'
                    }
                },
                'type': 'object'
            },
            'customValue': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'type': 'object'
            },
            'dropDown': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ix': {
                        'description': 'Effect Index. Used for expressions.',
                        'title': 'Effect Index',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'ty': {
                        'const': 7,
                        'description': 'Effect type.',
                        'title': 'Type',
                        'type': 'number'
                    },
                    'v': {
                        'description': 'Effect value.',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Value',
                        'type': 'object'
                    }
                },
                'type': 'object'
            },
            'fill': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ef': {
                        'description': 'Effect List of properties.',
                        'items': [
                            {
                                '$ref': '#/effects/point'
                            },
                            {
                                '$ref': '#/effects/dropDown'
                            },
                            {
                                '$ref': '#/effects/color'
                            },
                            {
                                '$ref': '#/effects/dropDown'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            }
                        ],
                        'title': 'Effects',
                        'type': 'array'
                    },
                    'ix': {
                        'description': 'Effect Index. Used for expressions.',
                        'title': 'Effect Index',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'ty': {
                        'const': 21,
                        'description': 'Effect type.',
                        'title': 'Type',
                        'type': 'number'
                    }
                },
                'type': 'object'
            },
            'group': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ef': {
                        'description': 'Effect List of properties.',
                        'items': {
                            'oneOf': [
                                {
                                    '$ref': '#/effects/index'
                                }
                            ],
                            'type': 'object'
                        },
                        'title': 'Effects',
                        'type': 'array'
                    },
                    'en': {
                        'description': 'Enabled AE property value',
                        'extended_name': 'Enabled',
                        'type': 'number'
                    },
                    'ix': {
                        'description': 'Effect Index. Used for expressions.',
                        'title': 'Effect Index',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'ty': {
                        'const': 5,
                        'description': 'Effect type.',
                        'title': 'Type',
                        'type': 'number'
                    }
                },
                'type': 'object'
            },
            'index': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'oneOf': [
                    {
                        '$ref': '#/effects/slider'
                    },
                    {
                        '$ref': '#/effects/angle'
                    },
                    {
                        '$ref': '#/effects/color'
                    },
                    {
                        '$ref': '#/effects/point'
                    },
                    {
                        '$ref': '#/effects/checkbox'
                    },
                    {
                        '$ref': '#/effects/group'
                    },
                    {
                        '$ref': '#/effects/noValue'
                    },
                    {
                        '$ref': '#/effects/dropDown'
                    },
                    {
                        '$ref': '#/effects/customValue'
                    },
                    {
                        '$ref': '#/effects/layerIndex'
                    },
                    {
                        '$ref': '#/effects/tint'
                    },
                    {
                        '$ref': '#/effects/fill'
                    },
                    {
                        '$ref': '#/effects/stroke'
                    },
                    {
                        '$ref': '#/effects/tritone'
                    },
                    {
                        '$ref': '#/effects/proLevels'
                    }
                ],
                'type': 'object'
            },
            'layerIndex': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ix': {
                        'description': 'Effect Index. Used for expressions. NOT USED. EQUALS SLIDER.',
                        'title': 'Effect Index',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'ty': {
                        'const': 0,
                        'description': 'Effect type.',
                        'title': 'Type',
                        'type': 'number'
                    },
                    'v': {
                        'description': 'Effect value.',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            }
                        ],
                        'title': 'Value',
                        'type': 'object'
                    }
                },
                'type': 'object'
            },
            'noValue': {
            },
            'point': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ix': {
                        'description': 'Effect Index. Used for expressions.',
                        'title': 'Effect Index',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'ty': {
                        'const': 2,
                        'description': 'Effect type.',
                        'title': 'Type',
                        'type': 'number'
                    },
                    'v': {
                        'description': 'Effect value.',
                        'items': {
                            'oneOf': [
                                {
                                    '$ref': '#/properties/multiDimensional'
                                },
                                {
                                    '$ref': '#/properties/multiDimensionalKeyframed'
                                }
                            ],
                            'type': 'object'
                        },
                        'title': 'Value',
                        'type': 'object'
                    }
                },
                'type': 'object'
            },
            'proLevels': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ef': {
                        'description': 'ffect List of properties.',
                        'items': [
                            {
                                '$ref': '#/effects/dropDown'
                            },
                            {
                                '$ref': '#/effects/noValue'
                            },
                            {
                                '$ref': '#/effects/noValue'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/noValue'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/noValue'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/noValue'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/noValue'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            }
                        ],
                        'title': 'Effects',
                        'type': 'array'
                    },
                    'ix': {
                        'description': 'Effect Index. Used for expressions.',
                        'title': 'Effect Index',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'ty': {
                        'const': 23,
                        'description': 'Effect type.',
                        'title': 'Type',
                        'type': 'number'
                    }
                },
                'type': 'object'
            },
            'slider': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ix': {
                        'description': 'Effect Index. Used for expressions.',
                        'title': 'Effect Index',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'ty': {
                        'const': 0,
                        'description': 'Effect type.',
                        'title': 'Type',
                        'type': 'number'
                    },
                    'v': {
                        'description': 'Effect value.',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Value',
                        'type': 'object'
                    }
                },
                'type': 'object'
            },
            'stroke': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ef': {
                        'description': 'Effect List of properties.',
                        'items': [
                            {
                                '$ref': '#/effects/color'
                            },
                            {
                                '$ref': '#/effects/checkbox'
                            },
                            {
                                '$ref': '#/effects/checkbox'
                            },
                            {
                                '$ref': '#/effects/color'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/slider'
                            },
                            {
                                '$ref': '#/effects/dropDown'
                            },
                            {
                                '$ref': '#/effects/dropDown'
                            }
                        ],
                        'title': 'Effects',
                        'type': 'array'
                    },
                    'ix': {
                        'description': 'Effect Index. Used for expressions.',
                        'title': 'Effect Index',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'ty': {
                        'const': 22,
                        'description': 'Effect type.',
                        'title': 'Type',
                        'type': 'number'
                    }
                },
                'type': 'object'
            },
            'tint': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ef': {
                        'description': 'Effect List of properties.',
                        'items': [
                            {
                                '$ref': '#/effects/color'
                            },
                            {
                                '$ref': '#/effects/color'
                            },
                            {
                                '$ref': '#/effects/slider'
                            }
                        ],
                        'title': 'Effects',
                        'type': 'array'
                    },
                    'ix': {
                        'description': 'Effect Index. Used for expressions.',
                        'title': 'Effect Index',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'ty': {
                        'const': 20,
                        'description': 'Effect type.',
                        'title': 'Type',
                        'type': 'number'
                    }
                },
                'type': 'object'
            },
            'tritone': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ef': {
                        'description': 'Effect List of properties.',
                        'items': [
                            {
                                '$ref': '#/effects/color'
                            },
                            {
                                '$ref': '#/effects/color'
                            },
                            {
                                '$ref': '#/effects/color'
                            },
                            {
                                '$ref': '#/effects/slider'
                            }
                        ],
                        'title': 'Effects',
                        'type': 'array'
                    },
                    'ix': {
                        'description': 'Effect Index. Used for expressions.',
                        'title': 'Effect Index',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'ty': {
                        'const': 23,
                        'description': 'Effect type.',
                        'title': 'Type',
                        'type': 'number'
                    }
                },
                'type': 'object'
            }
        },
        'helpers': {
            'blendMode': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'default': 0,
                'oneOf': [
                    {
                        'const': 0,
                        'standsFor': 'normal'
                    },
                    {
                        'const': 1,
                        'standsFor': 'multiply'
                    },
                    {
                        'const': 2,
                        'standsFor': 'screen'
                    },
                    {
                        'const': 3,
                        'standsFor': 'overlay'
                    },
                    {
                        'const': 4,
                        'standsFor': 'darken'
                    },
                    {
                        'const': 5,
                        'standsFor': 'lighten'
                    },
                    {
                        'const': 6,
                        'standsFor': 'colorDodge'
                    },
                    {
                        'const': 7,
                        'standsFor': 'colorBurn'
                    },
                    {
                        'const': 8,
                        'standsFor': 'hardLight'
                    },
                    {
                        'const': 9,
                        'standsFor': 'softLight'
                    },
                    {
                        'const': 10,
                        'standsFor': 'difference'
                    },
                    {
                        'const': 11,
                        'standsFor': 'exclusion'
                    },
                    {
                        'const': 12,
                        'standsFor': 'hue'
                    },
                    {
                        'const': 13,
                        'standsFor': 'saturation'
                    },
                    {
                        'const': 14,
                        'standsFor': 'color'
                    },
                    {
                        'const': 15,
                        'standsFor': 'luminosity'
                    }
                ],
                'type': 'number'
            },
            'boolean': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'oneOf': [
                    {
                        'const': 0,
                        'standsFor': False
                    },
                    {
                        'const': 1,
                        'standsFor': True
                    }
                ],
                'type': 'number'
            },
            'composite': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'default': 1,
                'oneOf': [
                    {
                        'const': 1,
                        'standsFor': 'Above'
                    },
                    {
                        'const': 2,
                        'standsFor': 'Below'
                    }
                ],
                'type': 'number'
            },
            'lineCap': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'default': 2,
                'oneOf': [
                    {
                        'const': 1,
                        'standsFor': 'butt'
                    },
                    {
                        'const': 2,
                        'standsFor': 'round'
                    },
                    {
                        'const': 3,
                        'standsFor': 'square'
                    }
                ],
                'type': 'number'
            },
            'lineJoin': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'default': 2,
                'oneOf': [
                    {
                        'const': 1,
                        'standsFor': 'miter'
                    },
                    {
                        'const': 2,
                        'standsFor': 'round'
                    },
                    {
                        'const': 3,
                        'standsFor': 'bevel'
                    }
                ],
                'type': 'number'
            },
            'mask': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'inv': {
                        'default': False,
                        'description': 'Inverted Mask flag',
                        'title': 'Inverted',
                        'type': 'boolean'
                    },
                    'mode': {
                        'default': 'a',
                        'description': 'Mask mode. Not all mask types are supported.',
                        'oneOf': [
                            {
                                'const': 'n',
                                'standsFor': 'None'
                            },
                            {
                                'const': 'a',
                                'standsFor': 'Additive'
                            },
                            {
                                'const': 's',
                                'standsFor': 'Subtract'
                            },
                            {
                                'const': 'i',
                                'standsFor': 'Intersect'
                            },
                            {
                                'const': 'l',
                                'standsFor': 'Lighten'
                            },
                            {
                                'const': 'd',
                                'standsFor': 'Darken'
                            },
                            {
                                'const': 'f',
                                'standsFor': 'Difference'
                            }
                        ],
                        'title': 'Mode',
                        'type': 'string'
                    },
                    'nm': {
                        'description': 'Mask name. Used for expressions and effects.',
                        'title': 'Name',
                        'type': 'string'
                    },
                    'o': {
                        'default': {
                            'a': 0,
                            'k': 100
                        },
                        'description': 'Mask opacity.',
                        'oneOf': [
                            {
                                '$ref': '#/properties/const'
                            },
                            {
                                '$ref': '#/properties/constKeyframed'
                            }
                        ],
                        'title': 'Opacity',
                        'type': 'object'
                    },
                    'pt': {
                        'description': 'Mask vertices',
                        'oneOf': [
                            {
                                '$ref': '#/properties/shape'
                            },
                            {
                                '$ref': '#/properties/shapeKeyframed'
                            }
                        ],
                        'title': 'Points',
                        'type': 'object'
                    }
                },
                'type': 'object'
            },
            'textBased': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'default': 1,
                'oneOf': [
                    {
                        'const': 1,
                        'standsFor': 'Characters'
                    },
                    {
                        'const': 2,
                        'standsFor': 'Character Excluding Spaces'
                    },
                    {
                        'const': 3,
                        'standsFor': 'Words'
                    },
                    {
                        'const': 4,
                        'standsFor': 'Lines'
                    }
                ],
                'type': 'number'
            },
            'textGrouping': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'default': 1,
                'oneOf': [
                    {
                        'const': 1,
                        'standsFor': 'Characters'
                    },
                    {
                        'const': 2,
                        'standsFor': 'Word'
                    },
                    {
                        'const': 3,
                        'standsFor': 'Line'
                    },
                    {
                        'const': 4,
                        'standsFor': 'All'
                    }
                ],
                'type': 'number'
            },
            'textShape': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'default': 1,
                'oneOf': [
                    {
                        'const': 1,
                        'standsFor': 'Square'
                    },
                    {
                        'const': 2,
                        'standsFor': 'Ramp Up'
                    },
                    {
                        'const': 3,
                        'standsFor': 'Ramp Down'
                    },
                    {
                        'const': 4,
                        'standsFor': 'Triangle'
                    },
                    {
                        'const': 5,
                        'standsFor': 'Round'
                    },
                    {
                        'const': 6,
                        'standsFor': 'Smooth'
                    }
                ],
                'type': 'number'
            },
            'transform': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'a': {
                        'default': {
                            'a': 0,
                            'k': [
                                0,
                                0,
                                0
                            ]
                        },
                        'description': 'Transform Anchor Point',
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Anchor Point',
                        'type': 'object'
                    },
                    'o': {
                        'default': {
                            'a': 0,
                            'k': 100
                        },
                        'description': 'Transform Opacity',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Opacity',
                        'type': 'object'
                    },
                    'p': {
                        'default': {
                            'a': 0,
                            'k': [
                                0,
                                0,
                                0
                            ]
                        },
                        'description': 'Transform Position',
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Position',
                        'type': 'object'
                    },
                    'px': {
                        'default': {
                            'a': 0,
                            'k': 0
                        },
                        'description': 'Transform Position X',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Position X',
                        'type': 'object'
                    },
                    'py': {
                        'default': {
                            'a': 0,
                            'k': 0
                        },
                        'description': 'Transform Position Y',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Position Y',
                        'type': 'object'
                    },
                    'pz': {
                        'default': {
                            'a': 0,
                            'k': 0
                        },
                        'description': 'Transform Position Z',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Position Z',
                        'type': 'object'
                    },
                    'r': {
                        'default': {
                            'a': 0,
                            'k': 0
                        },
                        'description': 'Transform Rotation',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Rotation',
                        'type': 'object'
                    },
                    's': {
                        'default': {
                            'a': 0,
                            'k': [
                                100,
                                100,
                                100
                            ]
                        },
                        'description': 'Transform Scale',
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Scale',
                        'type': 'object'
                    },
                    'sa': {
                        'default': {
                            'a': 0,
                            'k': 0
                        },
                        'description': 'Transform Skew Axis',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Skew Axis',
                        'type': 'object'
                    },
                    'sk': {
                        'default': {
                            'a': 0,
                            'k': 0
                        },
                        'description': 'Transform Skew',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Skew',
                        'type': 'object'
                    }
                },
                'type': 'object'
            }
        },
        'layers': {
            'comp': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ao': {
                        'description': 'Auto-Orient along path AE property.',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/boolean'
                            }
                        ],
                        'title': 'Auto-Orient',
                        'type': 'number'
                    },
                    'bm': {
                        'default': 0,
                        'description': 'Blend Mode',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/blendMode'
                            }
                        ],
                        'title': 'Blend Mode',
                        'type': 'number'
                    },
                    'cl': {
                        'description': 'Parsed layer name used as html class on SVG/HTML renderer',
                        'title': 'Class',
                        'type': 'string'
                    },
                    'ddd': {
                        'default': 0,
                        'description': '3d layer flag',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/boolean'
                            }
                        ],
                        'title': '3d Layer',
                        'type': 'number'
                    },
                    'ef': {
                        'description': 'List of Effects',
                        'items': {
                            'oneOf': [
                                {
                                    '$ref': '#/effects/index'
                                }
                            ],
                            'type': 'object'
                        },
                        'title': 'Effects',
                        'type': 'array'
                    },
                    'hasMask': {
                        'description': 'Boolean when layer has a mask. Will be deprecated in favor of checking masksProperties.',
                        'title': 'Has Masks',
                        'type': 'number'
                    },
                    'ind': {
                        'description': 'Layer index in AE. Used for parenting and expressions.',
                        'title': 'Index',
                        'type': 'number'
                    },
                    'ip': {
                        'description': 'In Point of layer. Sets the initial frame of the layer.',
                        'title': 'In Point',
                        'type': 'number'
                    },
                    'ks': {
                        'description': 'Transform properties',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/transform'
                            }
                        ],
                        'title': 'Transform',
                        'type': 'object'
                    },
                    'ln': {
                        'description': 'Parsed layer name used as html id on SVG/HTML renderer',
                        'title': 'layer HTML ID',
                        'type': 'string'
                    },
                    'masksProperties': {
                        'description': 'List of Masks',
                        'items': {
                            'oneOf': [
                                {
                                    '$ref': '#/helpers/mask'
                                }
                            ],
                            'type': 'object'
                        },
                        'title': 'Masks Properties',
                        'type': 'array'
                    },
                    'nm': {
                        'description': 'After Effects Layer Name. Used for expressions.',
                        'title': 'Name',
                        'type': 'string'
                    },
                    'op': {
                        'description': 'Out Point of layer. Sets the final frame of the layer.',
                        'title': 'Out Point',
                        'type': 'number'
                    },
                    'parent': {
                        'description': 'Layer Parent. Uses ind of parent.',
                        'title': 'Parent',
                        'type': 'number'
                    },
                    'refId': {
                        'description': "id pointing to the source composition defined on 'assets' object",
                        'title': 'Reference ID',
                        'type': 'string'
                    },
                    'sr': {
                        'default': 1,
                        'description': 'Layer Time Stretching',
                        'title': 'Stretch',
                        'type': 'number'
                    },
                    'st': {
                        'description': 'Start Time of layer. Sets the start time of the layer.',
                        'title': 'Start Time',
                        'type': 'number'
                    },
                    'tm': {
                        'description': "Comp's Time remapping",
                        'oneOf': [
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Time Remapping',
                        'type': 'number'
                    },
                    'ty': {
                        'const': 0,
                        'description': 'Type of layer: Precomp.',
                        'title': 'Type',
                        'type': 'number'
                    }
                },
                'type': 'object'
            },
            'image': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ao': {
                        'default': 0,
                        'description': 'Auto-Orient along path AE property.',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/boolean'
                            }
                        ],
                        'title': 'Auto-Orient',
                        'type': 'number'
                    },
                    'bm': {
                        'default': 0,
                        'description': 'Blend Mode',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/blendMode'
                            }
                        ],
                        'title': 'Blend Mode',
                        'type': 'number'
                    },
                    'cl': {
                        'description': 'Parsed layer name used as html class on SVG/HTML renderer',
                        'title': 'Class',
                        'type': 'string'
                    },
                    'ddd': {
                        'default': 0,
                        'description': '3d layer flag',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/boolean'
                            }
                        ],
                        'title': '3d Layer',
                        'type': 'number'
                    },
                    'ef': {
                        'description': 'List of Effects',
                        'items': {
                            'oneOf': [
                                {
                                    '$ref': '#/effects/index'
                                }
                            ],
                            'type': 'object'
                        },
                        'title': 'Effects',
                        'type': 'array'
                    },
                    'hasMask': {
                        'description': 'Boolean when layer has a mask. Will be deprecated in favor of checking masksProperties.',
                        'title': 'Has Masks',
                        'type': 'number'
                    },
                    'ind': {
                        'description': 'Layer index in AE. Used for parenting and expressions.',
                        'title': 'Index',
                        'type': 'number'
                    },
                    'ip': {
                        'description': 'In Point of layer. Sets the initial frame of the layer.',
                        'title': 'In Point',
                        'type': 'number'
                    },
                    'ks': {
                        'description': 'Transform properties',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/transform'
                            }
                        ],
                        'title': 'Transform',
                        'type': 'object'
                    },
                    'ln': {
                        'description': 'Parsed layer name used as html id on SVG/HTML renderer',
                        'title': 'layer HTML ID',
                        'type': 'string'
                    },
                    'masksProperties': {
                        'description': 'List of Masks',
                        'items': {
                            'oneOf': [
                                {
                                    '$ref': '#/helpers/mask'
                                }
                            ],
                            'type': 'object'
                        },
                        'title': 'Masks Properties',
                        'type': 'array'
                    },
                    'nm': {
                        'description': 'After Effects Layer Name. Used for expressions.',
                        'title': 'Name',
                        'type': 'string'
                    },
                    'op': {
                        'description': 'Out Point of layer. Sets the final frame of the layer.',
                        'title': 'Out Point',
                        'type': 'number'
                    },
                    'parent': {
                        'description': 'Layer Parent. Uses ind of parent.',
                        'title': 'Parent',
                        'type': 'number'
                    },
                    'refId': {
                        'description': "id pointing to the source image defined on 'assets' object",
                        'title': 'Reference ID',
                        'type': 'string'
                    },
                    'sr': {
                        'default': 1,
                        'description': 'Layer Time Stretching',
                        'title': 'Stretch',
                        'type': 'number'
                    },
                    'st': {
                        'description': 'Start Time of layer. Sets the start time of the layer.',
                        'title': 'Start Time',
                        'type': 'number'
                    },
                    'ty': {
                        'const': 2,
                        'description': 'Type of layer: Image.',
                        'title': 'Type',
                        'type': 'number'
                    }
                },
                'type': 'object'
            },
            'null': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ao': {
                        'default': 0,
                        'description': 'Auto-Orient along path AE property.',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/boolean'
                            }
                        ],
                        'title': 'Auto-Orient',
                        'type': 'number'
                    },
                    'cl': {
                        'description': 'Parsed layer name used as html class on SVG/HTML renderer',
                        'title': 'Class',
                        'type': 'string'
                    },
                    'ddd': {
                        'default': 0,
                        'description': '3d layer flag',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/boolean'
                            }
                        ],
                        'title': '3d Layer',
                        'type': 'number'
                    },
                    'ef': {
                        'description': 'List of Effects',
                        'items': {
                            'oneOf': [
                                {
                                    '$ref': '#/effects/index'
                                }
                            ],
                            'type': 'object'
                        },
                        'title': 'Effects',
                        'type': 'array'
                    },
                    'ind': {
                        'description': 'Layer index in AE. Used for parenting and expressions.',
                        'title': 'Index',
                        'type': 'number'
                    },
                    'ip': {
                        'description': 'In Point of layer. Sets the initial frame of the layer.',
                        'title': 'In Point',
                        'type': 'number'
                    },
                    'ks': {
                        'description': 'Transform properties',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/transform'
                            }
                        ],
                        'title': 'Transform',
                        'type': 'object'
                    },
                    'ln': {
                        'description': 'Parsed layer name used as html id on SVG/HTML renderer',
                        'title': 'layer HTML ID',
                        'type': 'string'
                    },
                    'nm': {
                        'description': 'After Effects Layer Name. Used for expressions.',
                        'title': 'Name',
                        'type': 'string'
                    },
                    'op': {
                        'description': 'Out Point of layer. Sets the final frame of the layer.',
                        'title': 'Out Point',
                        'type': 'number'
                    },
                    'parent': {
                        'description': 'Layer Parent. Uses ind of parent.',
                        'title': 'Parent',
                        'type': 'number'
                    },
                    'sr': {
                        'default': 1,
                        'description': 'Layer Time Stretching',
                        'title': 'Stretch',
                        'type': 'number'
                    },
                    'st': {
                        'description': 'Start Time of layer. Sets the start time of the layer.',
                        'title': 'Start Time',
                        'type': 'number'
                    },
                    'ty': {
                        'const': 3,
                        'description': 'Type of layer: Null.',
                        'title': 'Type',
                        'type': 'number'
                    }
                },
                'type': 'object'
            },
            'shape': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ao': {
                        'default': 0,
                        'description': 'Auto-Orient along path AE property.',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/boolean'
                            }
                        ],
                        'title': 'Auto-Orient',
                        'type': 'number'
                    },
                    'bm': {
                        'default': 0,
                        'description': 'Blend Mode',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/blendMode'
                            }
                        ],
                        'title': 'Blend Mode',
                        'type': 'number'
                    },
                    'cl': {
                        'description': 'Parsed layer name used as html class on SVG/HTML renderer',
                        'title': 'Class',
                        'type': 'string'
                    },
                    'ddd': {
                        'default': 0,
                        'description': '3d layer flag',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/boolean'
                            }
                        ],
                        'title': '3d Layer',
                        'type': 'number'
                    },
                    'ef': {
                        'description': 'List of Effects',
                        'items': {
                            'oneOf': [
                                {
                                    '$ref': '#/effects/index'
                                }
                            ],
                            'type': 'object'
                        },
                        'title': 'Effects',
                        'type': 'array'
                    },
                    'hasMask': {
                        'description': 'Boolean when layer has a mask. Will be deprecated in favor of checking masksProperties.',
                        'title': 'Has Masks',
                        'type': 'number'
                    },
                    'ind': {
                        'description': 'Layer index in AE. Used for parenting and expressions.',
                        'title': 'Index',
                        'type': 'number'
                    },
                    'ip': {
                        'description': 'In Point of layer. Sets the initial frame of the layer.',
                        'title': 'In Point',
                        'type': 'number'
                    },
                    'it': {
                        'description': 'Shape list of items',
                        'items': {
                            'oneOf': [
                                {
                                    '$ref': '#/shapes/shape'
                                },
                                {
                                    '$ref': '#/shapes/rect'
                                },
                                {
                                    '$ref': '#/shapes/ellipse'
                                },
                                {
                                    '$ref': '#/shapes/star'
                                },
                                {
                                    '$ref': '#/shapes/fill'
                                },
                                {
                                    '$ref': '#/shapes/gFill'
                                },
                                {
                                    '$ref': '#/shapes/gStroke'
                                },
                                {
                                    '$ref': '#/shapes/stroke'
                                },
                                {
                                    '$ref': '#/shapes/merge'
                                },
                                {
                                    '$ref': '#/shapes/trim'
                                },
                                {
                                    '$ref': '#/shapes/group'
                                },
                                {
                                    '$ref': '#/shapes/roundedCorners'
                                },
                                {
                                    '$ref': '#/shapes/repeater'
                                }
                            ],
                            'type': 'object'
                        },
                        'title': 'Items',
                        'type': 'array'
                    },
                    'ks': {
                        'description': 'Transform properties',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/transform'
                            }
                        ],
                        'title': 'Transform',
                        'type': 'object'
                    },
                    'ln': {
                        'description': 'Parsed layer name used as html id on SVG/HTML renderer',
                        'title': 'layer HTML ID',
                        'type': 'string'
                    },
                    'masksProperties': {
                        'description': 'List of Masks',
                        'items': {
                            'oneOf': [
                                {
                                    '$ref': '#/helpers/mask'
                                }
                            ],
                            'type': 'object'
                        },
                        'title': 'Masks Properties',
                        'type': 'array'
                    },
                    'nm': {
                        'description': 'After Effects Layer Name. Used for expressions.',
                        'title': 'Name',
                        'type': 'string'
                    },
                    'op': {
                        'description': 'Out Point of layer. Sets the final frame of the layer.',
                        'title': 'Out Point',
                        'type': 'number'
                    },
                    'parent': {
                        'description': 'Layer Parent. Uses ind of parent.',
                        'title': 'Parent',
                        'type': 'number'
                    },
                    'sr': {
                        'default': 1,
                        'description': 'Layer Time Stretching',
                        'title': 'Stretch',
                        'type': 'number'
                    },
                    'st': {
                        'description': 'Start Time of layer. Sets the start time of the layer.',
                        'title': 'Start Time',
                        'type': 'number'
                    },
                    'ty': {
                        'const': 4,
                        'description': 'Type of layer: Shape.',
                        'title': 'Type',
                        'type': 'number'
                    }
                },
                'type': 'object'
            },
            'solid': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ao': {
                        'default': 0,
                        'description': 'Auto-Orient along path AE property.',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/boolean'
                            }
                        ],
                        'title': 'Auto-Orient',
                        'type': 'number'
                    },
                    'bm': {
                        'default': 0,
                        'description': 'Blend Mode',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/blendMode'
                            }
                        ],
                        'title': 'Blend Mode',
                        'type': 'number'
                    },
                    'cl': {
                        'description': 'Parsed layer name used as html class on SVG/HTML renderer',
                        'title': 'Class',
                        'type': 'string'
                    },
                    'ddd': {
                        'default': 0,
                        'description': '3d layer flag',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/boolean'
                            }
                        ],
                        'title': '3d Layer',
                        'type': 'number'
                    },
                    'ef': {
                        'description': 'Auto-Orient along path AE property.',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/boolean'
                            }
                        ],
                        'title': 'Effects',
                        'type': 'number'
                    },
                    'hasMask': {
                        'description': 'Boolean when layer has a mask. Will be deprecated in favor of checking masksProperties.',
                        'title': 'Has Masks',
                        'type': 'number'
                    },
                    'ind': {
                        'description': 'Layer index in AE. Used for parenting and expressions.',
                        'title': 'Index',
                        'type': 'number'
                    },
                    'ip': {
                        'description': 'In Point of layer. Sets the initial frame of the layer.',
                        'title': 'In Point',
                        'type': 'number'
                    },
                    'ks': {
                        'description': 'Transform properties',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/transform'
                            }
                        ],
                        'title': 'Transform',
                        'type': 'object'
                    },
                    'ln': {
                        'description': 'Parsed layer name used as html id on SVG/HTML renderer',
                        'title': 'layer HTML ID',
                        'type': 'string'
                    },
                    'masksProperties': {
                        'description': 'List of Masks',
                        'items': {
                            'oneOf': [
                                {
                                    '$ref': '#/helpers/mask'
                                }
                            ],
                            'type': 'object'
                        },
                        'title': 'Masks Properties',
                        'type': 'array'
                    },
                    'nm': {
                        'description': 'After Effects Layer Name. Used for expressions.',
                        'title': 'Name',
                        'type': 'string'
                    },
                    'op': {
                        'description': 'Out Point of layer. Sets the final frame of the layer.',
                        'title': 'Out Point',
                        'type': 'number'
                    },
                    'parent': {
                        'description': 'Layer Parent. Uses ind of parent.',
                        'title': 'Parent',
                        'type': 'number'
                    },
                    'sc': {
                        'description': 'Color of the solid in hex',
                        'title': 'Solid Color',
                        'type': 'string'
                    },
                    'sh': {
                        'description': 'Height of the solid.',
                        'title': 'Solid Height',
                        'type': 'number'
                    },
                    'sr': {
                        'default': 1,
                        'description': 'Layer Time Stretching',
                        'title': 'Stretch',
                        'type': 'number'
                    },
                    'st': {
                        'description': 'Start Time of layer. Sets the start time of the layer.',
                        'title': 'Start Time',
                        'type': 'number'
                    },
                    'sw': {
                        'description': 'Width of the solid.',
                        'title': 'Solid Width',
                        'type': 'number'
                    },
                    'ty': {
                        'const': 1,
                        'description': 'Type of layer: Solid.',
                        'title': 'Type',
                        'type': 'number'
                    }
                },
                'type': 'object'
            },
            'text': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ao': {
                        'default': 0,
                        'description': 'Auto-Orient along path AE property.',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/boolean'
                            }
                        ],
                        'title': 'Auto-Orient',
                        'type': 'number'
                    },
                    'bm': {
                        'default': 0,
                        'description': 'Blend Mode',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/blendMode'
                            }
                        ],
                        'title': 'Blend Mode',
                        'type': 'number'
                    },
                    'cl': {
                        'description': 'Parsed layer name used as html class on SVG/HTML renderer',
                        'title': 'Class',
                        'type': 'string'
                    },
                    'ddd': {
                        'default': 0,
                        'description': '3d layer flag',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/boolean'
                            }
                        ],
                        'title': '3d Layer',
                        'type': 'number'
                    },
                    'ef': {
                        'description': 'Auto-Orient along path AE property.',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/boolean'
                            }
                        ],
                        'title': 'Effects',
                        'type': 'number'
                    },
                    'hasMask': {
                        'description': 'Boolean when layer has a mask. Will be deprecated in favor of checking masksProperties.',
                        'title': 'Has Masks',
                        'type': 'number'
                    },
                    'ind': {
                        'description': 'Layer index in AE. Used for parenting and expressions.',
                        'title': 'Index',
                        'type': 'number'
                    },
                    'ip': {
                        'description': 'In Point of layer. Sets the initial frame of the layer.',
                        'title': 'In Point',
                        'type': 'number'
                    },
                    'ks': {
                        'description': 'Transform properties',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/transform'
                            }
                        ],
                        'title': 'Transform',
                        'type': 'object'
                    },
                    'ln': {
                        'description': 'Parsed layer name used as html id on SVG/HTML renderer',
                        'title': 'layer HTML ID',
                        'type': 'string'
                    },
                    'masksProperties': {
                        'description': 'List of Masks',
                        'items': {
                            'oneOf': [
                                {
                                    '$ref': '#/helpers/mask'
                                }
                            ],
                            'type': 'object'
                        },
                        'title': 'Masks Properties',
                        'type': 'array'
                    },
                    'nm': {
                        'description': 'After Effects Layer Name. Used for expressions.',
                        'title': 'Name',
                        'type': 'string'
                    },
                    'op': {
                        'description': 'Out Point of layer. Sets the final frame of the layer.',
                        'title': 'Out Point',
                        'type': 'number'
                    },
                    'parent': {
                        'description': 'Layer Parent. Uses ind of parent.',
                        'title': 'Parent',
                        'type': 'number'
                    },
                    'sr': {
                        'default': 1,
                        'description': 'Layer Time Stretching',
                        'title': 'Stretch',
                        'type': 'number'
                    },
                    'st': {
                        'description': 'Start Time of layer. Sets the start time of the layer.',
                        'title': 'Start Time',
                        'type': 'number'
                    },
                    't': {
                        'description': 'Text Data',
                        'properties': {
                            'an_': {
                                'description': 'Text animators',
                                'items': {
                                    'properties': {
                                        'ap_': {
                                            'description': 'Text animator animated properties',
                                            'properties': {
                                                'a_': {
                                                    'description': 'Text animator Anchor Point',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/multiDimensional'
                                                        },
                                                        {
                                                            '$ref': '#/properties/multiDimensionalKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Anchor Point',
                                                    'type': 'object'
                                                },
                                                'fc_': {
                                                    'description': 'Text animator Fill Color',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/multiDimensional'
                                                        },
                                                        {
                                                            '$ref': '#/properties/multiDimensionalKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Fill Color',
                                                    'type': 'object'
                                                },
                                                'flb_': {
                                                    'description': 'Text animator Fill Brightness',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/value'
                                                        },
                                                        {
                                                            '$ref': '#/properties/valueKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Fill Brightness',
                                                    'type': 'object'
                                                },
                                                'flh_': {
                                                    'description': 'Text animator Fill Hue',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/value'
                                                        },
                                                        {
                                                            '$ref': '#/properties/valueKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Fill Hue',
                                                    'type': 'object'
                                                },
                                                'fls_': {
                                                    'description': 'Text animator Fill Saturation',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/value'
                                                        },
                                                        {
                                                            '$ref': '#/properties/valueKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Fill Saturation',
                                                    'type': 'object'
                                                },
                                                'o_': {
                                                    'description': 'Text animator Opacity',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/value'
                                                        },
                                                        {
                                                            '$ref': '#/properties/valueKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Opacity',
                                                    'type': 'object'
                                                },
                                                'p_': {
                                                    'description': 'Text animator Position',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/multiDimensional'
                                                        },
                                                        {
                                                            '$ref': '#/properties/multiDimensionalKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Position',
                                                    'type': 'object'
                                                },
                                                'r_': {
                                                    'description': 'Text animator Rotation',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/value'
                                                        },
                                                        {
                                                            '$ref': '#/properties/valueKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Rotation',
                                                    'type': 'object'
                                                },
                                                'sc': {
                                                    'description': 'Text animator Scale',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/multiDimensional'
                                                        },
                                                        {
                                                            '$ref': '#/properties/multiDimensionalKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Scale',
                                                    'type': 'object'
                                                },
                                                'sk_': {
                                                    'description': 'Text animator Skew',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/value'
                                                        },
                                                        {
                                                            '$ref': '#/properties/valueKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Skew',
                                                    'type': 'object'
                                                },
                                                'ska_': {
                                                    'description': 'Text animator Skew Axis',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/value'
                                                        },
                                                        {
                                                            '$ref': '#/properties/valueKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Skew Axis',
                                                    'type': 'object'
                                                },
                                                'stc_': {
                                                    'description': 'Text animator Stroke Color',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/multiDimensional'
                                                        },
                                                        {
                                                            '$ref': '#/properties/multiDimensionalKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Stroke Color',
                                                    'type': 'object'
                                                },
                                                'stw_': {
                                                    'description': 'Text animator Stroke Width',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/value'
                                                        },
                                                        {
                                                            '$ref': '#/properties/valueKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Stroke Width',
                                                    'type': 'object'
                                                },
                                                'tr_': {
                                                    'description': 'Text animator Tracking',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/value'
                                                        },
                                                        {
                                                            '$ref': '#/properties/valueKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Tracking',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': 'Animated Properties',
                                            'type': 'object'
                                        },
                                        'rs_': {
                                            'description': 'Animators Range Selecton',
                                            'properties': {
                                                'bo_': {
                                                    'description': 'Selector Based On',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/helpers/textBased'
                                                        }
                                                    ],
                                                    'title': 'Based On',
                                                    'type': 'number'
                                                },
                                                'e_': {
                                                    'description': 'Selector End',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/value'
                                                        },
                                                        {
                                                            '$ref': '#/properties/valueKeyframed'
                                                        }
                                                    ],
                                                    'title': 'End',
                                                    'type': 'number'
                                                },
                                                'ma_': {
                                                    'description': 'Selector Max Amount',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/value'
                                                        },
                                                        {
                                                            '$ref': '#/properties/valueKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Max Amount',
                                                    'type': 'number'
                                                },
                                                'maxe_': {
                                                    'description': 'Levels Max Ease',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/value'
                                                        },
                                                        {
                                                            '$ref': '#/properties/valueKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Max Ease',
                                                    'type': 'number'
                                                },
                                                'mine_': {
                                                    'description': 'Levels Min Ease',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/value'
                                                        },
                                                        {
                                                            '$ref': '#/properties/valueKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Min Ease',
                                                    'type': 'number'
                                                },
                                                'of_': {
                                                    'description': 'Selector Offset',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/value'
                                                        },
                                                        {
                                                            '$ref': '#/properties/valueKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Offset',
                                                    'type': 'number'
                                                },
                                                'rand_': {
                                                    'description': 'Selector Randomize Order',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/helpers/boolean'
                                                        }
                                                    ],
                                                    'title': 'Randomize',
                                                    'type': 'number'
                                                },
                                                'ru_': {
                                                    'description': 'Selector Range Units. Percentage or Index.',
                                                    'title': 'Range Units',
                                                    'type': 'number'
                                                },
                                                'sh_': {
                                                    'description': 'Selector Shape',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/helpers/textShape'
                                                        }
                                                    ],
                                                    'title': 'Shape',
                                                    'type': 'number'
                                                },
                                                'st_': {
                                                    'description': 'Selector Start',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/value'
                                                        },
                                                        {
                                                            '$ref': '#/properties/valueKeyframed'
                                                        }
                                                    ],
                                                    'title': 'Start',
                                                    'type': 'number'
                                                },
                                                't_': {
                                                    'description': 'Selector Type. Expressible, or Normal.',
                                                    'title': 'Type',
                                                    'type': 'number'
                                                }
                                            },
                                            'title': 'Range Selecton',
                                            'type': 'object'
                                        }
                                    },
                                    'type': 'object'
                                },
                                'title': 'Animators',
                                'type': 'array'
                            },
                            'doc_': {
                                'description': 'Text Document Data',
                                'properties': {
                                    'kf_': {
                                        'description': 'Text Document Data Keyframes',
                                        'items': {
                                            'oneOf': [
                                                {
                                                    'properties': {
                                                        't_': {
                                                            'description': 'Keyframe Time',
                                                            'title': 'Time',
                                                            'type': 'number'
                                                        },
                                                        'tp_': {
                                                            'description': 'Text Properties',
                                                            'properties': {
                                                                'f_': {
                                                                    'description': 'Text Font',
                                                                    'title': 'Font',
                                                                    'type': 'string'
                                                                },
                                                                'fc_': {
                                                                    'description': 'Text Font Color',
                                                                    'title': 'Font Color',
                                                                    'type': 'array'
                                                                },
                                                                'j_': {
                                                                    'description': 'Text Justification',
                                                                    'title': 'Justificaiton',
                                                                    'type': 'string'
                                                                },
                                                                'lh_': {
                                                                    'description': 'Text Line Height',
                                                                    'title': 'Line Height',
                                                                    'type': 'number'
                                                                },
                                                                's_': {
                                                                    'description': 'Text Font Size',
                                                                    'title': 'Size',
                                                                    'type': 'number'
                                                                },
                                                                't_': {
                                                                    'description': 'Text String Value',
                                                                    'title': 'Text',
                                                                    'type': 'string'
                                                                },
                                                                'tr_': {
                                                                    'description': 'Text Tracking',
                                                                    'title': 'Tracking',
                                                                    'type': 'number'
                                                                }
                                                            },
                                                            'title': 'Text Properties',
                                                            'type': 'object'
                                                        }
                                                    }
                                                }
                                            ],
                                            'type': 'object'
                                        },
                                        'title': 'Keyframes',
                                        'type': 'array'
                                    }
                                },
                                'title': 'Document',
                                'type': 'object'
                            },
                            'mo_': {
                                'description': 'Text More Options',
                                'properties': {
                                    'apg_': {
                                        'description': 'Text Anchor Point Grouping',
                                        'oneOf': [
                                            {
                                                '$ref': '#/helpers/textGrouping'
                                            }
                                        ],
                                        'title': 'Anchor Point Grouping',
                                        'type': 'number'
                                    },
                                    'ga_': {
                                        'description': 'Text Grouping Alignment',
                                        'oneOf': [
                                            {
                                                '$ref': '#/properties/multiDimensional'
                                            },
                                            {
                                                '$ref': '#/properties/multiDimensionalKeyframed'
                                            }
                                        ],
                                        'title': 'Grouping Alignment',
                                        'type': 'number'
                                    }
                                },
                                'title': 'More Options',
                                'type': 'object'
                            },
                            'tp_': {
                                'description': 'Text Path',
                                'title': 'Text Path',
                                'type': 'number'
                            }
                        },
                        'title': 'Text Data',
                        'type': 'object'
                    },
                    'ty': {
                        'description': 'Type of layer: Text.',
                        'title': 'Type',
                        'type': 'number',
                        'value': 5
                    }
                },
                'type': 'object'
            }
        },
        'properties': {
            'const': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ix': {
                        'description': 'Property Index. Used for expressions.',
                        'extended_name': 'Property Index',
                        'type': 'string'
                    },
                    'k': {
                        'description': 'Property Value',
                        'extended_name': 'Value',
                        'type': 'number'
                    },
                    'x': {
                        'description': 'Property Expression. An AE expression that modifies the value.',
                        'extended_name': 'Expression',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'constKeyframed': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'i': {
                        'description': 'Bezier curve interpolation in value.',
                        'extended_name': 'In Value',
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
                    'o': {
                        'description': 'Bezier curve interpolation out value.',
                        'extended_name': 'Out Value',
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
                    's': {
                        'description': 'Start value of keyframe segment.',
                        'extended_name': 'Start',
                        'type': 'number'
                    },
                    't': {
                        'description': 'Start time of keyframe segment.',
                        'extended_name': 'Time',
                        'type': 'number'
                    }
                },
                'type': 'object'
            },
            'multiDimensional': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ix': {
                        'description': 'Property Index. Used for expressions.',
                        'extended_name': 'Property Index',
                        'type': 'string'
                    },
                    'k': {
                        'description': 'Property Value',
                        'extended_name': 'Value',
                        'items': {
                            'type': 'number'
                        },
                        'type': 'array'
                    },
                    'x': {
                        'description': 'Property Expression. An AE expression that modifies the value.',
                        'extended_name': 'Expression',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'multiDimensionalKeyframed': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ix': {
                        'description': 'Property Index. Used for expressions.',
                        'extended_name': 'Property Index',
                        'type': 'string'
                    },
                    'k': {
                        'description': 'Property Value keyframes',
                        'extended_name': 'Keyframes',
                        'items': {
                            '$ref': '#/properties/offsetKeyframe',
                            'type': 'object'
                        },
                        'type': 'array'
                    },
                    'ti': {
                        'description': 'In Spatial Tangent. Only for spatial properties. Array of numbers.',
                        'extended_name': 'In Tangent',
                        'type': 'array'
                    },
                    'to': {
                        'description': 'Out Spatial Tangent. Only for spatial properties. Array of numbers.',
                        'extended_name': 'Out Tangent',
                        'type': 'array'
                    },
                    'x': {
                        'description': 'Property Expression. An AE expression that modifies the value.',
                        'extended_name': 'Expression',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'offsetKeyframe': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'i': {
                        'description': 'Bezier curve interpolation in value.',
                        'extended_name': 'In Value',
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
                    'o': {
                        'description': 'Bezier curve interpolation out value.',
                        'extended_name': 'Out Value',
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
                'type': 'object'
            },
            'shape': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'a': {
                        'description': 'Defines if property is animated',
                        'extended_name': 'Animated',
                        'type': 'number'
                    },
                    'ix': {
                        'description': 'Property Index. Used for expressions.',
                        'extended_name': 'Property Index',
                        'type': 'string'
                    },
                    'k': {
                        '$ref': '#/properties/shapeProp',
                        'description': 'Property Value',
                        'extended_name': 'Value',
                        'type': 'object'
                    },
                    'x': {
                        'description': 'Property Expression. An AE expression that modifies the value.',
                        'extended_name': 'Expression',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'shapeKeyframed': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ix': {
                        'description': 'Property Index. Used for expressions.',
                        'extended_name': 'Property Index',
                        'type': 'string'
                    },
                    'k': {
                        'description': 'Property Value keyframes',
                        'extended_name': 'Keyframes',
                        'items': {
                            '$ref': '#/properties/shapePropKeyframe',
                            'type': 'object'
                        },
                        'type': 'array'
                    },
                    'ti': {
                        'description': 'In Spatial Tangent. Only for spatial properties. Array of numbers.',
                        'extended_name': 'In Tangent',
                        'type': 'array'
                    },
                    'to': {
                        'description': 'Out Spatial Tangent. Only for spatial properties. Array of numbers.',
                        'extended_name': 'Out Tangent',
                        'type': 'array'
                    },
                    'x': {
                        'description': 'Property Expression. An AE expression that modifies the value.',
                        'extended_name': 'Expression',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'shapeProp': {
                '$schema': 'http://json-schema.org/draft-04/schema',
                'properties': {
                    'c': {
                        'description': 'Closed property of shape',
                        'extended_name': 'Closed',
                        'type': 'boolean'
                    },
                    'i': {
                        'description': 'Bezier curve In points. Array of 2 dimensional arrays.',
                        'extended_name': 'In Point',
                        'items': {
                            'items': {
                                'type': 'number'
                            },
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'
                        },
                        'type': 'array'
                    },
                    'o': {
                        'description': 'Bezier curve Out points. Array of 2 dimensional arrays.',
                        'extended_name': 'Out Point',
                        'items': {
                            'items': {
                                'type': 'number'
                            },
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'
                        },
                        'type': 'array'
                    },
                    'v': {
                        'description': 'Bezier curve Vertices. Array of 2 dimensional arrays.',
                        'extended_name': 'Vertices',
                        'items': {
                            'items': {
                                'type': 'number'
                            },
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'
                        },
                        'type': 'array'
                    }
                },
                'type': 'object'
            },
            'shapePropKeyframe': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'i': {
                        'description': 'Bezier curve interpolation in value.',
                        'extended_name': 'In Value',
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
                    'o': {
                        'description': 'Bezier curve interpolation out value.',
                        'extended_name': 'Out Value',
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
                    's': {
                        'description': 'Start value of keyframe segment.',
                        'extended_name': 'Start',
                        'items': {
                            '$ref': '#/properties/shapeProp',
                            'type': 'object'
                        },
                        'type': 'array'
                    },
                    't': {
                        'description': 'Start time of keyframe segment.',
                        'extended_name': 'Time',
                        'type': 'number'
                    }
                },
                'type': 'object'
            },
            'value': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ix': {
                        'description': 'Property Index. Used for expressions.',
                        'extended_name': 'Property Index',
                        'type': 'string'
                    },
                    'k': {
                        'description': 'Property Value',
                        'extended_name': 'Value',
                        'type': 'number'
                    },
                    'x': {
                        'description': 'Property Expression. An AE expression that modifies the value.',
                        'extended_name': 'Expression',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'valueKeyframe': {
                '$schema': 'http://json-schema.org/draft-04/schema',
                'properties': {
                    'i': {
                        'oneOf': [
                            {
                                'description': 'Bezier curve interpolation in value.',
                                'extended_name': 'In Value',
                                'properties': {
                                    'x': {
                                        'description': 'bezier x axis',
                                        'extended_name': 'X axis',
                                        'type': 'number'
                                    },
                                    'y': {
                                        'description': 'bezier y axis',
                                        'extended_name': 'Y axis',
                                        'type': 'number'
                                    }
                                },
                                'type': 'object'
                            },
                            {
                                'description': 'Bezier curve interpolation in value.',
                                'extended_name': 'In Value',
                                'properties': {
                                    'x': {
                                        'description': 'bezier x axis',
                                        'extended_name': 'X axis',
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    },
                                    'y': {
                                        'description': 'bezier y axis',
                                        'extended_name': 'Y axis',
                                        'items': {
                                            'type': 'number'
                                        },
                                        'type': 'array'
                                    }
                                },
                                'type': 'object'
                            }
                        ],
                        'type': 'object'
                    },
                    's': {
                        'oneOf': [
                            {
                                'description': 'Start value of keyframe segment.',
                                'extended_name': 'Start',
                                'type': 'number'
                            },
                            {
                                'description': 'Start value of keyframe segment.',
                                'extended_name': 'Start',
                                'items': {
                                    'type': 'number'
                                },
                                'type': 'array'
                            }
                        ]
                    },
                    't': {
                        'description': 'Start time of keyframe segment.',
                        'extended_name': 'Time',
                        'type': 'number'
                    }
                },
                'type': 'object'
            },
            'valueKeyframed': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ix': {
                        'description': 'Property Index. Used for expressions.',
                        'extended_name': 'Property Index',
                        'type': 'string'
                    },
                    'k': {
                        'description': 'Property Value keyframes',
                        'extended_name': 'Keyframes',
                        'items': {
                            '$ref': '#/properties/valueKeyframe',
                            'type': 'object'
                        },
                        'type': 'array'
                    },
                    'x': {
                        'description': 'Property Expression. An AE expression that modifies the value.',
                        'extended_name': 'Expression',
                        'type': 'string'
                    }
                },
                'type': 'object'
            }
        },
        'shapes': {
            'ellipse': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'd': {
                        'default': 1,
                        'description': "After Effect's Direction. Direction how the shape is drawn. Used for trim path for example.",
                        'title': 'Direction',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'p': {
                        'description': "Ellipse's position",
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Position',
                        'type': 'object'
                    },
                    's': {
                        'description': "Ellipse's size",
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Size',
                        'type': 'object'
                    },
                    'ty': {
                        'const': 'el',
                        'description': 'Shape content type.',
                        'title': 'Type',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'fill': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'c': {
                        'description': 'Fill Color',
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Color',
                        'type': 'object'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'o': {
                        'description': 'Fill Opacity',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Opacity',
                        'type': 'object'
                    },
                    'ty': {
                        'const': 'fl',
                        'description': 'Shape content type.',
                        'title': 'Type',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'gFill': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'a': {
                        'description': 'Highlight Angle. Only if type is Radial',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Highlight Angle',
                        'type': 'object'
                    },
                    'e': {
                        'description': 'Gradient End Point',
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'End Point',
                        'type': 'object'
                    },
                    'g': {
                        'description': 'Gradient Colors',
                        'title': 'Gradient Colors',
                        'type': 'object'
                    },
                    'h': {
                        'description': 'Gradient Highlight Length. Only if type is Radial',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Highlight Length',
                        'type': 'object'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'o': {
                        'description': 'Fill Opacity',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Opacity',
                        'type': 'object'
                    },
                    's': {
                        'description': 'Gradient Start Point',
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Start Point',
                        'type': 'object'
                    },
                    't': {
                        'description': 'Gradient Type',
                        'oneOf': [
                            {
                                'standsFor': 'Linear',
                                'value': 1
                            },
                            {
                                'standsFor': 'Radial',
                                'value': 2
                            }
                        ],
                        'title': 'Type',
                        'type': 'object'
                    },
                    'ty': {
                        'const': 'gf',
                        'description': 'Shape content type.',
                        'title': 'Type',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'gStroke': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'a': {
                        'description': 'Highlight Angle. Only if type is Radial',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Highlight Angle',
                        'type': 'object'
                    },
                    'e': {
                        'description': 'Gradient End Point',
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'End Point',
                        'type': 'object'
                    },
                    'g': {
                        'description': 'Gradient Colors',
                        'title': 'Gradient Colors',
                        'type': 'object'
                    },
                    'h': {
                        'description': 'Gradient Highlight Length. Only if type is Radial',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Highlight Length',
                        'type': 'object'
                    },
                    'lc': {
                        'description': 'Gradient Stroke Line Cap',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/lineCap'
                            }
                        ],
                        'title': 'Line Cap',
                        'type': 'number'
                    },
                    'lj': {
                        'description': 'Gradient Stroke Line Join',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/lineJoin'
                            }
                        ],
                        'title': 'Line Join',
                        'type': 'number'
                    },
                    'ml': {
                        'description': 'Gradient Stroke Miter Limit. Only if Line Join is set to Miter.',
                        'title': 'Miter Limit',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'o': {
                        'description': 'Stroke Opacity',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Opacity',
                        'type': 'object'
                    },
                    's': {
                        'description': 'Gradient Start Point',
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Start Point',
                        'type': 'object'
                    },
                    't': {
                        'description': 'Gradient Type',
                        'oneOf': [
                            {
                                'standsFor': 'Linear',
                                'value': 1
                            },
                            {
                                'standsFor': 'Radial',
                                'value': 2
                            }
                        ],
                        'title': 'Type',
                        'type': 'object'
                    },
                    'ty': {
                        'const': 'gs',
                        'description': 'Shape content type.',
                        'title': 'Type',
                        'type': 'string'
                    },
                    'w': {
                        'description': 'Gradient Stroke Width',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Stroke Width',
                        'type': 'object'
                    }
                },
                'type': 'object'
            },
            'group': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'it': {
                        'description': 'Group list of items',
                        'items': {
                            'oneOf': [
                                {
                                    '$ref': '#/shapes/shape',
                                    'value': 'sh'
                                },
                                {
                                    '$ref': '#/shapes/rect',
                                    'value': 'rc'
                                },
                                {
                                    '$ref': '#/shapes/ellipse',
                                    'value': 'el'
                                },
                                {
                                    '$ref': '#/shapes/star',
                                    'value': 'sr'
                                },
                                {
                                    '$ref': '#/shapes/fill',
                                    'value': 'fl'
                                },
                                {
                                    '$ref': '#/shapes/gFill',
                                    'value': 'gf'
                                },
                                {
                                    '$ref': '#/shapes/gStroke',
                                    'value': 'gs'
                                },
                                {
                                    '$ref': '#/shapes/stroke',
                                    'value': 'st'
                                },
                                {
                                    '$ref': '#/shapes/merge',
                                    'value': 'mm'
                                },
                                {
                                    '$ref': '#/shapes/trim',
                                    'value': 'tm'
                                },
                                {
                                    '$ref': '#/shapes/group',
                                    'value': 'gr'
                                },
                                {
                                    '$ref': '#/shapes/roundedCorners',
                                    'value': 'rd'
                                },
                                {
                                    '$ref': '#/shapes/transform',
                                    'value': 'tr'
                                }
                            ],
                            'type': 'object'
                        },
                        'title': 'Items',
                        'type': 'array'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'np': {
                        'description': 'Group number of properties. Used for expressions.',
                        'title': 'Number of Properties',
                        'type': 'number'
                    },
                    'ty': {
                        'const': 'gr',
                        'description': 'Shape content type.',
                        'title': 'Type',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'merge': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'mm': {
                        'description': 'Merge Mode',
                        'title': 'Merge Mode',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'ty': {
                        'const': 'mm',
                        'description': "Shape content type. THIS FEATURE IS NOT SUPPORTED. It's exported because if you export it, they will come.",
                        'title': 'Type',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'rect': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'd': {
                        'description': "After Effect's Direction. Direction how the shape is drawn. Used for trim path for example.",
                        'title': 'Direction',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'p': {
                        'description': "Rect's position",
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Position',
                        'type': 'object'
                    },
                    'r': {
                        'description': "Rect's rounded corners",
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Rounded corners',
                        'type': 'object'
                    },
                    's': {
                        'description': "Rect's size",
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Size',
                        'type': 'object'
                    },
                    'ty': {
                        'const': 'rc',
                        'description': 'Shape content type.',
                        'title': 'Type',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'repeater': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'c': {
                        'default': {
                            'a': 0,
                            'k': 1
                        },
                        'description': 'Number of Copies',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Copies',
                        'type': 'object'
                    },
                    'm': {
                        'default': 1,
                        'description': 'Composite of copies',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/composite'
                            }
                        ],
                        'title': 'Composite',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'o': {
                        'default': {
                            'a': 0,
                            'k': 0
                        },
                        'description': 'Offset of Copies',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Offset',
                        'type': 'object'
                    },
                    'tr': {
                        'description': 'Transform values for each repeater copy',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/transform'
                            }
                        ],
                        'title': 'Transform',
                        'type': 'object'
                    },
                    'ty': {
                        'const': 'rp',
                        'description': 'Shape content type.',
                        'title': 'Type',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'roundedCorners': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'r': {
                        'description': 'Rounded Corner Radius',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Radius',
                        'type': 'object'
                    },
                    'ty': {
                        'const': 'rd',
                        'description': 'Shape content type.',
                        'title': 'Type',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'shape': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'd': {
                        'description': "After Effect's Direction. Direction how the shape is drawn. Used for trim path for example.",
                        'title': 'Direction',
                        'type': 'number'
                    },
                    'ks': {
                        'description': "Shape's vertices",
                        'oneOf': [
                            {
                                '$ref': '#/properties/shape'
                            },
                            {
                                '$ref': '#/properties/shapeKeyframed'
                            }
                        ],
                        'title': 'Vertices',
                        'type': 'object'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'ty': {
                        'const': 'sh',
                        'description': 'Shape content type.',
                        'title': 'Type',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'star': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'd': {
                        'description': "After Effect's Direction. Direction how the shape is drawn. Used for trim path for example.",
                        'title': 'Direction',
                        'type': 'number'
                    },
                    'ir': {
                        'description': "Star's inner radius. (Star only)",
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Inner Radius',
                        'type': 'object'
                    },
                    'is': {
                        'description': "Star's inner roundness. (Star only)",
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Inner Roundness',
                        'type': 'object'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'or': {
                        'description': "Star's outer radius.",
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Outer Radius',
                        'type': 'object'
                    },
                    'os': {
                        'description': "Star's outer roundness.",
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Outer Roundness',
                        'type': 'object'
                    },
                    'p': {
                        'description': "Star's position",
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Position',
                        'type': 'object'
                    },
                    'pt': {
                        'description': "Star's number of points.",
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Points',
                        'type': 'object'
                    },
                    'r': {
                        'description': "Star's rotation.",
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Rotation',
                        'type': 'object'
                    },
                    'sy': {
                        'description': "Star's type. Polygon or Star.",
                        'oneOf': [
                            {
                                'standsFor': 'Star',
                                'value': 1
                            },
                            {
                                'standsFor': 'Polygon',
                                'value': 2
                            }
                        ],
                        'title': 'Star Type',
                        'type': 'object'
                    },
                    'ty': {
                        'const': 'sr',
                        'description': 'Shape content type.',
                        'title': 'Type',
                        'type': 'string'
                    }
                },
                'type': 'object'
            },
            'stroke': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'c': {
                        'description': 'Stroke Color',
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Color',
                        'type': 'object'
                    },
                    'lc': {
                        'description': 'Stroke Line Cap',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/lineCap'
                            }
                        ],
                        'title': 'Line Cap',
                        'type': 'number'
                    },
                    'lj': {
                        'description': 'Stroke Line Join',
                        'oneOf': [
                            {
                                '$ref': '#/helpers/lineJoin'
                            }
                        ],
                        'title': 'Line Join',
                        'type': 'number'
                    },
                    'ml': {
                        'description': 'Stroke Miter Limit. Only if Line Join is set to Miter.',
                        'title': 'Miter Limit',
                        'type': 'number'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'o': {
                        'description': 'Stroke Opacity',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Opacity',
                        'type': 'object'
                    },
                    'ty': {
                        'const': 'st',
                        'description': 'Shape content type.',
                        'title': 'Type',
                        'type': 'string'
                    },
                    'w': {
                        'description': 'Stroke Width',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Width',
                        'type': 'object'
                    }
                },
                'type': 'object'
            },
            'transform': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'a': {
                        'description': 'Shape Transform Anchor Point',
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Anchor Point',
                        'type': 'object'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'o': {
                        'description': 'Shape Transform Opacity',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Opacity',
                        'type': 'object'
                    },
                    'p': {
                        'description': 'Shape Transform Position',
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Position',
                        'type': 'object'
                    },
                    'r': {
                        'description': 'Shape Transform Rotation',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Rotation',
                        'type': 'object'
                    },
                    's': {
                        'description': 'Shape Transform Scale',
                        'oneOf': [
                            {
                                '$ref': '#/properties/multiDimensional'
                            },
                            {
                                '$ref': '#/properties/multiDimensionalKeyframed'
                            }
                        ],
                        'title': 'Scale',
                        'type': 'object'
                    },
                    'sa': {
                        'description': 'Shape Transform Skew Axis',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Skew Axis',
                        'type': 'object'
                    },
                    'sk': {
                        'description': 'Shape Transform Skew',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Skew',
                        'type': 'object'
                    }
                },
                'type': 'object'
            },
            'trim': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'e': {
                        'description': 'Trim End.',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'End',
                        'type': 'object'
                    },
                    'mn': {
                        'description': "After Effect's Match Name. Used for expressions.",
                        'title': 'Match Name',
                        'type': 'string'
                    },
                    'nm': {
                        'description': "After Effect's Name. Used for expressions.",
                        'title': 'Name',
                        'type': 'string'
                    },
                    'o': {
                        'description': 'Trim Offset.',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Offset',
                        'type': 'object'
                    },
                    's': {
                        'description': 'Trim Start.',
                        'oneOf': [
                            {
                                '$ref': '#/properties/value'
                            },
                            {
                                '$ref': '#/properties/valueKeyframed'
                            }
                        ],
                        'title': 'Start',
                        'type': 'object'
                    },
                    'ty': {
                        'const': 'tm',
                        'description': 'Shape content type.',
                        'title': 'Type',
                        'type': 'string'
                    }
                },
                'type': 'object'
            }
        },
        'sources': {
            'chars': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'ch': {
                        'description': 'Character Value',
                        'title': 'Character',
                        'type': 'string'
                    },
                    'data': {
                        'description': 'Character Data',
                        'properties': {
                            'cs_': {
                                'description': 'Character Composing Shapes',
                                'items': {
                                    'properties': {
                                        'i_': {
                                            'description': 'Character Items',
                                            'properties': {
                                                'k_': {
                                                    'description': 'Character Items Keys',
                                                    'oneOf': [
                                                        {
                                                            '$ref': '#/properties/shape'
                                                        }
                                                    ],
                                                    'title': 'keys',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': 'Items',
                                            'type': 'object'
                                        }
                                    },
                                    'type': 'object'
                                },
                                'title': 'Character Shapes',
                                'type': 'array'
                            }
                        },
                        'title': 'Character Data',
                        'type': 'object'
                    },
                    'fFamily': {
                        'description': 'Character Font Family',
                        'title': 'Font Family',
                        'type': 'string'
                    },
                    'size': {
                        'description': 'Character Font Size',
                        'title': 'Font Size',
                        'type': 'string'
                    },
                    'style': {
                        'description': 'Character Font Style',
                        'title': 'Font Style',
                        'type': 'string'
                    },
                    'w': {
                        'description': 'Character Width',
                        'title': 'Width',
                        'type': 'number'
                    }
                },
                'type': 'object'
            },
            'image': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'h': {
                        'description': 'Image Height',
                        'title': 'Height',
                        'type': 'number'
                    },
                    'id': {
                        'description': 'Image ID',
                        'title': 'ID',
                        'type': 'string'
                    },
                    'p': {
                        'description': 'Image name',
                        'title': 'Image name',
                        'type': 'string'
                    },
                    'u': {
                        'description': 'Image path',
                        'title': 'Image path',
                        'type': 'string'
                    },
                    'w': {
                        'description': 'Image Width',
                        'title': 'Width',
                        'type': 'number'
                    }
                },
                'type': 'object'
            },
            'precomp': {
                '$schema': 'http://json-schema.org/draft-04/schema#',
                'properties': {
                    'id': {
                        'description': 'Precomp ID',
                        'title': 'ID',
                        'type': 'string'
                    },
                    'layers': {
                        'description': 'List of Precomp Layers',
                        'items': {
                            'oneOf': [
                                {
                                    '$ref': '#/layers/shape'
                                },
                                {
                                    '$ref': '#/layers/solid'
                                },
                                {
                                    '$ref': '#/layers/comp'
                                },
                                {
                                    '$ref': '#/layers/image'
                                },
                                {
                                    '$ref': '#/layers/null'
                                },
                                {
                                    '$ref': '#/layers/text'
                                }
                            ],
                            'type': 'object'
                        },
                        'title': 'Layers',
                        'type': 'array'
                    }
                },
                'type': 'object'
            }
        }
    }
}

snapshots['test_annotate 1'] = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'properties': {
        'assets': {
            'description': 'source items that can be used in multiple places. Comps and Images for now.',
            'items': [
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'id': {
                            'description': 'Precomp ID',
                            'title': 'ID',
                            'type': 'string'
                        },
                        'layers': {
                            'description': 'List of Precomp Layers',
                            'items': [
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                },
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'ddd': {
                                            'default': 0,
                                            'description': '3d layer flag',
                                            'title': '3d Layer',
                                            'type': 'number'
                                        },
                                        'ind': {
                                            'description': 'Layer index in AE. Used for parenting and expressions.',
                                            'title': 'Index',
                                            'type': 'number'
                                        },
                                        'ip': {
                                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                                            'title': 'In Point',
                                            'type': 'number'
                                        },
                                        'ks': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'a': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'o': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                'p': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                },
                                                'r': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'type': 'number'
                                                        }
                                                    },
                                                    'title': '#/properties/value',
                                                    'type': 'object'
                                                },
                                                's': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                                    'properties': {
                                                        'k': {
                                                            'description': 'Property Value',
                                                            'extended_name': 'Value',
                                                            'items': [
                                                                {
                                                                    'type': 'number'
                                                                },
                                                                {
                                                                    'type': 'number'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/multiDimensional',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/helpers/transform',
                                            'type': 'object'
                                        },
                                        'nm': {
                                            'description': 'After Effects Layer Name. Used for expressions.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'op': {
                                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                                            'title': 'Out Point',
                                            'type': 'number'
                                        },
                                        'st': {
                                            'description': 'Start Time of layer. Sets the start time of the layer.',
                                            'title': 'Start Time',
                                            'type': 'number'
                                        },
                                        'ty': {
                                            'const': 4,
                                            'description': 'Type of layer: Shape.',
                                            'title': 'Type',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/layers/shape',
                                    'type': 'object'
                                }
                            ],
                            'title': 'Layers',
                            'type': 'array'
                        }
                    },
                    'title': '#/sources/precomp',
                    'type': 'object'
                }
            ],
            'title': 'Assets',
            'type': 'array'
        },
        'fr': {
            'description': 'Frame Rate',
            'title': 'Frame Rate',
            'type': 'number'
        },
        'h': {
            'description': 'Composition Height',
            'title': 'Height',
            'type': 'number'
        },
        'ip': {
            'description': 'In Point of the Time Ruler. Sets the initial Frame of the animation.',
            'title': 'In Point',
            'type': 'number'
        },
        'layers': {
            'description': 'List of Composition Layers',
            'items': [
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'refId': {
                            'description': "id pointing to the source composition defined on 'assets' object",
                            'title': 'Reference ID',
                            'type': 'string'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 0,
                            'description': 'Type of layer: Precomp.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/comp',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 3,
                            'description': 'Type of layer: Null.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/null',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 3,
                            'description': 'Type of layer: Null.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/null',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'parent': {
                            'description': 'Layer Parent. Uses ind of parent.',
                            'title': 'Parent',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'hasMask': {
                            'description': 'Boolean when layer has a mask. Will be deprecated in favor of checking masksProperties.',
                            'title': 'Has Masks',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'masksProperties': {
                            'description': 'List of Masks',
                            'items': [
                                {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'inv': {
                                            'default': False,
                                            'description': 'Inverted Mask flag',
                                            'title': 'Inverted',
                                            'type': 'boolean'
                                        },
                                        'mode': {
                                            'default': 'a',
                                            'description': 'Mask mode. Not all mask types are supported.',
                                            'oneOf': [
                                                {
                                                    'const': 'n',
                                                    'standsFor': 'None'
                                                },
                                                {
                                                    'const': 'a',
                                                    'standsFor': 'Additive'
                                                },
                                                {
                                                    'const': 's',
                                                    'standsFor': 'Subtract'
                                                },
                                                {
                                                    'const': 'i',
                                                    'standsFor': 'Intersect'
                                                },
                                                {
                                                    'const': 'l',
                                                    'standsFor': 'Lighten'
                                                },
                                                {
                                                    'const': 'd',
                                                    'standsFor': 'Darken'
                                                },
                                                {
                                                    'const': 'f',
                                                    'standsFor': 'Difference'
                                                }
                                            ],
                                            'title': 'Mode',
                                            'type': 'string'
                                        },
                                        'nm': {
                                            'description': 'Mask name. Used for expressions and effects.',
                                            'title': 'Name',
                                            'type': 'string'
                                        },
                                        'o': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'k': {
                                                    'description': 'Property Value',
                                                    'extended_name': 'Value',
                                                    'type': 'number'
                                                }
                                            },
                                            'title': '#/properties/const',
                                            'type': 'object'
                                        },
                                        'pt': {
                                            '$schema': 'http://json-schema.org/draft-04/schema#',
                                            'properties': {
                                                'k': {
                                                    '$schema': 'http://json-schema.org/draft-04/schema',
                                                    'properties': {
                                                        'i': {
                                                            'description': 'Bezier curve In points. Array of 2 dimensional arrays.',
                                                            'extended_name': 'In Point',
                                                            'items': [
                                                                {
                                                                    'items': {
                                                                        'type': 'number'
                                                                    },
                                                                    'maxItems': 2,
                                                                    'minItems': 2,
                                                                    'type': 'array'
                                                                },
                                                                {
                                                                    'items': {
                                                                        'type': 'number'
                                                                    },
                                                                    'maxItems': 2,
                                                                    'minItems': 2,
                                                                    'type': 'array'
                                                                },
                                                                {
                                                                    'items': {
                                                                        'type': 'number'
                                                                    },
                                                                    'maxItems': 2,
                                                                    'minItems': 2,
                                                                    'type': 'array'
                                                                },
                                                                {
                                                                    'items': {
                                                                        'type': 'number'
                                                                    },
                                                                    'maxItems': 2,
                                                                    'minItems': 2,
                                                                    'type': 'array'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        },
                                                        'o': {
                                                            'description': 'Bezier curve Out points. Array of 2 dimensional arrays.',
                                                            'extended_name': 'Out Point',
                                                            'items': [
                                                                {
                                                                    'items': {
                                                                        'type': 'number'
                                                                    },
                                                                    'maxItems': 2,
                                                                    'minItems': 2,
                                                                    'type': 'array'
                                                                },
                                                                {
                                                                    'items': {
                                                                        'type': 'number'
                                                                    },
                                                                    'maxItems': 2,
                                                                    'minItems': 2,
                                                                    'type': 'array'
                                                                },
                                                                {
                                                                    'items': {
                                                                        'type': 'number'
                                                                    },
                                                                    'maxItems': 2,
                                                                    'minItems': 2,
                                                                    'type': 'array'
                                                                },
                                                                {
                                                                    'items': {
                                                                        'type': 'number'
                                                                    },
                                                                    'maxItems': 2,
                                                                    'minItems': 2,
                                                                    'type': 'array'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        },
                                                        'v': {
                                                            'description': 'Bezier curve Vertices. Array of 2 dimensional arrays.',
                                                            'extended_name': 'Vertices',
                                                            'items': [
                                                                {
                                                                    'items': {
                                                                        'type': 'number'
                                                                    },
                                                                    'maxItems': 2,
                                                                    'minItems': 2,
                                                                    'type': 'array'
                                                                },
                                                                {
                                                                    'items': {
                                                                        'type': 'number'
                                                                    },
                                                                    'maxItems': 2,
                                                                    'minItems': 2,
                                                                    'type': 'array'
                                                                },
                                                                {
                                                                    'items': {
                                                                        'type': 'number'
                                                                    },
                                                                    'maxItems': 2,
                                                                    'minItems': 2,
                                                                    'type': 'array'
                                                                },
                                                                {
                                                                    'items': {
                                                                        'type': 'number'
                                                                    },
                                                                    'maxItems': 2,
                                                                    'minItems': 2,
                                                                    'type': 'array'
                                                                }
                                                            ],
                                                            'type': 'array'
                                                        }
                                                    },
                                                    'title': '#/properties/shapeProp',
                                                    'type': 'object'
                                                }
                                            },
                                            'title': '#/properties/shape',
                                            'type': 'object'
                                        }
                                    },
                                    'title': '#/helpers/mask',
                                    'type': 'object'
                                }
                            ],
                            'title': 'Masks Properties',
                            'type': 'array'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'sc': {
                            'description': 'Color of the solid in hex',
                            'title': 'Solid Color',
                            'type': 'string'
                        },
                        'sh': {
                            'description': 'Height of the solid.',
                            'title': 'Solid Height',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'sw': {
                            'description': 'Width of the solid.',
                            'title': 'Solid Width',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 1,
                            'description': 'Type of layer: Solid.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/solid',
                    'type': 'object'
                },
                {
                    '$schema': 'http://json-schema.org/draft-04/schema#',
                    'properties': {
                        'ddd': {
                            'default': 0,
                            'description': '3d layer flag',
                            'title': '3d Layer',
                            'type': 'number'
                        },
                        'ind': {
                            'description': 'Layer index in AE. Used for parenting and expressions.',
                            'title': 'Index',
                            'type': 'number'
                        },
                        'ip': {
                            'description': 'In Point of layer. Sets the initial frame of the layer.',
                            'title': 'In Point',
                            'type': 'number'
                        },
                        'ks': {
                            '$schema': 'http://json-schema.org/draft-04/schema#',
                            'properties': {
                                'a': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'o': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                'p': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                },
                                'r': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'type': 'number'
                                        }
                                    },
                                    'title': '#/properties/value',
                                    'type': 'object'
                                },
                                's': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'properties': {
                                        'k': {
                                            'description': 'Property Value',
                                            'extended_name': 'Value',
                                            'items': [
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                },
                                                {
                                                    'type': 'number'
                                                }
                                            ],
                                            'type': 'array'
                                        }
                                    },
                                    'title': '#/properties/multiDimensional',
                                    'type': 'object'
                                }
                            },
                            'title': '#/helpers/transform',
                            'type': 'object'
                        },
                        'nm': {
                            'description': 'After Effects Layer Name. Used for expressions.',
                            'title': 'Name',
                            'type': 'string'
                        },
                        'op': {
                            'description': 'Out Point of layer. Sets the final frame of the layer.',
                            'title': 'Out Point',
                            'type': 'number'
                        },
                        'st': {
                            'description': 'Start Time of layer. Sets the start time of the layer.',
                            'title': 'Start Time',
                            'type': 'number'
                        },
                        'ty': {
                            'const': 4,
                            'description': 'Type of layer: Shape.',
                            'title': 'Type',
                            'type': 'number'
                        }
                    },
                    'title': '#/layers/shape',
                    'type': 'object'
                }
            ],
            'title': 'Layers',
            'type': 'array'
        },
        'op': {
            'description': 'Out Point of the Time Ruler. Sets the final Frame of the animation',
            'title': 'Out Point',
            'type': 'number'
        },
        'v': {
            'description': 'Bodymovin Version',
            'title': 'Version',
            'type': 'string'
        },
        'w': {
            'description': 'Composition Width',
            'title': 'Width',
            'type': 'number'
        }
    },
    'type': 'object'
}
