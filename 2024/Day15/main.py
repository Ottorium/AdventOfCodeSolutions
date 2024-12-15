map, movements= open("15.txt", "r").read().split("\n\n")
map = [list(row) for row in map.split('\n')]


def makeMoveLeft(map, object):
    if map[object[0]][object[1] - 1] == ".":
        if map[object[0]][object[1]] == "@":
            map[object[0]][object[1]] = "."
            map[object[0]][object[1] - 1] = "@"
            return map, True
        elif map[object[0]][object[1]] == "O":
            map[object[0]][object[1] - 1] = map[object[0]][object[1]]
        else:
            raise Exception("Func called with not @ nor O.")
        return map, True

    if map[object[0]][object[1] - 1] == "#":
        return map, False

    if map[object[0]][object[1] - 1] == "O":
        map, b = makeMoveLeft(map, [object[0], object[1] - 1])
        if b:
            if map[object[0]][object[1]] == "@":
                map[object[0]][object[1]] = "."
                map[object[0]][object[1] - 1] = "@"
                return map, True
            elif map[object[0]][object[1]] == ".":
                map[object[0]][object[1]] = map[object[0]][object[1] + 1]
                map[object[0]][object[1] - 1] = "O"
                return map, True
            elif  map[object[0]][object[1]] == "O":
                return map, True

    return map, False

def makeMoveRight(map, object):
    if map[object[0]][object[1] + 1] == ".":
        if map[object[0]][object[1]] == "@":
            map[object[0]][object[1]] = "."
            map[object[0]][object[1] + 1] = "@"
            return map, True
        elif map[object[0]][object[1]] == "O":
            map[object[0]][object[1] + 1] = map[object[0]][object[1]]
        else:
            raise Exception("Func called with not @ nor O.")
        return map, True

    if map[object[0]][object[1] + 1] == "#":
        return map, False

    if map[object[0]][object[1] + 1] == "O":
        map, b = makeMoveRight(map, [object[0], object[1] + 1])
        if b:
            if map[object[0]][object[1]] == "@":
                map[object[0]][object[1]] = "."
                map[object[0]][object[1] + 1] = "@"
                return map, True
            elif map[object[0]][object[1]] == ".":
                map[object[0]][object[1]] = map[object[0]][object[1] - 1]
                map[object[0]][object[1] + 1] = "O"
                return map, True
            elif  map[object[0]][object[1]] == "O":
                return map, True

    return map, False

def makeMoveUp(map, object):
    if map[object[0] - 1][object[1]] == ".":
        if map[object[0]][object[1]] == "@":
            map[object[0]][object[1]] = "."
            map[object[0] - 1][object[1]] = "@"
            return map, True
        elif map[object[0]][object[1]] == "O":
            map[object[0] - 1][object[1]] = map[object[0]][object[1]]
        else:
            raise Exception("Func called with not @ nor O.")
        return map, True

    if map[object[0] - 1][object[1]] == "#":
        return map, False

    if map[object[0] - 1][object[1]] == "O":
        map, b = makeMoveUp(map, [object[0] - 1, object[1]])
        if b:
            if map[object[0]][object[1]] == "@":
                map[object[0]][object[1]] = "."
                map[object[0] - 1][object[1]] = "@"
                return map, True
            elif map[object[0]][object[1]] == ".":
                map[object[0]][object[1]] = map[object[0] + 1][object[1]]
                map[object[0] - 1][object[1]] = "O"
                return map, True
            elif  map[object[0]][object[1]] == "O":
                return map, True

    return map, False

def makeMoveDown(map, object):
    if map[object[0] + 1][object[1]] == ".":
        if map[object[0]][object[1]] == "@":
            map[object[0]][object[1]] = "."
            map[object[0] + 1][object[1]] = "@"
            return map, True
        elif map[object[0]][object[1]] == "O":
            map[object[0] + 1][object[1]] = map[object[0]][object[1]]
        else:
            raise Exception("Func called with not @ nor O.")
        return map, True

    if map[object[0] + 1][object[1]] == "#":
        return map, False

    if map[object[0] + 1][object[1]] == "O":
        map, b = makeMoveDown(map, [object[0] + 1, object[1]])
        if b:
            if map[object[0]][object[1]] == "@":
                map[object[0]][object[1]] = "."
                map[object[0] + 1][object[1]] = "@"
                return map, True
            elif map[object[0]][object[1]] == ".":
                map[object[0]][object[1]] = map[object[0] - 1][object[1]]
                map[object[0] + 1][object[1]] = "O"
                return map, True
            elif  map[object[0]][object[1]] == "O":
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
    if move == '^':
        map, b = makeMoveUp(map, robot)
        return map
    if move == 'v':
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
prettyPrint(map)

sum = 0
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if map[i][j] == "O":
            sum += i * 100 + j
print(sum)