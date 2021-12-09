import numpy as np
def main():

    with open("input.txt") as f:
        lines = f.readlines()


    nums = list(map(int, lines[0].strip().split(",")))


    grids = []
    masks = []
    buf = []
    for line in lines[2:] + ["\n"]:
        if line == "\n":
            arr = np.array(buf)
            grids.append(arr)
            buf = []
            masks.append(np.zeros_like(arr))

        else:
            buf.append(list(map( int, line.strip().split())))

    for num in nums:
        for grid, mask in zip(grids, masks):
            mask[grid == num] = 1
            if len(mask[mask.sum(0) == 5]) > 0 or len(mask[mask.sum(1) == 5]):
                return grid[mask == 0].sum() * num


    print(grids[0])
    print(grids[1])
    print(grids[2])

    print(masks[0])
    print(masks[1])
    print(masks[2])

print(main())
