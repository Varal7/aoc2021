import re
from collections import *
from functools import *
from itertools import *
import numpy as np
import pyperclip
import sys
sys.setrecursionlimit(1000)

def cprint(t):
    print(t)
    pyperclip.copy(t)


def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def part1():
        tab = []
        for line in lines:
            line = line.strip()
            tab.append([int(t) for t in line])
        risk = 0

        n = len(tab)
        m = len(tab[0])


        def is_low(i, j):
            for di, dj in dirs:
                if i+di >=0 and i+di < n and j+dj >= 0 and j+dj < m:
                    if tab[i+di][j+dj] <= tab[i][j]:
                        return False

            return True

        for i in range(n):
            for j in range(m):
                if is_low(i, j):
                    risk += tab[i][j] + 1

        return risk


    def part2():
        tab = []
        for line in lines:
            line = line.strip()
            tab.append([int(t) for t in line])

        n = len(tab)
        m = len(tab[0])

        t = dict()

        for i in range(n):
            for j in range(m):
                t[(i,j)] = tab[i][j]


        colors = dict()
        roots = []
        groups = defaultdict(set)
        visited = set()

        def is_low(i, j):
            for di, dj in dirs:
                if i+di >=0 and i+di < n and j+dj >= 0 and j+dj < m:
                    if tab[i+di][j+dj] <= tab[i][j]:
                        return False

            return True

        for i in range(n):
            for j in range(m):
                if is_low(i, j):
                    roots.append((i, j))
                    groups[(i,j)].add((i,j))

        def get_color(node):
            if node in roots:
                return node

            if node in colors:
                return colors[node]

            i, j = node

            for di, dj in dirs:
                nei = i+di, j+dj
                if i+di >=0 and i+di < n and j+dj >= 0 and j+dj < m:
                    if t[nei] < t[node]:
                        c = get_color(nei)
                        colors[node] = c
                        groups[c].add(node)
                        break

            return colors[node]

        for i in range(n):
            for j in range(m):
                if t[i,j] != 9:
                    get_color((i, j))

        for k, v in groups.items():
            print(k, len(v))
            print(sorted(v))
            print()

        ans = 1
        for v in sorted([len(x) for x in groups.values()])[-3:]:
            #  print(v)
            ans *= v


        return ans

    cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
