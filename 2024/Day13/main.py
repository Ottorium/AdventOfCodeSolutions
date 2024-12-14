with open('13.txt', 'r') as file:
    texts = file.read().split('\n\n')
list_of_buttons = []

def parse(current): # this can be done so much easier with regex, but i don't care, i was in a hurry and im not that good with regex :)
    lines = current.split('\n')
    vs = lines[0].split(':')[1].strip().split(", ")
    x_value = int(vs[0].split("+")[1])
    y_value = int(vs[1].split("+")[1])
    buttonA = {"x": x_value, "y": y_value}
    vs = lines[1].split(':')[1].strip().split(", ")
    x_value = int(vs[0].split("+")[1])
    y_value = int(vs[1].split("+")[1])
    buttonB = {"x": x_value, "y": y_value}
    vs = lines[2].split(':')[1].strip().split(", ")
    x_value = int(vs[0].split("=")[1]) + 10000000000000
    y_value = int(vs[1].split("=")[1]) + 10000000000000
    prize = {"x": x_value, "y": y_value}
    return buttonA, buttonB, prize

def press(current, button):
    current["x"] += button["x"]
    current["y"] += button["y"]


s = 0
rs = 0
print("for level 1, delete the + 10000000000000 in lines 16 and 17")
for current in texts:
    buttonA, buttonB, prize = parse(current)
    current = {"x": 0, "y": 0}

    ax = buttonA["x"]
    bx = buttonB["x"]
    px = prize["x"]
    ay = buttonA["y"]
    by = buttonB["y"]
    py = prize["y"]

    if (ax % bx == 0 or bx % ax == 0) and (ay % by == 0 or by % ay == 0):
        pass

    a = (px*by-py*bx)/(by*ax-ay*bx)

    b = (px*ay-py*ax)/(ay*bx-ax*by)

    tokens = a * 3 + b
    if a % 1 == 0 and b % 1 == 0:
        rs += 1
        s += int(tokens)

print(s)