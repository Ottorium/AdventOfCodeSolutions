blocks = open("24.txt").read().split("\n\n")

wires = dict()
for x in blocks[0].split("\n"):
    w, v = x.split(": ")
    wires[w] = int(v)

instructions = list()
for instruction in blocks[1].split("\n"):
    equ = instruction.split(" -> ")
    write_to = equ[1]
    calculation = equ[0].split(" ")
    x = calculation[0]
    operand = calculation[1]
    y = calculation[2]
    instructions.append((x, operand, y, write_to))

for x, operand, y, write_to in instructions:
    try:
        if operand == "AND":
            result = wires[x] & wires[y]
        elif operand == "OR":
            result = wires[x] | wires[y]
        elif operand == "XOR":
            result = wires[x] ^ wires[y]
        else:
            raise Exception("Unknown operand " + operand)
    except KeyError:
        instructions.append((x, operand, y, write_to))
        continue
    wires[write_to] = result

zeds = dict()
for w in wires:
    v = wires[w]
    if w.startswith("z"):
        zeds[int(w[1:])] = v

sorted_ = reversed([zeds[key] for key in sorted(zeds)])

r = ""
for s in sorted_:
    r += str(s)
number = int(r, 2)

print("Part 1: " + str(number))
print("I wasn't able to solve Part 2.'")
