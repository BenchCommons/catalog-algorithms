#!/usr/bin/env python3
"""Minimal interpreters used by CI for Brainfuck-family esoteric languages.

Usage: python3 scripts/esolang.py {bf,ook,cow} FILE
"""
import re
import sys

OOK = {("Ook.", "Ook?"): ">", ("Ook?", "Ook."): "<", ("Ook.", "Ook."): "+", ("Ook!", "Ook!"): "-",
       ("Ook!", "Ook."): ".", ("Ook.", "Ook!"): ",", ("Ook!", "Ook?"): "[", ("Ook?", "Ook!"): "]"}
COW = {"moO": ">", "mOo": "<", "MoO": "+", "MOo": "-", "Moo": ".", "MOO": "[", "moo": "]"}


def to_bf(lang, src):
    if lang == "bf":
        return "".join(c for c in src if c in "<>+-.,[]")
    if lang == "ook":
        words = re.findall(r"Ook[.?!]", src)
        return "".join(OOK[(words[i], words[i + 1])] for i in range(0, len(words) - 1, 2))
    if lang == "cow":
        return "".join(COW[w] for w in re.findall(r"[mM][oO][oO]", src) if w in COW)
    raise SystemExit("unknown language: " + lang)


def run(code):
    jumps, stack = {}, []
    for i, c in enumerate(code):
        if c == "[":
            stack.append(i)
        elif c == "]":
            j = stack.pop()
            jumps[i], jumps[j] = j, i
    tape, ptr, pc, out = [0] * 30000, 0, 0, []
    while pc < len(code):
        c = code[pc]
        if c == ">":
            ptr += 1
        elif c == "<":
            ptr -= 1
        elif c == "+":
            tape[ptr] = (tape[ptr] + 1) % 256
        elif c == "-":
            tape[ptr] = (tape[ptr] - 1) % 256
        elif c == ".":
            out.append(chr(tape[ptr]))
        elif c == "[" and tape[ptr] == 0:
            pc = jumps[pc]
        elif c == "]" and tape[ptr] != 0:
            pc = jumps[pc]
        pc += 1
    return "".join(out)


if __name__ == "__main__":
    lang, path = sys.argv[1], sys.argv[2]
    with open(path, encoding="utf-8") as fh:
        print(run(to_bf(lang, fh.read())))
