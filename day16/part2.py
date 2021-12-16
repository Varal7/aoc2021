import re
from collections import *
from functools import *
from itertools import *
import numpy as np
from math import prod
import pyperclip

from heapq import heapify, heappop, heappush

def cprint(t):
    print(t)
    pyperclip.copy(t)


def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    line = lines[0].strip()

    def str2li(s):
        d = {
        "0" : "0000",
        "1" : "0001",
        "2" : "0010",
        "3" : "0011",
        "4" : "0100",
        "5" : "0101",
        "6" : "0110",
        "7" : "0111",
        "8" : "1000",
        "9" : "1001",
        "A" : "1010",
        "B" : "1011",
        "C" : "1100",
        "D" : "1101",
        "E" : "1110",
        "F" : "1111",
                }
        buf = ""
        for c in s:
            buf += d[c]
        return list(map(int, buf))

    def l2val(li):
        return int("".join(map(str,li)), 2)

    def part1():
        s = str2li(line)
        n = len(s)
        count = 0


        def parse_lit_val(j, prev):
            if s[j] == 0:
                j+= 5
                return j, prev * 16 + l2val(s[j-4:j])
            else:
                j+=5
                return parse_lit_val(j, prev * 16 + l2val(s[j-4:j]) )


        def parse_packet(i):
            nonlocal count
            V = l2val(s[i:i+3])
            count += V
            i+=3
            T = l2val(s[i:i+3])
            i+=3
            if T == 4:
                i, val = parse_lit_val(i, 0)
                return i, val
            else:
                values = []
                I = s[i]
                i+=1
                if I == 0:
                    L = l2val(s[i:i+15])
                    i+=15
                    end = i + L
                    while i < end:
                        i, val = parse_packet(i)
                        values.append(val)

                else:
                    L = l2val(s[i:i+11])
                    i += 11
                    for j in range(L):
                        i = parse_packet(i)
                        values.append(val)

                if T == 0:
                    return i, sum(values)
                if T == 1:
                    return i, prod(values)
                if T == 2:
                    return i, min(values)
                if T == 3:
                    return i, max(values)
                if T == 5:
                    return i, 1 if values[0] > values[1] else 0
                if T == 6:
                    return i, 1 if values[0] < values[1] else 0
                if T == 7:
                    return i, 1 if values[0] == values[1] else 0

                assert(False)



        print(parse_packet(0))
        print(n)

        return count

    cprint(part1())
    #  cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
