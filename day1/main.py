lines = open("input.txt").readlines()

prev = None
count = 0
for line in lines:
    cur = int(line)
    if prev is not None and cur > prev:
        count += 1

    prev = cur

print(count)
