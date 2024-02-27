#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Counts the data, so we don't have to do this repeatedly.
"""
import json
from typing import TypedDict


# ../keyboard.py specificies this same structure
LEFT_LAYOUT = "',.PY" "AOEUI" ";QJKX"
RIGHT_LAYOUT = "[]" "FGCRL/=" "DHTNS-" "BMWVZ"
LAYOUT = LEFT_LAYOUT + RIGHT_LAYOUT


class CountDict(TypedDict):
    letter: str
    count: int


def letter_count_sans_repeat(corpus: str, layout: str) -> CountDict:
    """
    Counts letter-frequency in corpus.

    Repeats are "stay" characters,
    rather than "return to home row characters,
    thus they incur home-like minimum cost.
    So, we don't count any run of repeats.

    In this EC, some symbols are movable.
    Unlike letters, symbols can't be capitalized.
    To count all symbols, we effectively reverse "capitalize" them.
    So, we replace all movable symbols with their "lower-case" counterpart.
    """
    corpus = corpus.replace('"', "'")
    corpus = corpus.replace("<", ".")
    corpus = corpus.replace(">", ".")
    corpus = corpus.replace("{", "[")
    corpus = corpus.replace("}", "]")
    corpus = corpus.replace("?", "/")
    corpus = corpus.replace("+", "=")
    corpus = corpus.replace("_", "-")
    corpus = corpus.replace(":", ";")
    char_dict = dict.fromkeys(layout, 0)
    last_char = ""
    for character in corpus:
        cap_char = character.upper()
        if cap_char in layout:
            if cap_char != last_char:
                char_dict[cap_char] += 1
                last_char = cap_char
    return char_dict


with open(file="big_corpus.txt", mode="r", encoding="latin-1") as fhand:
    big_corpus = fhand.read()
count_dict = letter_count_sans_repeat(corpus=big_corpus, layout=LAYOUT)
with open("counts.json", mode="w") as foutput:
    json.dump(obj=count_dict, fp=foutput)
