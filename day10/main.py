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


    cprint(part1())
    #  cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
