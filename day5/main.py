from collections import defaultdict
import numpy as np


def main():
    #  with open("test.txt") as f:
    #  with open("test2.txt") as f:
    with open("input.txt") as f:
        lines = f.readlines()


    def part1():
        xmax = None
        ymax = None

        for line in lines:
            line = line.strip()
            a, b = line.split(" -> ")
            x1,y1 = a.split(",")
            x2,y2 = b.split(",")
            x1,y1,x2,y2 = map(int, [x1, y1, x2, y2])
            if xmax is None or x1 > xmax:
                xmax = x1
            if xmax is None or x2 > xmax:
                xmax = x2
            if ymax is None or y1 > ymax:
                ymax = y1
            if ymax is None or y2 > ymax:
                ymax = y2

        tab = np.array([[0 for _ in range(ymax + 1)] for _ in range(xmax + 1)])

        for line in lines:
            line = line.strip()
            a, b = line.split(" -> ")
            x1,y1 = a.split(",")
            x2,y2 = b.split(",")
            x1,y1,x2,y2 = map(int, [x1, y1, x2, y2])

            if x1 == x2:
                y1, y2 = min(y1, y2), max(y1, y2)
                tab[x1, y1: y2 + 1] += 1

            if y1 == y2:
                x1, x2 = min(x1, x2), max(x1, x2)
                tab[x1:x2+ 1, y1] += 1

        print(tab)

        return (tab >= 2).sum()

    def part2():
        xmax = None
        ymax = None

        for line in lines:
            line = line.strip()
            a, b = line.split(" -> ")
            x1,y1 = a.split(",")
            x2,y2 = b.split(",")
            x1,y1,x2,y2 = map(int, [x1, y1, x2, y2])
            if xmax is None or x1 > xmax:
                xmax = x1
            if xmax is None or x2 > xmax:
                xmax = x2
            if ymax is None or y1 > ymax:
                ymax = y1
            if ymax is None or y2 > ymax:
                ymax = y2

        tab = np.array([[0 for _ in range(ymax + 1)] for _ in range(xmax + 1)])

        for line in lines:
            line = line.strip()
            a, b = line.split(" -> ")
            x1,y1 = a.split(",")
            x2,y2 = b.split(",")
            x1,y1,x2,y2 = map(int, [x1, y1, x2, y2])

            if x1 == x2:
                y1, y2 = min(y1, y2), max(y1, y2)
                tab[x1, y1: y2 + 1] += 1

            elif y1 == y2:
                x1, x2 = min(x1, x2), max(x1, x2)
                tab[x1:x2+ 1, y1] += 1

            elif (x1 - x2) * (y1 - y2) > 0:
                x1, x2 = min(x1, x2), max(x1, x2)
                y1, y2 = min(y1, y2), max(y1, y2)

                for i in range(x2 - x1 + 1):
                    tab[x1 +i, y1+i] += 1

            else:
                x1, x2 = min(x1, x2), max(x1, x2)
                y1, y2 = max(y1, y2), min(y1, y2)

                for i in range(x2 - x1 + 1):
                    tab[x1 +i, y1-i] += 1

        print(tab.T)

        return (tab >= 2).sum()

    #  print(part1())
    print(part2())

main()
