map, movements= open("15.txt", "r").read().split("\n\n")
map = [list(row) for row in map.split('\n')]

newStringMap = [""] * len(map)
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if map[i][j] == "O":
            newStringMap[i] += "[]"
        if map[i][j] == ".":
            newStringMap[i] += ".."
        if map[i][j] == "#":
            newStringMap[i] += "##"
        if map[i][j] == "@":
            newStringMap[i] += "@."

newMap = []
for i in range(len(newStringMap)): # 1453087
    newMap.append([])
    for j in range(len(newStringMap[i])):
        newMap[i].append(newStringMap[i][j])

map = newMap

def makeMoveLeft(map, object):
    if map[object[0]][object[1] - 1] == "#":
        return map, False

    if map[object[0]][object[1] - 1] == ".":
        if map[object[0]][object[1]] == "@":
            map[object[0]][object[1]] = "."
            map[object[0]][object[1] - 1] = "@"
            return map, True
        elif map[object[0]][object[1]] == "[":
            map[object[0]][object[1] - 1] = "["
            map[object[0]][object[1]] = "]"
        else:
            raise Exception("Func called with not @ nor ].")
        return map, True

    if map[object[0]][object[1] - 1] == "]" or map[object[0]][object[1] - 1] == "[":
        map, madeAMove = makeMoveLeft(map, [object[0], object[1] - 1])

        if madeAMove:
            if map[object[0]][object[1]] == "@":
                map[object[0]][object[1]] = "."
                map[object[0]][object[1] - 1] = "@"
                return map, True
            elif map[object[0]][object[1]] == ".":
                map[object[0]][object[1]] = map[object[0]][object[1] + 1]
                map[object[0]][object[1] - 1] = "O"
                return map, True
            elif map[object[0]][object[1]] == "]":
                map[object[0]][object[1]] = "["
            elif map[object[0]][object[1]] == "[":
                map[object[0]][object[1]] = "]"
                return map, True
            return map, True

    return map, False

def makeMoveRight(map, object):
    if map[object[0]][object[1] + 1] == "#":
        return map, False

    if map[object[0]][object[1] + 1] == ".":
        if map[object[0]][object[1]] == "@":
            map[object[0]][object[1]] = "."
            map[object[0]][object[1] + 1] = "@"
            return map, True
        elif map[object[0]][object[1]] == "]":
            map[object[0]][object[1] + 1] = "]"
            map[object[0]][object[1]] = "["
        else:
            raise Exception("Func called with not @ nor ].")
        return map, True

    if map[object[0]][object[1] + 1] == "[" or map[object[0]][object[1] + 1] == "]":
        map, madeAMove = makeMoveRight(map, [object[0], object[1] + 1])

        if madeAMove:
            if map[object[0]][object[1]] == "@":
                map[object[0]][object[1]] = "."
                map[object[0]][object[1] + 1] = "@"
                return map, True
            elif map[object[0]][object[1]] == ".":
                map[object[0]][object[1]] = map[object[0]][object[1] - 1]
                map[object[0]][object[1] + 1] = "O"
                return map, True
            elif  map[object[0]][object[1]] == "[":
                map[object[0]][object[1]] = "]"
            elif map[object[0]][object[1]] == "]":
                map[object[0]][object[1]] = "["
                return map, True
            return map, True

    return map, False

def isRunningIntoObstacleUp(map, object):
    if map[object[0] - 1][object[1]] == "#":
        return True
    if map[object[0] - 1][object[1]] == ".":
        return False

    if map[object[0] - 1][object[1]] == "[":
        return isRunningIntoObstacleUp(map, [object[0] - 1, object[1]]) or isRunningIntoObstacleUp(map, [object[0] - 1, object[1] + 1])

    if map[object[0] - 1][object[1]] == "]":
        return isRunningIntoObstacleUp(map, [object[0] - 1, object[1]]) or isRunningIntoObstacleUp(map, [object[0] - 1, object[1] - 1])

    raise Exception("Unknown Object.")

def isRunningIntoObstacleDown(map, object):
    if map[object[0] + 1][object[1]] == "#":
        return True
    if map[object[0] + 1][object[1]] == ".":
        return False

    if map[object[0] + 1][object[1]] == "[":
        return isRunningIntoObstacleDown(map, [object[0] + 1, object[1]]) or isRunningIntoObstacleDown(map, [object[0] + 1, object[1] + 1])

    if map[object[0] + 1][object[1]] == "]":
        return isRunningIntoObstacleDown(map, [object[0] + 1, object[1]]) or isRunningIntoObstacleDown(map, [object[0] + 1, object[1] - 1])

    if map[object[0] + 1][object[1]] == ".":
        return False

    raise Exception("Unknown Object.")

def moveObstacleUp(map, obstacle):
    if map[obstacle[0]][obstacle[1]] == ".":
        return map

    if map[obstacle[0]][obstacle[1]] == "#":
        raise ZeroDivisionError

    if map[obstacle[0]][obstacle[1]] == "[":
        map = moveObstacleUp(map, (obstacle[0] - 1, obstacle[1]))
        map = moveObstacleUp(map, (obstacle[0] - 1, obstacle[1] + 1))

        map[obstacle[0]][obstacle[1]] = "."
        map[obstacle[0] - 1][obstacle[1]] = "["
        map[obstacle[0]][obstacle[1] + 1] = "."
        map[obstacle[0] - 1][obstacle[1] + 1] = "]"
        return map
    if map[obstacle[0]][obstacle[1]] == "]":
        map = moveObstacleUp(map, (obstacle[0] - 1, obstacle[1]))
        map = moveObstacleUp(map, (obstacle[0] - 1, obstacle[1] - 1))


        map[obstacle[0]][obstacle[1]] = "."
        map[obstacle[0] - 1][obstacle[1]] = "]"
        map[obstacle[0]][obstacle[1] - 1] = "."
        map[obstacle[0] - 1][obstacle[1] - 1] = "["
        return map
    return map

