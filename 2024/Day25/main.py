blocks = open("25.txt").read().split("\n\n")

locks = list()
keys = list()
for block in blocks:
    grid = [[s] for s in zip(*block.split("\n")[1:])]

    nums = list()
    for row in grid:
        c = 0
        for s in row[0] if block[0][0] == "#" else row[0][:-1]:
            c += 1 if s == "#" else 0
        nums.append(c)

    if block[0][0] == "#":
        locks.append(nums)
    else:
        keys.append(nums)


def couldFit(key, lock):
    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False
    return True

s = 0
for lock in locks:

    for key in keys:
        if couldFit(key, lock):
            s += 1
print("Part 1: " + str(s))
print("Could not get Part 2 because I didn't solve all of the previous puzzles'")
