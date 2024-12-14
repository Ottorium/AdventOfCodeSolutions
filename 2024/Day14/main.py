list_of_postitions = []
list_of_vels = []
for thing in open("14.txt", "r").read().split("\n"):
    things = thing.split("=")
    list_of_postitions.append(things[1].strip("v").strip().split(","))
    list_of_vels.append(things[2].strip().split(","))
for i in range(len(list_of_postitions)):
    list_of_postitions[i][0] = int(list_of_postitions[i][0])
    list_of_postitions[i][1] = int(list_of_postitions[i][1])
    list_of_vels[i][0] = int(list_of_vels[i][0])
    list_of_vels[i][1] = int(list_of_vels[i][1])


def normalizePosition(pos, width, height):
    px, py = pos
    while px < 0:
        px += width
    while py < 0:
        py += height
    while px >= width:
        px -= width
    while py >= height:
        py -= height
    return [px, py]

def updatePosition(pos, vel, width, height):
    px, py = normalizePosition(pos, width, height)
    vx, vy = vel
    px += vx
    py += vy
    return normalizePosition([px, py], width, height)


def getSafetyFactor(list_of_postitions, width, height):
    heightMid = (height - 1) / 2
    widthMid = (width - 1) / 2
    q1, q2, q3, q4 = 0, 0, 0, 0

    for pos in list_of_postitions:
        px, py = normalizePosition(pos, width, height)
        if px == widthMid:
            continue
        if py == heightMid:
            continue

        # q1
        if px < widthMid and py < heightMid:
            q1 += 1

        # q2
        if px > widthMid and py < heightMid:
            q2 += 1

        # q3
        if px > widthMid and py > heightMid:
            q3 += 1

        # q4
        if px < widthMid and py > heightMid:
            q4 += 1

    #print(q1, q2, q3, q4)
    return q1 * q2 * q3 * q4

def prettyPrint(list_of_postitions, width, height):
    char_array = [['.' for _ in range(width)] for _ in range(height)]

    for pos in list_of_postitions:
        px, py = normalizePosition(pos, width, height)
        char_array[py][px] = "x"



    for i in char_array:
        for j in i:
            print(j, end="")
        print()


width = 101
height = 103
new_poss = []
for i in range(1, 100):
    new_poss = []
    for j, pos in enumerate(list_of_postitions):
        u = updatePosition(pos, list_of_vels[j], width, height)
        new_poss.append(u)
    list_of_postitions = new_poss

    # For part two, let the loop run for longer and look through  the pictures
    prettyPrint(list_of_postitions, width, height)
    print()

sf = getSafetyFactor(list_of_postitions, width, height)
print("Part 1: " + str(sf))
print("""How I solved Part 2: I tried a lot of things. But eventually, I decided to do it manually:
    - I binary searched for the answer on the website. 
    - I got a range from 5000 to 10000 from that but then it stopped giving me outputs if the number is too high or too low (this is generally a good thing). 
    - I searched through the pictures manually from 5000 on. My answer was around 7000. 

I have no idea how this would be solvable with code, as the picture doesn't even fill out the whole map and there are other robots running around outside of the christmas tree. 
Part 2 is a TERRIBLE problem.
""")