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
        arr = []
        for line in lines:
            arr.append([int(x) for x in line.strip()])
        arr = np.array(arr)
        num_steps = 100

        n = len(arr)
        m = len(arr[0])

        count = 0

        for _ in range(num_steps):
            arr += np.ones_like(arr)
            flashing = arr > 9
            flash_q = []
            for i in range(n):
                for j in range(m):
                    if flashing[i][j]:
                        flash_q.append((i, j))
            flashed = set(flash_q)

            while len(flash_q) > 0:
                #  print(arr)
                #  print(flash_q)
                (i,j) = flash_q.pop()
                #  print("<", (i, j))
                for ii in range(max(0, i-1),min(n,i+2)):
                    for jj in range(max(0, j-1), min(m, j+2)):
                        if (i,j) != (ii,jj):
                            arr[ii,jj] += 1
                            if arr[ii,jj] > 9 and (ii,jj) not in flashed:
                                flash_q.append((ii, jj))
                                #  print(">", (ii,jj))

                                flashed.add((ii, jj))
                                flashing[ii,jj] = True

            arr[flashing] = 0
            count += len(flashed)

            #  print(arr)



        return count


    def part2():
        arr = []
        for line in lines:
            arr.append([int(x) for x in line.strip()])
        arr = np.array(arr)

        n = len(arr)
        m = len(arr[0])

        count = 0

        while True:
            count += 1
            arr += np.ones_like(arr)
            flashing = arr > 9
            flash_q = []
            for i in range(n):
                for j in range(m):
                    if flashing[i][j]:
                        flash_q.append((i, j))
            flashed = set(flash_q)

            while len(flash_q) > 0:
                #  print(arr)
                #  print(flash_q)
                (i,j) = flash_q.pop()
                #  print("<", (i, j))
                for ii in range(max(0, i-1),min(n,i+2)):
                    for jj in range(max(0, j-1), min(m, j+2)):
                        if (i,j) != (ii,jj):
                            arr[ii,jj] += 1
                            if arr[ii,jj] > 9 and (ii,jj) not in flashed:
                                flash_q.append((ii, jj))
                                #  print(">", (ii,jj))

                                flashed.add((ii, jj))
                                flashing[ii,jj] = True

            arr[flashing] = 0

            if len(flashed) == 100:
                break




        return count


    cprint(part1())
    cprint(part2())

print("Test")
main("test.txt")
#  main("test2.txt")
print("Real")
main("input.txt")