def makeMoveUp(map, object):

    if map[object[0] - 1][object[1]] == ".":
        if map[object[0]][object[1]] == "@":
            map[object[0]][object[1]] = "."
            map[object[0] - 1][object[1]] = "@"
            return map, True
        elif map[object[0]][object[1]] == "[":
            map[object[0] - 1][object[1]] = "["
            map[object[0] - 1][object[1] + 1] = "]"
        elif map[object[0]][object[1]] == "]":
            map[object[0] - 1][object[1]] = "]"
            map[object[0] - 1][object[1] - 1] = "["

        else:
            raise Exception("Func called with not @ nor O.")
        return map, True

    if map[object[0] - 1][object[1]] == "[" or map[object[0] - 1][object[1]] == "]":
        theUp = map[object[0] - 1][object[1]]
        try:
            map = moveObstacleUp(map, [object[0] - 1, object[1]])
        except(ZeroDivisionError):
            return map, False


        if map[object[0]][object[1]] == "@":
            map[object[0]][object[1]] = "."
            if theUp == "[":
                map[object[0] - 1][object[1]] = "@"
                map[object[0] - 1][object[1] + 1] = "."
                return map, True

            if theUp == "]":
                map[object[0] - 1][object[1]] = "@"
                map[object[0] - 1][object[1] - 1] = "."
                return map, True
        return map, True


    return map, False

def moveObstacleDown(map, obstacle):
    if map[obstacle[0]][obstacle[1]] == ".":
        return map

    if map[obstacle[0]][obstacle[1]] == "#":
        raise ZeroDivisionError

    if map[obstacle[0]][obstacle[1]] == "[":
        map = moveObstacleDown(map, (obstacle[0] + 1, obstacle[1]))
        map = moveObstacleDown(map, (obstacle[0] + 1, obstacle[1] + 1))

        map[obstacle[0]][obstacle[1]] = "."
        map[obstacle[0] + 1][obstacle[1]] = "["
        map[obstacle[0]][obstacle[1] + 1] = "."
        map[obstacle[0] + 1][obstacle[1] + 1] = "]"
        return map

    if map[obstacle[0]][obstacle[1]] == "]":
        map = moveObstacleDown(map, (obstacle[0] + 1, obstacle[1]))
        map = moveObstacleDown(map, (obstacle[0] + 1, obstacle[1] - 1))

        map[obstacle[0]][obstacle[1]] = "."
        map[obstacle[0] + 1][obstacle[1]] = "]"
        map[obstacle[0]][obstacle[1] - 1] = "."
        map[obstacle[0] + 1][obstacle[1] - 1] = "["
        return map

    return map

def makeMoveDown(map, object):

    if map[object[0] + 1][object[1]] == ".":
        if map[object[0]][object[1]] == "@":
            map[object[0]][object[1]] = "."
            map[object[0] + 1][object[1]] = "@"
            return map, True
        elif map[object[0]][object[1]] == "[":
            map[object[0] + 1][object[1]] = "["
            map[object[0] + 1][object[1] + 1] = "]"
        elif map[object[0]][object[1]] == "]":
            map[object[0] + 1][object[1]] = "]"
            map[object[0] + 1][object[1] - 1] = "["

        else:
            raise Exception("Func called with not @ nor O.")
        return map, True

    if map[object[0] + 1][object[1]] == "[" or map[object[0] + 1][object[1]] == "]":
        theDown = map[object[0] + 1][object[1]]
        try:
            map = moveObstacleDown(map, [object[0] + 1, object[1]])
        except(ZeroDivisionError):
            return map, False

        if map[object[0]][object[1]] == "@":
            map[object[0]][object[1]] = "."
            if theDown == "[":
                map[object[0] + 1][object[1]] = "@"
                map[object[0] + 1][object[1] + 1] = "."
                return map, True

            if theDown == "]":
                map[object[0] + 1][object[1]] = "@"
                map[object[0] + 1][object[1] - 1] = "."
                return map, True
        return map, True

    return map, False



def makeMove(map, move):
    robot = None
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == "@":
                robot = [i, j]
                break

    if robot is None:
        raise Exception("No robot found")


    if move == '<':
        map, b = makeMoveLeft(map, robot)
        return map
    if move == '>':
        map, b = makeMoveRight(map, robot)
        return map
    if move == '^' and not isRunningIntoObstacleUp(map, robot):
        map, b = makeMoveUp(map, robot)
        return map
    if move == 'v' and not isRunningIntoObstacleDown(map, robot):
        map, b = makeMoveDown(map, robot)
        return map
    return map

def prettyPrint(map):
    for row in map:
        for cell in row:
            print(cell, end='')
        print()


for move in movements:
    map = makeMove(map, move)
    #prettyPrint(map)


sum = 0
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if map[i][j] == "[":
            sum += i * 100 + j

print(sum)