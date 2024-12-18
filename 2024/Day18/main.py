from modifiedDay16 import solve

with open("18.txt", 'r') as file:
    lines = [line for line in file]


def pretty_print(grid):
    for row in grid:
        print("".join(row))
    print()


def solvePart1(grid, n):
    for i in range(n):
        line = lines[i]
        x, y = line.split(",")
        x = int(x)
        y = int(y.strip("\n"))
        grid[int(y)][int(x)] = "#"
    grid[0][0] = "S"
    grid[-1][-1] = "E"

    cols = len(grid[0])

    bordered_grid = [
        ['#'] * (cols + 2)  # Top border row
    ]
    for row in grid:
        bordered_grid.append(['#'] + list(row) + ['#'])
    bordered_grid.append(['#'] * (cols + 2))
    r = solve(bordered_grid)
    return r

width = 71
height = 71

grid = [['.' for _ in range(width)] for _ in range(height)]

print("Part 1: " + str(solvePart1(grid, 1024)))
print("for part 2 I binary searched")
