import re
from collections import *
from functools import *
from itertools import *
from math import *
import pyperclip
import numpy as np
from sympy import symbols, Eq, Piecewise, Integer, simplify
import sys
from tqdm import tqdm

from heapq import heapify, heappop, heappush

def cprint(t):
    print(t)
    pyperclip.copy(t)

def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    def part1():
        inp_lines = [i for (i, line) in enumerate(lines) if line.startswith("inp")]

        @lru_cache
        def f(w, x, y, z, lineno):
            if lineno == len(lines):
                return {"w": w, "x": x, "y": y, "z": z, "lineno": None }
            if lineno in inp_lines:
                return {"w": w, "x": x, "y": y, "z": z, "lineno": lineno }

            var = {"w": w, "x": x, "y": y, "z": z}

            line = lines[lineno].strip()
            op, a, b = line.split()
            if b in "wxyz":
                b = var[b]
            else:
                b = int(b)

            if op == "add":
                var[a] = var[a] + b
            if op == "mul":
                var[a] = var[a] * b
            if op == "div":
                var[a] = int(var[a] / b)
            if op == "mod":
                var[a] = var[a] % b
            if op == "eql":
                var[a] = 1 if var[a] == b else 0

            var["lineno"] = lineno + 1

            return f(**var)

        @lru_cache
        def g(w, x, y, z, lineno, inp):
            var = {"w": w, "x": x, "y": y, "z": z, "lineno": lineno}
            var[lines[lineno].split()[1]] = int(inp[0])
            var["lineno"] += 1
            new_var = f(**var)
            if new_var["lineno"] is None:
                return new_var
            new_var["inp"] = inp[1:]
            return g(**new_var)

        def compute(inp):
            return g(0, 0, 0, 0, 0, inp)["z"]

        fg = product(*repeat("987654321", 14))
        for inp in tqdm(fg):
            inp = "".join(inp)
            if compute(inp) == 0:
                return inp


    cprint(part1())
    #  cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
