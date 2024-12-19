from functools import cache

c = open("19.txt", 'r').read()
blocks = c.split("\n\n")
possible_colors = [p.strip("\n") for p in blocks[0].split(", ")]
towels = blocks[1].split("\n")
max_strip_length = 0

for x in possible_colors:
    max_strip_length = max(max_strip_length, len(x))

@cache
def isPossible(towel):
    if towel == "": return 1
    result = 0
    for p in possible_colors:
        if not towel.startswith(p): continue
        after = towel[len(p):]
        result += isPossible(after)
    return result

sum1 = 0
sum2 = 0
for towel in towels:
    r = isPossible(towel)
    if r > 0:
        sum1 += 1
    sum2 += r
print("Part 1: " + str(sum1))
print("Part 2: " + str(sum2))