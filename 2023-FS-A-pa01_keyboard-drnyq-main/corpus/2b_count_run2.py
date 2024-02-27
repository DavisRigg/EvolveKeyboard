#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Counts the data, so we don't have to do this repeatedly.
"""
import json
from typing import TypedDict
import itertools


# ../keyboard.py specificies this same structure
LEFT_LAYOUT = "',.PY" "AOEUI" ";QJKX"
RIGHT_LAYOUT = "[]" "FGCRL/=" "DHTNS-" "BMWVZ"
LAYOUT = LEFT_LAYOUT + RIGHT_LAYOUT


class CountDict(TypedDict):
    letter: str
    count: int


def run2_counts(corpus: str, layout: str) -> CountDict:
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
    all_combinations = [comb[0] + comb[1] for comb in itertools.product(layout, layout)]
    char_dict = dict.fromkeys(all_combinations, 0)
    for icharacter in range(len(corpus) - 1):
        cap_char1 = corpus[icharacter].upper()
        cap_char2 = corpus[icharacter + 1].upper()
        if cap_char1 in layout and cap_char2 in layout:
            run_pair = cap_char1 + cap_char2
            char_dict[run_pair] += 1
    return char_dict


with open(file="big_corpus.txt", mode="r", encoding="latin-1") as fhand:
    big_corpus = fhand.read()
count_dict = run2_counts(corpus=big_corpus, layout=LAYOUT)
with open("counts_run2.json", mode="w") as foutput:
    json.dump(obj=count_dict, fp=foutput)
