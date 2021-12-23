import re
from collections import *
from functools import *
from itertools import *
from math import *
import pyperclip
import numpy as np
import sys

from heapq import heapify, heappop, heappush

def cprint(t):
    print(t)
    pyperclip.copy(t)

def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    key = list(lines[0].strip())

    assert bool(key[0] == ".") ^ bool(key[-1] == ".")
    alternates = key[0] == "#"

    def part1():
        num_steps = 2
        n = len(lines[2:])
        m = len(lines[2])
        cur = set()
        for i, line in enumerate(lines[2:]):
            for j, c in enumerate(line.strip()):
                if c == "#":
                    cur.add((i,j))

        rev = False

        def get_cur(i,j):
            def g():
                if i < 1 or j < 1 or i > n or j > m:
                    return 0
                return 1 if (i-1, j-1) in cur else 0
            return 1 - g() if rev else g()

        for _ in range(num_steps):
            nei = set()
            for i in range(n+2):
                for j in range(n+2):
                    s = ""
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            ii = i + di
                            jj = j + dj
                            s += str(get_cur(ii, jj))
                    val = int(s, 2)
                    switch = alternates and not rev
                    if bool(key[val] == "#") ^ switch:
                        nei.add((i,j))

            cur = nei
            n += 2
            m += 2
            if alternates:
                rev = not rev

        return len(cur)


    def part2():
        num_steps = 50
        n = len(lines[2:])
        m = len(lines[2])
        cur = set()
        for i, line in enumerate(lines[2:]):
            for j, c in enumerate(line.strip()):
                if c == "#":
                    cur.add((i,j))

        rev = False

        def get_cur(i,j):
            def g():
                if i < 1 or j < 1 or i > n or j > m:
                    return 0
                return 1 if (i-1, j-1) in cur else 0
            return 1 - g() if rev else g()

        for _ in range(num_steps):
            nei = set()
            for i in range(n+2):
                for j in range(n+2):
                    s = ""
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            ii = i + di
                            jj = j + dj
                            s += str(get_cur(ii, jj))
                    val = int(s, 2)
                    switch = alternates and not rev
                    if bool(key[val] == "#") ^ switch:
                        nei.add((i,j))

            cur = nei
            n += 2
            m += 2
            if alternates:
                rev = not rev

        return len(cur)





    cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
