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

    LOWER = 3
    UPPER = 2

    hallways = [ (1,1), (1,2), (1,4), (1,6), (1,8), (1,10), (1,11), ]

    def leq(li1, li2):
        if len(li1) != len(li2):
            return False
        for el in li1:
            if el not in li2:
                return False
        return True

    class Node:
        def __init__(self, A, B, C, D):
            self.A = sorted(A)
            self.B = sorted(B)
            self.C = sorted(C)
            self.D = sorted(D)

            self.dict = {
                "A": self.A,
                "B": self.B,
                "C": self.C,
                "D": self.D,
            }

            self.pos2k = dict()

            for k in "ABCD":
                for pos in self.dict[k]:
                    self.pos2k[pos] = k


        def to_tuple(self):
            return tuple(el for li in self.dict.values() for el in li)

        def __lt__(self, other):
            return self.to_tuple() < other.to_tuple()

        def __eq__(self, other):
            return self.to_tuple() == other.to_tuple()

        def __hash__(self):
            return self.to_tuple().__hash__()

        @classmethod
        def from_lines(cls, lines):
            d = defaultdict(list)
            for i in [1,2,3]:
                for j, c in enumerate(lines[i]):
                    if c in "ABCD":
                        d[c].append((i,j))
            return cls(**d)

        def points(self):
            points = dict()
            for k in "ABCD":
                for i in [0,1]:
                    points[f"{k}{i}"] =  self.dict[k][i]

            return points

        def __str__(self):
            grid = [["." for _ in range(13)] for _ in range(5)]
            for k in "ABCD":
                for pos in self.dict[k]:
                    x, y = pos
                    grid[x][y] = k
            return "\n".join(["".join(line) for line in grid])

        def heuristic(self):
            cost = 0
            for k in "ABCD":
                for i in [0, 1]:
                    s = self.dict[k][i]
                    if s[1] != self.base(k):
                        cost += self.cost(s, (UPPER, self.base(k)), k)
            return cost

        def base(self, k):
            return {"A": 3, "B": 5, "C": 7, "D": 9}[k]

        def energy(self, k):
            return {"A": 1, "B": 10, "C": 100, "D": 1000}[k]

        def is_base_clean(self, k):
            j = self.base(k)
            for i in [LOWER, UPPER]:
                if (i, j) in self.pos2k and self.pos2k[(i,j)] != k:
                    return False
            return True

        def cost(self, s, t, k):
            return self.energy(k) * (abs(s[0] - t[0]) + abs(s[1] - t[1]))

        def move(self, s, t):
            k = self.pos2k[s]
            d = {k: v for (k, v) in self.dict.items()}
            d[k] = [pos for pos in self.dict[k] if pos != s] + [t]
            return Node(**d)

        def no_collides_inner(self, s, t):
            if s in hallways:
                i = s[0]
                if t[1] > s[1]:
                    for j in range(s[1] + 1, t[1] + 1):
                        if (i, j) in self.pos2k:
                            return False
                else:
                    for j in range(t[1], s[1]):
                        if (i, j) in self.pos2k:
                            return False
                j = t[1]
                for i in range(s[0], t[0]):
                    if (i, j) in self.pos2k:
                        return False
                return True

            else:
                return self.no_collides_inner(t, s)

        def neighbours(self):
            neis = []
            for k in "ABCD":
                for s in self.dict[k]:
                    if s[1] == self.base(k) and self.is_base_clean(k):
                        continue
                    if s in hallways:
                        if self.is_base_clean(k):
                            if not (LOWER, self.base(k)) in self.pos2k:
                                t = (LOWER, self.base(k))
                                if self.no_collides_inner(s, t):
                                    neis.append((self.cost(s,t,k), self.move(s, t)))
                            else:
                                t = (UPPER, self.base(k))
                                if self.no_collides_inner(s, t):
                                    neis.append((self.cost(s,t,k), self.move(s, t)))
                    else:
                        for t in hallways:
                            if not t in self.pos2k:
                                if self.no_collides_inner(s, t):
                                    neis.append((self.cost(s,t,k), self.move(s, t)))

            return neis


    def part1():
        with open("final.txt") as f:
            final_lines = f.readlines()
        final = Node.from_lines(final_lines)

        node = Node.from_lines(lines)

        for c, nei in node.neighbours():
            print(c)
            print(nei)

        q = [(0, 0, node)]
        visited = set()

        while len(q) > 0:
            _, cost, node = heappop(q)
            if node == final:
                return cost
            visited.add(node)
            for (d, nei) in node.neighbours():
                if nei not in visited:
                    heappush(q, (cost + d + nei.heuristic(), cost + d, nei))


        return 0

    cprint(part1())
    #  cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
