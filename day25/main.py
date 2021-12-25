import re
from collections import *
from functools import *
from itertools import *
from math import *
import pyperclip
import numpy as np
from sympy import symbols, Eq, Piecewise, Integer, simplify
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
        n = len(lines)
        m = len(lines[0].strip())
        down = np.zeros((n, m))
        right = np.zeros((n, m))
        for i, line in enumerate(lines):
            for j, c in enumerate(line.strip()):
                if c == ">":
                    right[i][j] = 1
                if c == "v":
                    down[i][j] = 1

        count = 0

        def shift_left(arr: np.array) -> np.array :
            return np.concatenate((arr[:,1:], arr[:,:1]), axis=1)

        def shift_right(arr: np.array) -> np.array :
            return np.concatenate((arr[:,-1:], arr[:,:-1]), axis=1)

        def shift_up(arr: np.array) -> np.array :
            return np.concatenate((arr[1:,:], arr[:1,:]), axis=0)

        def shift_down(arr: np.array) -> np.array:
            return np.concatenate((arr[-1:,:], arr[:-1,:]), axis=0)

        while True:
            moved = False
            right_mask = shift_left(down + right)
            right_moving = right * (1 - right_mask)
            right -= right_moving
            right += shift_right(right_moving)
            if right_moving.sum() > 0:
                moved = True

            down_mask = shift_up(down + right)
            down_moving = down * (1 - down_mask)
            down -= down_moving
            down += shift_down(down_moving)
            if down_moving.sum() > 0:
                moved = True

            count += 1

            if not moved:
                break

        return count


    cprint(part1())
    #  cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
