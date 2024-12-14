from functools import lru_cache

def blink(stone):
    num = int(stone)
    str_word = str(num)
    if num == 0:
        return [1]
    elif len(str_word) % 2 == 0:
        mid = len(str_word) // 2
        return [int(str_word[:mid]), int(str_word[mid:])]
    else:
        return [num * 2024]

@lru_cache(None)
def exe(stone, n):
    if n == 0:
        return 1
    length = 0
    for newStone in blink(stone):
        length += exe(newStone, n - 1)
    return length

sum = 0
print("Really proud of this solution :)")
for stone in open('11.txt', 'r').readline().split():
    sum += exe(stone, 75) # 25 for level one
print(sum)