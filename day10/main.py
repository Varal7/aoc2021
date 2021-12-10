import re
from collections import *
from functools import *
from itertools import *
import numpy as np
import pyperclip

openings = "[({<"
closings = "])}>"

o2c = {x:y for x,y in zip(openings, closings)}
c2o = {y:x for x,y in zip(openings, closings)}

def cprint(t):
    print(t)
    pyperclip.copy(t)


def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    def part1():
        points = {
                ")": 3,
                "]": 57,
                "}": 1197 ,
                ">": 25137,
        }

        ans = 0
        for line in lines:
            line = line.strip()
            stack = []
            for c in line:
                if c in openings:
                    stack.append(c)
                else:
                    o = stack.pop()
                    if c2o[c] != o:
                        ans += points[c]
                        break
        return ans

    def part2():
        points = {
                ")": 1,
                "]": 2,
                "}": 3 ,
                ">": 4,
        }

        values = []

        for line in lines:
            value = 0
            line = line.strip()
            stack = []
            discard = False
            for c in line:
                if c in openings:
                    stack.append(c)
                else:
                    o = stack.pop()
                    if c2o[c] != o:
                        discard = True
                        break

            if discard:
                continue

            while len(stack) > 0 :
                o = stack.pop()
                value *= 5
                value += points[o2c[o]]

            values.append(value)

        values.sort()
        return values[len(values)//2]

    cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
