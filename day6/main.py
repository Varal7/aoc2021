import re
from collections import *
from functools import *
from itertools import *
import numpy as np
import pyperclip


def cprint(t):
    print(t)
    pyperclip.copy(t)


def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    def part1():
        for line in lines:
            line = line.strip()
        nums = list(map( int, lines[0].split(",")))

        def process(t):
            added = 0
            for i in range(len(t)):
                if t[i] == 0:
                    t[i] = 6
                    added += 1
                else:
                    t[i] -= 1
            return t + [8] * added

        for i in range(80):
            nums = process(nums)

        return len(nums)

    def part2():

        @lru_cache
        def becoming(n, val):
            if n == 0:
                return 1
            if val == 0:
                return becoming(n-1, 8) + becoming(n-1, 6)
            return becoming(n-1, val-1)

        for line in lines:
            line = line.strip()
        nums = list(map( int, lines[0].split(",")))
        c = Counter(nums)

        count = 0
        for k in c:
            count += becoming(256, k) * c[k]

        return count


    #  cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
