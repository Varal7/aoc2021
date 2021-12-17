import re
from collections import *
from functools import *
from itertools import *
import numpy as np
from math import prod
import pyperclip
import sys
sys.setrecursionlimit(1000*1000*1000)

from heapq import heapify, heappop, heappush

def cprint(t):
    print(t)
    pyperclip.copy(t)


def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    def part1():
        line = lines[0].strip()
        _, r = line.split(": ")
        xx, yy = r.split(", ")
        x_min, x_max = map(int, xx[2:].split(".."))
        y_min, y_max = map(int, yy[2:].split(".."))

        def meets(vx, vy, x, y):
            if y < y_min and vy < 0:
                return None
            if x > x_max and vx >= 0:
                return  None
            if x_min<= x <= x_max and y_min <= y <= y_max:
                return y

            x += vx
            y += vy

            new_vx = vx - 1 if vx > 0 else 0 if vx == 0 else vx + 1
            max_y = meets(new_vx, vy - 1, x, y)
            return max_y if max_y is None else max(max_y, y)

        max_height = None
        for vx in range(1, x_max):
            for vy in range(0, 900):
                val = meets(vx, vy, 0, 0)
                if val is not None:
                    if max_height is None or val > max_height:
                        max_height = val
        return max_height

    def part2():
        line = lines[0].strip()
        _, r = line.split(": ")
        xx, yy = r.split(", ")
        x_min, x_max = map(int, xx[2:].split(".."))
        y_min, y_max = map(int, yy[2:].split(".."))

        def meets(vx, vy, x, y):
            if y < y_min and vy < 0:
                return None
            if x > x_max and vx >= 0:
                return  None
            if x_min<= x <= x_max and y_min <= y <= y_max:
                return y

            x += vx
            y += vy

            new_vx = vx - 1 if vx > 0 else 0 if vx == 0 else vx + 1
            max_y = meets(new_vx, vy - 1, x, y)
            return max_y if max_y is None else max(max_y, y)

        count = 0
        for vx in range(1, x_max+1):
            for vy in range(-100, 900):
                val = meets(vx, vy, 0, 0)
                if val is not None:
                    count += 1
        return count


    cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
