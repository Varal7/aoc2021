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


    def part1():
        p1 = int(lines[0].strip()[-1])
        p2 = int(lines[1].strip()[-1])

        p1_score = 0
        p2_score = 0

        dice = 1

        while True:
            p1 = (p1 + (3 * (dice + 1))) % 10
            if p1 == 0:
                p1 = 10
            p1_score += p1
            dice += 3
            if p1_score >= 1000:
                return p2_score * (dice - 1)

            p2 = (p2 + (3 * (dice + 1))) % 10
            if p2 == 0:
                p2 = 10
            p2_score += p2
            dice += 3

            if p2_score >= 1000:
                return p1_score * (dice - 1)

    def part2():
        init_p1 = int(lines[0].strip()[-1])
        init_p2 = int(lines[1].strip()[-1])

        thresh = 21

        def normalize(pos):
            pos = pos % 10
            if pos == 0:
                pos = 10
            return pos

        @lru_cache
        def get_occur(p1, p2, p1_score, p2_score, p1_plays):
            if (p1_score, p2_score) == (0, 0):
                if (p1, p2, p1_plays) == (init_p1, init_p2, True):
                    return 1
                return 0

            if p1_score < 0 or p2_score < 0:
                return 0

            if p1_plays:
                count = 0
                for die in [1,2,3]:
                    if p2_score - p2 < thresh:
                        count += get_occur(p1, normalize(p2 - die), p1_score, p2_score - p2, False)
                return count

            else:
                count = 0
                for die in [1,2,3]:
                    if p1_score - p1 < thresh:
                        count += get_occur(normalize(p1 - die), p2, p1_score - p1, p2_score, True)
                return count

        p1_victories = 0
        p2_victories = 0
        for p1 in range(1, 11):
            for p2 in range(1, 11):
                for p1_score in range(thresh, thresh + 10):
                    for p2_score in range(thresh):
                        val = get_occur(p1, p2, p1_score, p2_score, False)
                        #  if val > 0:
                        #      print(p1, p2, p1_score, p2_score, False, val)
                        p1_victories += val
                for p2_score in range(thresh, thresh + 10):
                    for p1_score in range(thresh):
                        val = get_occur(p1, p2, p1_score, p2_score, True)
                        #  if val > 0:
                        #      print(p1, p2, p1_score, p2_score, True, val)
                        p2_victories +=val

        print(p1_victories)
        print(p2_victories)


        return max(p1_victories, p2_victories)




    cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
