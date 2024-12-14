from itertools import count
import re

with open('7.txt', 'r') as file:
    lines = file.readlines()


def evaluate(splitted, signs):
    assert len(splitted) == len(signs) + 1

    result = int(splitted[0])

    for i in range(len(signs)):
        if signs[i] == "+":
            result += int(splitted[i + 1])
        elif signs[i] == "*":
            result *= int(splitted[i + 1])
        elif signs[i] == "":
            result = int(str(result) + str(splitted[i + 1]))
        else:
            raise ValueError(f"Unsupported operator: {signs[i]}")
    return result


def int_to_symbol_array(n, length):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    base3_string = ""
    while n > 0:
        base3_string = str(n % 3) + base3_string
        n //= 3

    base3_string = base3_string.zfill(length)

    if len(base3_string) > length:
        raise ValueError(f"Length too small to represent the number in base 3")

    return [
        "" if digit == "0" else
        "+" if digit == "1" else
        "*"
        for digit in base3_string
    ]


def isPossible(result, splitted):
    count = 0
    while True:
        try:
            signs = int_to_symbol_array(count, len(splitted) - 1)
        except ValueError:
            return False
        actualResult = evaluate(splitted, signs)
        if actualResult == result:
            return True
        count += 1


sum = 0
print("Sadly I deleted the code for part 1. Here is part 2. This might take a while.")
for line in lines:
    splitted = line.split(": ")
    result = splitted[0]
    splitted.remove(result)
    result = int(result)

    splitted[0] = splitted[0].strip()
    splitted[-1] = splitted[-1].strip("\n")

    splitted = splitted[0].split(" ")

    if isPossible(result, splitted):
        sum += result
print(sum)
