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
        num_steps = 10
        rules = dict()
        X = []
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            if "->" in line:
                k, v = (line.split(" -> "))
                rules[k] = v
            else:
                X = list(line)

        for _ in range(num_steps):
            buf = []
            for i in range(len(X) - 1):
                buf.append(rules["".join([X[i], X[i+1]])])
            new_X = []
            for i in range(len(buf)):
                new_X.append(X[i])
                new_X.append(buf[i])
            new_X.append(X[-1])
            X = new_X

        c = Counter(X).most_common()
        return c[0][1] - c[-1][1]


    def part2():
        num_steps = 40
        rules = dict()
        X = []
        count = Counter()
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            if "->" in line:
                k, v = (line.split(" -> "))
                rules[k] = (k[0] + v, v + k[1])
            else:
                X = list(line)

        for i in range(len(X) - 1):
            count[X[i] + X[i+1]] += 1

        for _ in range(num_steps):
            new_count = Counter()
            for k, v in count.items():
                new_count[rules[k][0]] += v
                new_count[rules[k][1]] += v
                new_count[k] -= v

            count += new_count
            #  print(count)

        real_count = Counter()
        for k, v in count.items():
            real_count[k[0]] += v
            real_count[k[1]] += v
        real_count[X[0]] += 1
        real_count[X[-1]] += 1

        c = real_count.most_common()
        return (c[0][1] - c[-1][1]) // 2


    #  cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
