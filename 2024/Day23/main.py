from copy import deepcopy

connections = list()
computers = list()
for line in open('23.txt').readlines():
    line = line.strip()
    values = line.split("-")
    values.sort()
    connections.append(values)
    computers.append(values[0])
    computers.append(values[1])

map = dict()
for l, r in connections:
    if l not in map.keys(): map[l] = list()
    if r not in map.keys(): map[r] = list()
    map[l].append(r)
    map[r].append(l)

s = 0
three_way_connections = set()
for current in map.keys():
    for i in map[current]:
        for j in map[i]:
            for k in map[j]:
                if k == current:
                    three_way_connections.add(tuple(sorted((current, i, j))))

with_t = set()
for twc in three_way_connections:
    for t in twc:
        if t.startswith("t"):
            with_t.add(twc)
print("Part 1: " + str(len(with_t)))


def is_connected_to_all_computers_in_lan_party(computer, lan_party):
    if computer in lan_party: return False
    needed_connections = list()
    for other in lan_party:
        c = [computer, other]
        c.sort()
        needed_connections.append(c)
    for nc in needed_connections:
        if nc not in connections: return False
    return True

def pretty_string(lp):
    r = ""
    for computer in lp:
        r += computer + ","
    r = r[:-1]
    return r

biggest_lan_party = []
for i, v in enumerate(connections):
    l, r = v
    #print(str(i) + " out of " + str(len(connections)) + " biggest: " + str(pretty_string(biggest_lan_party)))
    lan_party = [l, r]
    while True:
        for computer in computers:
            if is_connected_to_all_computers_in_lan_party(computer, lan_party):
                lan_party.append(computer)
                break
        else:
            break

    if len(lan_party) > len(biggest_lan_party):
        biggest_lan_party = deepcopy(lan_party)
        biggest_lan_party.sort()

print("Part 2: " + str(pretty_string(biggest_lan_party)))