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

    neis = defaultdict(list)

    def part1():
        for line in lines:
            line = line.strip()
            a,b = line.split("-")
            neis[a].append(b)
            neis[b].append(a)

        def explore(past):
            #  print(past)
            count = 0
            if past[-1] == "end":
                return 1
            for nei in neis[past[-1]]:
                if nei.isupper() or nei not in past:
                    count += explore(past + [nei])

            return count

        return explore(["start"])


    def part2():
        for line in lines:
            line = line.strip()
            a,b = line.split("-")
            neis[a].append(b)
            neis[b].append(a)

        def explore(past, used=False):
            count = 0
            if past[-1] == "end":
                return 1
            for nei in neis[past[-1]]:
                if nei.isupper() or nei not in past:
                    count += explore(past + [nei], used)

                if not used and nei not in ["start", "end"] and nei.islower() and nei in past:
                    count += explore(past + [nei], True)

            return count

        return explore(["start"])



    #  cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
#  main("test2.txt")
print("Real")
main("input.txt")
