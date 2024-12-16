import heapq
from copy import deepcopy

with open("16.txt", 'r') as file:
    maze = [list(line.strip()) for line in file]

startPos = 0
endPos = 0
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 'S':
            startPos = (i, j)
        if maze[i][j] == 'E':
            endPos = (i, j)

queue = [(0,  # cost
          startPos[0], startPos[1],  # position
          0, 1,  # direction
          )]
seen = {(startPos[0], startPos[1], 0, 1)}
references = {(0, startPos[0], startPos[1], 0, 1): None  # key to previous node
              }

lowestCost = float("inf")
while queue:
    cCost, cRow, cCol, cDirRow, cDirCol = heapq.heappop(queue)
    currentNode = (cCost, cRow, cCol, cDirRow, cDirCol)
    seen.add((cRow, cCol, cDirRow, cDirCol))
    if maze[cRow][cCol] == 'E':
        if cCost <= lowestCost:
            lowestCost = cCost

    newThings = [
        (cCost + 1, cRow + cDirRow, cCol + cDirCol, cDirRow, cDirCol),
        (cCost + 1000, cRow, cCol, cDirCol, -cDirRow),
        (cCost + 1000, cRow, cCol, -cDirCol, cDirRow)
    ]
    for newCost, newRow, newCol, newDirY, newDirX in newThings:
        if (newRow, newCol, newDirY, newDirX) in seen:
            continue
        if maze[newRow][newCol] == '#':
            continue

        heapq.heappush(queue, (newCost, newRow, newCol, newDirY, newDirX))

        key = (newCost, newRow, newCol, newDirY, newDirX)
        if key in references:
            references[key].append(currentNode)
        else:
            references[key] = [currentNode]
print("Part 1: " + str(lowestCost))


def paintMaze(maze, references, val, seen):
    if val not in references:
        raise ValueError("val not in references")
    if val in seen: return maze
    seen.add(val)
    rs = references[val]
    if rs is None: return maze
    for nextValue in rs:
        cCost, cRow, cCol, cDirRow, cDirCol = nextValue
        maze[cRow][cCol] = "O"
        paintMaze(maze, references, nextValue, seen)


val = references[(lowestCost, endPos[0], endPos[1], -1, 0)][0]
painted_maze = deepcopy(maze)
paintMaze(painted_maze, references, val, set())

count = 0
for i in range(0, len(painted_maze)):
    for j in range(0, len(painted_maze[i])):
        if painted_maze[i][j] == 'E' or painted_maze[i][j] == 'S':
            painted_maze[i][j] = "O"
        if painted_maze[i][j] == 'O':
            count += 1
print("Part 2: " + str(count + 1))
