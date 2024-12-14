with open('12.txt', 'r') as file:
    garden = [list(line.rstrip('\n')) for line in file]


def get_adjacents(garden, region_point):
    rows, cols = len(garden), len(garden[0])
    target_letter = garden[region_point[0]][region_point[1]]
    adjacents = []

    if region_point[0] > 0 and garden[region_point[0] - 1][region_point[1]] == target_letter:
        adjacents.append([region_point[0] - 1, region_point[1]])

    if region_point[0] < rows - 1 and garden[region_point[0] + 1][region_point[1]] == target_letter:
        adjacents.append([region_point[0] + 1, region_point[1]])

    if region_point[1] > 0 and garden[region_point[0]][region_point[1] - 1] == target_letter:
        adjacents.append([region_point[0], region_point[1] - 1])

    if region_point[1] < cols - 1 and garden[region_point[0]][region_point[1] + 1] == target_letter:
        adjacents.append([region_point[0], region_point[1] + 1])

    return adjacents


def getRegion(garden, region_point, coming_from_point, seen):
    if region_point in seen:
        return 1

    seen.append(region_point)
    adjacent = get_adjacents(garden, region_point)

    if coming_from_point in adjacent:
        adjacent.remove(coming_from_point)

    if not adjacent:
        return 1

    region_size = 1
    for next_point in adjacent:
        if next_point in seen:
            continue
        region_size += getRegion(garden, next_point, region_point, seen)

    return region_size

def getRegionAllIdxs(garden, region_point, coming_from_point, seen):
    if region_point in seen:
        return [region_point]

    seen.append(region_point)
    adjacent = get_adjacents(garden, region_point)

    if coming_from_point in adjacent:
        adjacent.remove(coming_from_point)

    if not adjacent:
        return [region_point]

    regions = list()
    for next_point in adjacent:
        if next_point in seen:
            continue
        rs = getRegionAllIdxs(garden, next_point, region_point, seen)
        for r in rs:
            regions.append(r)
    regions.append(region_point)

    return regions



def getFenceCount(garden, region_point, seen=None):

    if seen is None:
        seen = set()

    if tuple(region_point) in seen:
        return 0

    rows, cols = len(garden), len(garden[0])
    target_letter = garden[region_point[0]][region_point[1]]
    fence_count = 0

    seen.add(tuple(region_point))

    if region_point[0] == 0:
        fence_count += 1
    elif garden[region_point[0] - 1][region_point[1]] != target_letter:
        fence_count += 1

    if region_point[0] == rows - 1:
        fence_count += 1
    elif garden[region_point[0] + 1][region_point[1]] != target_letter:
        fence_count += 1

    if region_point[1] == 0:
        fence_count += 1
    elif garden[region_point[0]][region_point[1] - 1] != target_letter:
        fence_count += 1

    if region_point[1] == cols - 1:
        fence_count += 1
    elif garden[region_point[0]][region_point[1] + 1] != target_letter:
        fence_count += 1

    adj = []
    directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]
    for dx, dy in directions:
        new_row = region_point[0] + dx
        new_col = region_point[1] + dy

        if (0 <= new_row < rows and 0 <= new_col < cols and
                garden[new_row][new_col] == target_letter):
            adj.append([new_row, new_col])

    for next_point in adj:
        if tuple(next_point) not in seen:
            fence_count += getFenceCount(garden, next_point, seen)

    return fence_count


def getNumberOfSides(garden, region):
    fulllist = list()
    plantsOfOneSort = getRegionAllIdxs(garden, region, None, list())
    for plant in plantsOfOneSort:
        if [plant[0], plant[1] - 1] not in plantsOfOneSort:
            fulllist.append([plant[0], plant[1] - 1, "l"])

        if [plant[0], plant[1] + 1] not in plantsOfOneSort:
            fulllist.append([plant[0], plant[1] + 1, "r"])

        if [plant[0] - 1, plant[1]] not in plantsOfOneSort:
            fulllist.append([plant[0] - 1, plant[1], "t"])

        if [plant[0] + 1, plant[1]] not in plantsOfOneSort:
            fulllist.append([plant[0] + 1, plant[1], "b"])

    fulllist.sort()
    removeThese = []
    for i, edge in enumerate(fulllist):
        for j in range(i, len(fulllist)):
            secondEdge = fulllist[j]
            if edge[0] == secondEdge[0] and abs(edge[1] - secondEdge[1]) == 1 and edge[2] == secondEdge[2]:
                removeThese.append(edge)

            elif edge[1] == secondEdge[1] and abs(edge[0] - secondEdge[0]) == 1 and edge[2] == secondEdge[2]:
                removeThese.append(edge)

    for rt in removeThese:
        if rt in fulllist:
            fulllist.remove(rt)

    return len(fulllist)


def getPriceLevel2(garden, region, comingFromPoint, seen):
    regionCount = getRegion(garden, region, comingFromPoint, seen)
    numberOfSides = getNumberOfSides(garden, region)
    return regionCount * numberOfSides

def getPriceLevel1(garden, region, comingFromPoint, seen):
    regionCount = getRegion(garden, region, comingFromPoint, seen)
    fenceCount = getFenceCount(garden, region)
    return regionCount * fenceCount



seen = list()
sum = 0
beforeBuffer = None
level = int(input("which level: "))
for i in range(len(garden)):
    for j in range(len(garden[i])):
        current = [i, j]
        if current in seen:
            continue
        if level == 1:
            price = getPriceLevel1(garden, current, beforeBuffer, seen)
        else:
            price = getPriceLevel2(garden, current, beforeBuffer, seen)

        sum += price
        beforeBuffer = current
print(sum)
