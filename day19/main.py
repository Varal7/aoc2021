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
    col_pos = [
            lambda x,y,z: (x,y,z),
            lambda x,y,z: (y,z,x),
            lambda x,y,z: (z,x,y),
    ]
    col_neg = [
            lambda x,y,z: (x,z,y),
            lambda x,y,z: (y,x,z),
            lambda x,y,z: (z,y,x),
    ]
    sym_pos = [
            lambda x,y,z: (x,y,z),
            lambda x,y,z: (-x,-y,z),
            lambda x,y,z: (x,-y,-z),
            lambda x,y,z: (-x,y,-z),
    ]
    sym_neg = [
            lambda x,y,z: (-x,y,z),
            lambda x,y,z: (x,-y,z),
            lambda x,y,z: (x,y,-z),
            lambda x,y,z: (-x,-y,-z),
    ]
    fg = list(chain(product(sym_pos, col_pos), product(sym_neg, col_neg)))

    def op(tr, grid):
        f, g = tr
        return [f(*(g(*line))) for line in grid]

    def transpose(delta, grid):
        dx, dy, dz = delta
        return [(lambda x, y, z: (x+dx, y+dy, z+dz))(*line) for line in grid]

    def minus(m1, m2):
        x,y,z = m1
        xx,yy,zz = m2
        return x-xx, y-yy, z-zz


    def part1():
        scanners = []

        with open(filename) as f:
            lines = f.readlines()

        scanner = []
        for line in lines + ["\n"]:
            if line.startswith("---"):
                continue
            if line == "\n":
                scanners.append(scanner)
                scanner = []
            else:
                scanner.append(tuple(map(int ,line.strip().split(","))))

        visited = set()
        queue = [0]


        while len(queue) > 0:
            i = queue.pop()
            og = scanners[i]
            visited.add(i)


            for j, scanner in enumerate(scanners):
                if j not in visited:
                    for tr in fg:
                        tred = op(tr, scanner)
                        deltas = Counter()
                        for v1 in og:
                            for v2 in tred:
                                deltas[ minus(v1, v2) ] += 1

                        delta, freq = deltas.most_common(1)[0]
                        if freq >= 12:
                            visited.add(j)
                            scanners[j] = transpose(delta, tred)
                            queue.append(j)
                            break

        points = set([line for scanner in scanners for line in scanner])

        return len(points)

    def part2():
        scanners = []

        with open(filename) as f:
            lines = f.readlines()

        scanner = []
        for line in lines + ["\n"]:
            if line.startswith("---"):
                continue
            if line == "\n":
                scanners.append(scanner)
                scanner = []
            else:
                scanner.append(tuple(map(int ,line.strip().split(","))))

        n = len(scanners)

        visited = set()
        queue = [0]

        delta_to_orig = {0 : (0,0,0)}

        while len(queue) > 0:
            i = queue.pop()
            og = scanners[i]
            visited.add(i)

            for j, scanner in enumerate(scanners):
                if j not in visited:
                    for tr in fg:
                        tred = op(tr, scanner)
                        deltas = Counter()
                        for v1 in og:
                            for v2 in tred:
                                deltas[ minus(v1, v2) ] += 1

                        delta, freq = deltas.most_common(1)[0]
                        if freq >= 12:
                            delta_to_orig[j] = delta
                            visited.add(j)
                            scanners[j] = transpose(delta, tred)
                            queue.append(j)
                            break


        maxi = None

        for i in range(n):
            for j in range(n):
                dx, dy, dz = minus(delta_to_orig[i], delta_to_orig[j])
                dist = abs(dx) + abs(dy) + abs(dz)
                if maxi is None or dist > maxi:
                    maxi = dist

        return maxi

    cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
