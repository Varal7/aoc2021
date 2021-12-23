import re
from collections import *
from functools import *
from itertools import *
from math import *
import pyperclip
import numpy as np
import sys
from tqdm import tqdm

from heapq import heapify, heappop, heappush

def cprint(t):
    print(t)
    pyperclip.copy(t)

def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    def part1():
        arr = np.zeros((101, 101, 101))
        for line in lines:
            val, rest = line.strip().split(" ")
            x, y, z = rest.split(",")
            xstart, xend = map(int, x[2:].split(".."))
            ystart, yend = map(int, y[2:].split(".."))
            zstart, zend = map(int, z[2:].split(".."))
            if -50 <= xstart <= 50:
                if val == "on":
                    arr[xstart+50: xend+50+1, ystart+50: yend+50+1, zstart+50:zend+50+1] = 1
                if val == "off":
                    arr[xstart+50: xend+50+1, ystart+50: yend+50+1, zstart+50:zend+50+1] = 0

        return int(arr.sum())

    def part2():
        c = Counter()
        xs = []
        ys = []
        zs = []
        s = []
        for line in lines:
            val, rest = line.strip().split(" ")
            x, y, z = rest.split(",")
            xstart, xend = map(int, x[2:].split(".."))
            ystart, yend = map(int, y[2:].split(".."))
            zstart, zend = map(int, z[2:].split(".."))
            s.append((val=="on", (xstart, xend + 1), (ystart, yend + 1), (zstart, zend + 1)))
            xs.append(xstart)
            xs.append(xend + 1)
            ys.append(ystart)
            ys.append(yend + 1)
            zs.append(zstart)
            zs.append(zend + 1)

        xs.sort()
        ys.sort()
        zs.sort()
        s.reverse()

        count = 0

        for x1, x2 in tqdm(zip(xs, xs[1:]), total=len(xs)):
            covers_x = [(val, x, y, z) for (val, x, y, z) in s if x[0] <= x1 < x[1]]
            for y1, y2 in zip(ys, ys[1:]):
                covers_y = [(val, x, y, z) for (val, x, y, z) in covers_x if y[0] <= y1 < y[1]]
                for z1, z2 in zip(zs, zs[1:]):
                    if next((val for (val, _, _, z) in covers_y if z[0] <= z1 < z[1]), False):
                        count += (x2 - x1) * (y2 - y1) * (z2 - z1)

        return count


    cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
