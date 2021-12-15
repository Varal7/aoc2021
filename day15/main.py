import re
from collections import *
from functools import *
from itertools import *
import numpy as np
import pyperclip

from heapq import heapify, heappop, heappush

def cprint(t):
    print(t)
    pyperclip.copy(t)


def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    def part1():
        tab = []
        for line in lines:
            line = line.strip()
            tab.append(list(map(int, line)))

        n = len(tab)
        m = len(tab[0])

        Q = [(tab[n-1][m-1], n-1, m-1)]
        heapify(Q)

        rr = [0, 1, 0, -1]
        cc = [1, 0, -1, 0]

        visited = set((n-1,m-1))

        while len(Q) > 0:
            val, i, j = heappop(Q)
            if (i, j) == (0, 0):
                return val - tab[0][0]
            for r, c in zip(rr, cc):
                ii = i + r
                jj = j + c
                if 0<=ii<n and 0<=jj<m:
                    if (ii, jj) not in visited:
                        heappush(Q, (val+tab[ii][jj], ii, jj))
                        visited.add((ii, jj))

        return 0


    def part2():
        tab = []
        for line in lines:
            line = line.strip()
            tab.append(list(map(int, line)))

        nn = len(tab)
        mm = len(tab[0])

        n = 5 * nn
        m = 5 * mm


        def get(i, j):
            i_tile = i // nn
            j_tile = j // mm
            c = (tab[i%nn][j%mm] + i_tile + j_tile) % 9
            if c == 0:
                return 9
            return c



        for i in range(n):
            for j in range(m):
                print(get(i, j), end="")
            print()

        Q = [(get(n-1, m-1), n-1, m-1)]
        heapify(Q)

        rr = [0, 1, 0, -1]
        cc = [1, 0, -1, 0]

        visited = set((n-1,m-1))

        while len(Q) > 0:
            val, i, j = heappop(Q)
            if (i, j) == (0, 0):
                return val - get(0, 0)
            for r, c in zip(rr, cc):
                ii = i + r
                jj = j + c
                if 0<=ii<n and 0<=jj<m:
                    if (ii, jj) not in visited:
                        heappush(Q, (val+get(ii, jj), ii, jj))
                        visited.add((ii, jj))

        return 0



    cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
