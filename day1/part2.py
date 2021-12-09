lines = open("input.txt").readlines()

nums = list(map(int, lines))
n = len(nums)
prev = None

count = 0
for i in range(0, n-2):
    cur =  sum(nums[i: i+3])
    if prev is not None and  cur > prev:
        print(cur)
        count += 1
    prev = cur

print(count)
