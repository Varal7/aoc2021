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
        def f(inp):
            var = {"w": 0, "x": 0, "y": 0, "z": 0}

            i = 0
            for idx, line in enumerate(lines):
                line = line.strip()
                if line.startswith("inp"):
                    var[line.split()[1]] = int(inp[i])
                    i += 1
                    continue
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

            return var

        return f("99394899891971")['z']


    def part2():
        def f(inp):
            var = {"w": 0, "x": 0, "y": 0, "z": 0}

            i = 0
            for idx, line in enumerate(lines):
                line = line.strip()
                if line.startswith("inp"):
                    var[line.split()[1]] = int(inp[i])
                    i += 1
                    continue
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

            return var

        return f("92171126131911")['z']


    cprint(part1())
    cprint(part2())

print("Test")
#  main("test.txt")
print("Real")
main("input.txt")
