import z3

p1 = 0
for buttons, joltages in map(lambda x: (x[:-1], x[-1]),
                             map(lambda x: [list(map(int, y[1:-1].split(","))) for y in x.split(" ")[1:]],
                                 open("input.txt").read().splitlines())):
    matrix = [[1 if i in buttons[b] else 0 for b in range(len(buttons))] + [joltages[i]] for i in range(len(joltages))]

    opt = z3.Optimize()
    z3buttons = z3.Ints(f"b{i}" for i in range(len(buttons)))

    for eq in matrix:
        opt.add(sum([z3buttons[i] * eq[i] for i in range(len(eq) - 1)]) == eq[-1])

    for btn in z3buttons:
        opt.add(btn >= 0)

    h = opt.minimize(sum(z3buttons))
    opt.check()
    opt.lower(h)
    p1 += opt.model().eval(sum(z3buttons)).as_long()
print(p1)
