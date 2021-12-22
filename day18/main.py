import re
from collections import *
from functools import *
from itertools import *
import pyperclip
import sys

from heapq import heapify, heappop, heappush

def cprint(t):
    print(t)
    pyperclip.copy(t)


class Snailfish:
    def __init__(self, x):
        self.value = None
        self.left = None
        self.right = None
        self.parent = None
        self.is_left = None
        self.is_right = None

        if isinstance(x, int):
            self.value = x
        else:
            self.assign_left(x[0])
            self.assign_right(x[1])

    def assign_left(self, left):
        if not isinstance(left, Snailfish):
            left = Snailfish(left)
        self.left = left
        self.left.parent = self
        self.left.is_left = True
        self.left.is_right = False

    def assign_right(self, right):
        if not isinstance(right, Snailfish):
            right = Snailfish(right)
        self.right = right
        self.right.parent = self
        self.right.is_right = True
        self.right.is_left = False

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        return f"[{self.left},{self.right}]"

    def magnitude(self):
        if self.value is not None:
            return self.value
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def __add__(self, other):
        return Snailfish([self, other])

    def replace(self, x):
        assert self.is_left or self.is_right
        assert self.parent is not None
        if self.is_left:
            self.parent.assign_left(x)
        else:
            self.parent.assign_right(x)

    def reduce(self):
        exploded = False
        right = None
        last = None

        def explode(node, depth=0):
            nonlocal exploded, right, last
            if node.value is not None:
                if right is not None:
                    node.value += right
                    right = None
                last = node
                return

            if depth == 4 and not exploded:
                if last is not None:
                    last.value += node.left.value
                right = node.right.value
                exploded = True
                node.replace(Snailfish(0))

            else:
                explode(node.left, depth+1)
                explode(node.right, depth+1)


        done = False
        def split(node):
            nonlocal done
            if done: return
            if node.value is not None:
                if node.value >= 10:
                    left = node.value // 2
                    right = node.value - left
                    node.replace(Snailfish([left, right]))
                    done = True
                return
            split(node.left)
            split(node.right)

        explode(self, depth=0)

        if exploded:
            return True

        split(self)

        if done:
            return True

        return False

    def full_reduce(self):
        while self.reduce():
            pass


def main(filename):
    def part1():
        with open(filename) as f:
            lines = f.readlines()
            numbers = [Snailfish(eval(line.strip())) for line in lines]
        s = numbers[0]
        for d in numbers[1:]:
            s += d
            s.full_reduce()
        print(s)
        return s.magnitude()


    def part2():
        with open(filename) as f:
            lines = f.readlines()
        n = len(lines)
        mag_max = None
        for i in range(n):
            for j in range(n):
                if i != j:
                    s = Snailfish(eval(lines[i].strip())) + Snailfish(eval(lines[j].strip()))
                    s.full_reduce()
                    mag = s.magnitude()
                    if mag_max is None or mag > mag_max:
                        mag_max = mag

        return mag_max


    cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
print("Real")
main("input.txt")
