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

    def part1():
        for line in lines:
            line = line.strip()
        nums = list(map( int, lines[0].split(",")))

        nums = sorted(nums)
        n = len(nums)
        median = nums[n//2]
        return (sum(x - median if x > median else median -x for x in nums))

    def part2():
        for line in lines:
            line = line.strip()
        nums = list(map( int, lines[0].split(",")))
        nums = sorted(nums)
        n = len(nums)
        mean = round(sum(nums) / n)
        print( sum(abs(x - mean) * (abs(x-mean)  + 1) // 2  for x in nums))
        mean -= 1
        print( sum(abs(x - mean) * (abs(x-mean)  + 1) // 2  for x in nums))
        mean += 2
        print( sum(abs(x - mean) * (abs(x-mean)  + 1) // 2  for x in nums))

        return mean


    #  cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
