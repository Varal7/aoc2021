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
        count = 0
        d = {2: 1, 4: 4, 3: 7, 7: 8}
        for line in lines:
            line = line.strip()
            line = line.split(" | ")[1]
            count += sum(1 for word in line.split() if len(word) in d)
        return count

    def part2():
        ok = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
        ok2i = {o: i for (i, o) in enumerate(ok)}

        count = 0
        for line in lines:
            line = line.strip()
            inp = line.split(" | ")[0]
            out = line.split(" | ")[1]

            for permute in permutations("abcdefg"):
                d = dict()
                for k, v in zip("abcdefg", permute):
                    d[k] = v

                found = True

                for word in inp.split():
                    new = "".join(sorted([d[el] for el in word]))
                    if new not in ok:
                        found = False
                        break

                if found:
                    digits = ""
                    for word in out.split():
                        real_out = "".join(sorted([d[el] for el in word]))
                        digits += str(ok2i[real_out])

                    count += int(digits)
                    break


        return count

    cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
