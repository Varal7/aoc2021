import numpy as np

lines = open("input.txt").readlines()
#  lines = open("test.txt").readlines()

n = len(lines)
m = len(lines[0].strip())

arr = np.array([list(map(int,line.strip())) for line in lines])

arr_oxy = arr[:]
arr_co2 = arr[:]

for i in range(m):
    val = 1 if arr_oxy[:,i].sum() >= (len(arr_oxy) / 2) else 0
    arr_oxy = arr_oxy[arr_oxy[:,i] == val]
    if arr_oxy.shape[0] == 1:
        break

for i in range(m):
    val = 1 if arr_co2[:,i].sum() < (len(arr_co2) / 2) else 0
    arr_co2 = arr_co2[arr_co2[:,i] == val]
    if arr_co2.shape[0] == 1:
        break

co2 = int("".join(map(str, arr_co2[0])), 2)
oxy = int("".join(map(str, arr_oxy[0])), 2)

print(co2 * oxy)
