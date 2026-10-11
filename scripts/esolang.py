#!/usr/bin/env python3
"""Minimal interpreters used by CI for small esoteric languages.

Usage: python3 scripts/esolang.py {bf,ook,cow,befunge,hq9,unlambda,whitespace} FILE
"""
import random
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
    return "".join(COW[w] for w in re.findall(r"[mM][oO][oO]", src) if w in COW)


def brainfuck(code):
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


def befunge(src, max_steps=1000000):
    grid = [list(line.ljust(80)) for line in src.split("\n")[:25]]
    grid += [[" "] * 80 for _ in range(25 - len(grid))]
    x = y = 0
    dx, dy = 1, 0
    stack, out, string_mode = [], [], False
    pop = lambda: stack.pop() if stack else 0
    for _ in range(max_steps):
        c = grid[y][x]
        if string_mode:
            if c == '"':
                string_mode = False
            else:
                stack.append(ord(c))
        elif c.isdigit():
            stack.append(int(c))
        elif c in "+-*/%`":
            b, a = pop(), pop()
            stack.append({"+": a + b, "-": a - b, "*": a * b, "/": a // b if b else 0,
                          "%": a % b if b else 0, "`": int(a > b)}[c])
        elif c == "!":
            stack.append(int(not pop()))
        elif c in "><^v?":
            if c == "?":
                c = random.choice("><^v")
            dx, dy = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}[c]
        elif c == "_":
            dx, dy = (-1, 0) if pop() else (1, 0)
        elif c == "|":
            dx, dy = (0, -1) if pop() else (0, 1)
        elif c == '"':
            string_mode = True
        elif c == ":":
            v = pop()
            stack += [v, v]
        elif c == "\\":
            b, a = pop(), pop()
            stack += [b, a]
        elif c == "$":
            pop()
        elif c == ".":
            out.append("%d " % pop())
        elif c == ",":
            out.append(chr(pop()))
        elif c == "#":
            x, y = (x + dx) % 80, (y + dy) % 25
        elif c == "g":
            gy, gx = pop(), pop()
            stack.append(ord(grid[gy][gx]))
        elif c == "p":
            py, px, v = pop(), pop(), pop()
            grid[py][px] = chr(v)
        elif c == "@":
            break
        x, y = (x + dx) % 80, (y + dy) % 25
    return "".join(out)


def hq9(src):
    out, acc = [], 0
    for c in src:
        if c == "H":
            out.append("Hello, world!\n")
        elif c == "Q":
            out.append(src)
        elif c == "9":
            out.append("99 bottles of beer on the wall\n")
        elif c == "+":
            acc += 1
    return "".join(out)


def unlambda(src):
    """Unlambda without the continuation (c) and delay (d) builtins."""
    src = re.sub(r"#.*", "", src)
    pos = 0
    out = []

    def parse():
        nonlocal pos
        while src[pos].isspace():
            pos += 1
        c = src[pos]
        pos += 1
        if c == "`":
            return ("app", parse(), parse())
        if c == ".":
            ch = src[pos]
            pos += 1
            return ("print", ch)
        return {"i": ("i",), "k": ("k",), "s": ("s",), "v": ("v",), "r": ("print", "\n")}[c]

    def apply(f, x):
        tag = f[0]
        if tag == "i":
            return x
        if tag == "v":
            return f
        if tag == "print":
            out.append(f[1])
            return x
        if tag == "k":
            return ("k1", x)
        if tag == "k1":
            return f[1]
        if tag == "s":
            return ("s1", x)
        if tag == "s1":
            return ("s2", f[1], x)
        if tag == "s2":
            return apply(apply(f[1], x), apply(f[2], x))
        raise ValueError(tag)

    def evaluate(node):
        if node[0] == "app":
            return apply(evaluate(node[1]), evaluate(node[2]))
        return node

    evaluate(parse())
    return "".join(out)


