print("This might take a while")
all_results = list()
s1 = 0
for line in open("22.txt", "r").readlines():
    line = line.strip("\n")
    num = int(line)
    this_element = list()
    this_element.append([num % 10, None])
    prev = num
    for _ in range(2000):
        num = ((num << 6) ^ num) % 16777216
        num = ((num >> 5) ^ num) % 16777216
        num = ((num << 11) ^ num) % 16777216
        this_element.append([num % 10, num % 10 - prev % 10])
        prev = num
    s1 += num
    all_results.append(this_element)
print("Part 1: " + str(s1))

all_seq_bananas = list()
for result in all_results:
    curr_seq = list()
    for i, r in enumerate(result[4:], start=4):
        seq = str(str(result[i - 3][1]) + str(result[i - 2][1]) + str(result[i - 1][1]) + str(r[1]))
        if seq in curr_seq: continue
        curr_seq.append(seq)
        bananas = r[0]
        all_seq_bananas.append((seq, bananas))

all_seq_bananas.sort(key=lambda x: x[0])

before_buffer = None
maximum_bananas = 0
bananas = 0
for x in all_seq_bananas:
    cs = x[0]
    if before_buffer != cs:
        bananas = 0
    bananas += x[1]
    maximum_bananas = max(maximum_bananas, bananas)
    before_buffer = cs
print("Part 2: " + str(maximum_bananas))
