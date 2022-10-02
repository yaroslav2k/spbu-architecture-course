# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = "3.10"

_lr_method = "LALR"

_lr_signature = "leftPIPEleftIDENTIFIERASSIGNMENT DOUBLE_QUOTES_ENCLOSED_IDENTIFIER IDENTIFIER PIPE SINGLE_QUOTES_ENCLOSED_IDENTIFIERpipeline : expression\n                    | pipeline pipe expressionexpression : identifier\n                      | expression identifier\n                      | assignmentassignment : ASSIGNMENTidentifier : IDENTIFIER\n                      | SINGLE_QUOTES_ENCLOSED_IDENTIFIER\n                      | DOUBLE_QUOTES_ENCLOSED_IDENTIFIERpipe : PIPE"

_lr_action_items = {
    "IDENTIFIER": (
        [
            0,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
        ],
        [
            5,
            5,
            -3,
            -5,
            -7,
            -8,
            -9,
            -6,
            5,
            -10,
            -4,
            5,
        ],
    ),
    "SINGLE_QUOTES_ENCLOSED_IDENTIFIER": (
        [
            0,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
        ],
        [
            6,
            6,
            -3,
            -5,
            -7,
            -8,
            -9,
            -6,
            6,
            -10,
            -4,
            6,
        ],
    ),
    "DOUBLE_QUOTES_ENCLOSED_IDENTIFIER": (
        [
            0,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
        ],
        [
            7,
            7,
            -3,
            -5,
            -7,
            -8,
            -9,
            -6,
            7,
            -10,
            -4,
            7,
        ],
    ),
    "ASSIGNMENT": (
        [
            0,
            9,
            10,
        ],
        [
            8,
            8,
            -10,
        ],
    ),
    "$end": (
        [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            11,
            12,
        ],
        [
            0,
            -1,
            -3,
            -5,
            -7,
            -8,
            -9,
            -6,
            -4,
            -2,
        ],
    ),
    "PIPE": (
        [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            11,
            12,
        ],
        [
            10,
            -1,
            -3,
            -5,
            -7,
            -8,
            -9,
            -6,
            -4,
            -2,
        ],
    ),
}

_lr_action = {}
for _k, _v in _lr_action_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_action:
            _lr_action[_x] = {}
        _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {
    "pipeline": (
        [
            0,
        ],
        [
            1,
        ],
    ),
    "expression": (
        [
            0,
            9,
        ],
        [
            2,
            12,
        ],
    ),
    "identifier": (
        [
            0,
            2,
            9,
            12,
        ],
        [
            3,
            11,
            3,
            11,
        ],
    ),
    "assignment": (
        [
            0,
            9,
        ],
        [
            4,
            4,
        ],
    ),
    "pipe": (
        [
            1,
        ],
        [
            9,
        ],
    ),
}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_goto:
            _lr_goto[_x] = {}
        _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
    ("S' -> pipeline", "S'", 1, None, None, None),
    ("pipeline -> expression", "pipeline", 1, "p_pipeline", "semantic_parser.py", 22),
    (
        "pipeline -> pipeline pipe expression",
        "pipeline",
        3,
        "p_pipeline",
        "semantic_parser.py",
        23,
    ),
    (
        "expression -> identifier",
        "expression",
        1,
        "p_expression",
        "semantic_parser.py",
        33,
    ),
    (
        "expression -> expression identifier",
        "expression",
        2,
        "p_expression",
        "semantic_parser.py",
        34,
    ),
    (
        "expression -> assignment",
        "expression",
        1,
        "p_expression",
        "semantic_parser.py",
        35,
    ),
    (
        "assignment -> ASSIGNMENT",
        "assignment",
        1,
        "p_assignment",
        "semantic_parser.py",
        44,
    ),
    (
        "identifier -> IDENTIFIER",
        "identifier",
        1,
        "p_identifier",
        "semantic_parser.py",
        50,
    ),
    (
        "identifier -> SINGLE_QUOTES_ENCLOSED_IDENTIFIER",
        "identifier",
        1,
        "p_identifier",
        "semantic_parser.py",
        51,
    ),
    (
        "identifier -> DOUBLE_QUOTES_ENCLOSED_IDENTIFIER",
        "identifier",
        1,
        "p_identifier",
        "semantic_parser.py",
        52,
    ),
    ("pipe -> PIPE", "pipe", 1, "p_pipe", "semantic_parser.py", 58),
]
