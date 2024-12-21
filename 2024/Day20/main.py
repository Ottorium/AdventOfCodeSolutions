from modifiedDay16 import solve

maze = [list(line.strip()) for line in open("20.txt", 'r')]
normal = solve(maze)

saves = list()
print("This might take a while")
for i in range(1, len(maze) - 1):
    for j in range(1, len(maze[0]) - 1):
        if maze[i][j] != "#": continue
        maze[i][j] = "."
        current = solve(maze)
        maze[i][j] = "#"

        if current <= normal - 100:
            saves.append(current)

print("Part 1: " + str(len(saves)))
print("I wasn't able to solve part 2")
