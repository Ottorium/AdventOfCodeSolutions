import heapq
def solve(maze):
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
            return cCost

        newThings = [
            (cCost + 1, cRow + cDirRow, cCol + cDirCol, cDirRow, cDirCol),
            (cCost + 0, cRow, cCol, cDirCol, -cDirRow),
            (cCost + 0, cRow, cCol, -cDirCol, cDirRow)
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