def whitespace(src):
    code = [c for c in src if c in " \t\n"]
    pos = 0

    def take(n):
        nonlocal pos
        s = "".join(code[pos:pos + n])
        pos += n
        return s

    def number():
        nonlocal pos
        sign = -1 if take(1) == "\t" else 1
        bits = ""
        while code[pos] != "\n":
            bits += "1" if take(1) == "\t" else "0"
        pos += 1
        return sign * int(bits or "0", 2)

    def label():
        nonlocal pos
        s = ""
        while code[pos] != "\n":
            s += take(1)
        pos += 1
        return s

    instrs, labels = [], {}
    S, T, L = " ", "\t", "\n"
    while pos < len(code):
        imp = take(1)
        if imp == S:
            op = take(1)
            if op == S:
                instrs.append(("push", number()))
            else:
                op += take(1)
                if op in (T + S, T + L):
                    instrs.append(({T + S: "copy", T + L: "slide"}[op], number()))
                else:
                    instrs.append(({L + S: "dup", L + T: "swap", L + L: "drop"}[op], None))
        elif imp == T:
            sub = take(1)
            op = take(2) if sub != L else ""
            if sub == S:
                instrs.append(({S + S: "add", S + T: "sub", S + L: "mul", T + S: "div", T + T: "mod"}[op], None))
            elif sub == T:
                instrs.append(({S: "store", T: "retrieve"}[op[0]], None))
                pos -= 1
            else:
                op = take(2)
                instrs.append(({S + S: "outc", S + T: "outn", T + S: "readc", T + T: "readn"}[op], None))
        else:
            op = take(2)
            if op == L + L:
                instrs.append(("end", None))
            elif op == T + L:
                instrs.append(("ret", None))
            else:
                name = {S + S: "mark", S + T: "call", S + L: "jump", T + S: "jz", T + T: "jn"}[op]
                lab = label()
                if name == "mark":
                    labels[lab] = len(instrs)
                else:
                    instrs.append((name, lab))

    stack, heap, calls, out, pc = [], {}, [], [], 0
    while pc < len(instrs):
        op, arg = instrs[pc]
        pc += 1
        if op == "push":
            stack.append(arg)
        elif op == "dup":
            stack.append(stack[-1])
        elif op == "copy":
            stack.append(stack[-1 - arg])
        elif op == "swap":
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif op == "drop":
            stack.pop()
        elif op == "slide":
            top = stack.pop()
            del stack[len(stack) - arg:]
            stack.append(top)
        elif op in ("add", "sub", "mul", "div", "mod"):
            b, a = stack.pop(), stack.pop()
            stack.append({"add": a + b, "sub": a - b, "mul": a * b, "div": a // b, "mod": a % b}[op])
        elif op == "store":
            v, a = stack.pop(), stack.pop()
            heap[a] = v
        elif op == "retrieve":
            stack.append(heap.get(stack.pop(), 0))
        elif op == "outc":
            out.append(chr(stack.pop()))
        elif op == "outn":
            out.append(str(stack.pop()))
        elif op in ("readc", "readn"):
            heap[stack.pop()] = 0
        elif op == "call":
            calls.append(pc)
            pc = labels[arg]
        elif op == "jump":
            pc = labels[arg]
        elif op == "jz":
            if stack.pop() == 0:
                pc = labels[arg]
        elif op == "jn":
            if stack.pop() < 0:
                pc = labels[arg]
        elif op == "ret":
            pc = calls.pop()
        elif op == "end":
            break
    return "".join(out)


def main():
    lang, path = sys.argv[1], sys.argv[2]
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    if lang in ("bf", "ook", "cow"):
        result = brainfuck(to_bf(lang, src))
    else:
        result = {"befunge": befunge, "hq9": hq9, "unlambda": unlambda, "whitespace": whitespace}[lang](src)
    print(result)


if __name__ == "__main__":
    main()
