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


        colors = defaultdict(lambda: None)
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
                    colors[(i,j)] = (i, j)
                    groups[(i,j)].add((i, j))
                    visited.add((i,j))

        def flows_unique(node):
            i,j = node
            out = None
            c = set()
            for di, dj in dirs:
                if i+di >=0 and i+di < n and j+dj >= 0 and j+dj < m:
                    if tab[i+di][j+dj] <= tab[i][j]:
                        out = (i+di, j+dj)
                        c.add(colors[out])
            if len(c) != 1:
                return None
            return list(c)[0]


        for root in roots:
            for level in range(t[root], 10):
                cur = [x for x in groups[root] if tab[x[0]][x[1]] == level]

                for i, j in cur:
                    for di, dj in dirs:
                        if i+di >=0 and i+di < n and j+dj >= 0 and j+dj < m:
                            nei = i+di, j+dj
                            if t[nei] == 9:
                                continue
                            #  import pdb; pdb.set_trace()
                            c = flows_unique(nei)
                            if c == root:
                                colors[nei] = root
                                groups[root].add(nei)


        #  for k, v in groups.items():
            #  print(k, len(v))
            #  print(sorted(v))
            #  print()

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
