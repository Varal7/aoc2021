a, b, c = 4, 5, 15
w = x = y = z = 0

x = (z %26 + b != w)
z //= a
z *= 25 * x + 1
z += (w + c) * x

if z % 26 + b != w:
    z //= a
    z *= 26
    z += (w + c)
else:
    z //= a

if a == 1:
    # we observe b is always > 10 so:
    z *= 26
    z += (w+c)
elif z % 26 + b != w:
    z += (w+c)
else:
    z //= 26


def find_repeat():
    with open("input.txt") as f:
        lines = f.readlines()
        for i, _ in enumerate(lines):
            if i < 18:
                continue
            if lines[i - 18] != lines[i]:
                print(i % 18, lines[i].strip())

def find_all():
    with open("input.txt") as f:
        lines = f.readlines()
        for i, _ in enumerate(lines):
            if i % 18 not in [4,5,15]:
                continue
            if i% 18 == 4:
                print(i//18, end="\t")
            print(i % 18, lines[i].strip(), end="\t")
            if i % 18 == 15:
                print()

def get_constraints():
    with open("input.txt") as f:
        lines = f.readlines()
        last_a = None
        stack = []
        for i, line in enumerate(lines):
            if i % 18 not in [4,5,15]:
                continue
            if i % 18 == 4:
                _, _, last_a = line.strip().split()
                continue
            if i % 18 == 5:
                if last_a == "26":
                    _, _, b = line.strip().split()
                    idx, old_c = stack.pop()
                    #  print(f"inp[{idx // 18}] + {old_c} + {b} == inp[{i // 18}]")
                    print(f"inp[{idx // 18}] + {int(old_c) + int(b)} == inp[{i // 18}]")
            if i % 18 == 15:
                if last_a == "1":
                    _, _, c = line.strip().split()
                    stack.append((i, c))


find_all()
get_constraints()

# 01234567890123
# 99394899891971

#  01234567890123
#  92171126131911
