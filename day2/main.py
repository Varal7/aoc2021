h = 0
depth = 0
aim = 0

for line in open("input.txt").readlines():
#  for line in open("test.txt").readlines():
    c, n = line.strip().split()
    n = int(n)
    if c == "down":
        aim += n
    if c == "up":
        aim -= n
    if c == "forward":
        h += n
        depth += aim * n


print(h * depth)
