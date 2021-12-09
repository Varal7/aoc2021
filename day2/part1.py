x = 0
y = 0

dire = {
        'forward': (1, 0),
        'up': (0, -1),
        'down': (0, 1),
        }

for line in open("input.txt").readlines():
    c, n = line.strip().split()
    n = int()
    for _ in range(n):
        x += dire[c][0]
        y += dire[c][1]


print(x * y)
