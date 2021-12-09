import numpy as np

lines = open("input.txt").readlines()
#  lines = open("test.txt").readlines()

n = len(lines)
m = len(lines[0].strip())

arr = np.array([list(map(int,line.strip())) for line in lines])

gamma = [1 if arr[:,i].sum() > n / 2 else 0 for i in range(m)]
epsilon = [1 if arr[:,i].sum() < n / 2 else 0 for i in range(m)]

gamma = int("".join(map(str, gamma)), 2)
epsilon = int("".join(map(str, epsilon)), 2)

print(gamma * epsilon)
