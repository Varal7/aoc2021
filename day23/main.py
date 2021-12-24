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

    HALLWAY = 1
    LOWER = 3
    UPPER = 2

    hallways = [1,2,4,6,8,10,11]
    base = {"A": 3, "B": 5, "C": 7, "D": 9}
    energy = {"A": 1, "B": 10, "C": 100, "D": 1000}

    i2k = "ABCDE"
    k2i = {o: i for (i,o) in enumerate(i2k)}

    final = ("AA", "BB", "CC", "DD", "E" * 12)

    def is_base_clean(state, k):
        return all(c in ["E", k] for c in state[k2i[k]])

    def hallway_clear(state, j1, j2):
        if state[-1][j2] != "E":
            return False
        j1, j2 = min(j1, j2), max(j1, j2)
        for j in range(j1 + 1, j2):
            if state[-1][j] != "E":
                return False
        return True

    def move(state, j, k, new_col, moving):
        sh = state[-1]
        s = []
        sh = "".join(c if jj != j else moving for (jj, c) in enumerate(sh))
        for i, sk in enumerate(state[:-1]):
            if i != k2i[k]:
                s.append(sk)
            else:
                s.append(new_col)
        s.append(sh)
        return tuple(s)


    @lru_cache
    def get_cost(state):
        sh = state[-1]

        if state == final:
            return 0

        candidates = []

        # can we move from hallway?
        for (j, k) in enumerate(sh):
            if k != "E":
                base_col = state[k2i[k]]
                if not is_base_clean(state, k):
                    continue
                n = len(base_col)
                i = base_col.index(k) if k in base_col else n
                new_col = "E" * (i - 1) + k * (n - i + 1)
                if hallway_clear(state, j, base[k]):
                    new_state = move(state, j, k, new_col, "E")
                    cost = (abs(j - base[k]) + i) * energy[k]
                    if (c := get_cost(new_state)) is not None:
                        return cost + c

        # move to hallway
        for k in "ABCD":
            sk = state[k2i[k]]
            if not is_base_clean(state, k):
                for (i, moving) in enumerate(sk):
                    if moving == "E":
                        continue
                    for j in hallways:
                        if hallway_clear(state, base[k], j):
                            new_state = move(state, j, k, sk[:i] + "E" + sk[i+1:], moving)
                            cost = (abs(j - base[k]) + (i+1)) * energy[moving]
                            if (c := get_cost(new_state)) is not None:
                                candidates.append(cost + c)

                    break

        if len(candidates) == 0:
            return None
        return min(candidates)

    def part1():
        with open(filename) as f:
            lines = f.readlines()
        lines = [line.rstrip().replace(".", "E") for line in lines]
        sh = "E" + lines[HALLWAY][1:-1]
        sa = lines[UPPER][base["A"]] + lines[LOWER][base["A"]]
        sb = lines[UPPER][base["B"]] + lines[LOWER][base["B"]]
        sc = lines[UPPER][base["C"]] + lines[LOWER][base["C"]]
        sd = lines[UPPER][base["D"]] + lines[LOWER][base["D"]]
        init_state = (sa, sb, sc, sd, sh)
        print(init_state)
        return get_cost(init_state)

    def part2():
        nonlocal final
        with open(filename) as f:
            lines = f.readlines()
        lines = [line.rstrip().replace(".", "E") for line in lines]
        extra_one = "  #D#C#B#A#"
        extra_two = "  #D#B#A#C#"
        lines = lines[:3] + [extra_one, extra_two] + lines[3:]

        sh = "E" + lines[HALLWAY][1:-1]
        ss = []
        for k in "ABCD":
            ss.append("".join(lines[i][base[k]] for i in range(2, 2 + 4)))
        init_state = tuple(ss + [sh])
        print(init_state)
        final = ("AAAA", "BBBB", "CCCC", "DDDD", "E" * 12)
        return get_cost(init_state)

    #  cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
