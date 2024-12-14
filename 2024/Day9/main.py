from uaclient.exceptions import InvalidArgChoice

with open("9.txt", 'r') as file:
    input_char_arr = [list(line.rstrip('\n')) for line in file]

level = int(input("which level to run: "))

interpret_as_number = True
string_with_dots = ''
idx = 0
for last_char in input_char_arr[0]:
    if interpret_as_number:
        string_with_dots += str(chr(idx)) * int(last_char)
        idx += 1
    else:
        string_with_dots += chr(50000) * int(last_char)
    interpret_as_number = not interpret_as_number



string_with_dots = string_with_dots.strip(chr(50000))

if level == 1:
    while string_with_dots.find(chr(50000)) != -1:
        dot_idx = string_with_dots.find(chr(50000))
        last_char = string_with_dots[-1]
        string_with_dots = string_with_dots[:dot_idx] + str(last_char) + string_with_dots[dot_idx+1:]
        string_with_dots = string_with_dots[:-1]
elif level == 2:
    for idx in reversed(range(ord(string_with_dots[-1]) + 1)):
        length = string_with_dots.count(chr(idx))
        free_space_idx = string_with_dots.find(str(chr(50000)) * length)
        current_index = string_with_dots.find(chr(idx))

        if free_space_idx == -1 or free_space_idx > current_index:
            continue

        string_before_free_space = string_with_dots[:free_space_idx]
        string_after_free_space = string_with_dots[free_space_idx + length:]

        string_before_current_index = string_with_dots[:current_index]
        string_after_current_index = string_with_dots[current_index + length:]

        string_with_dots = string_before_free_space + str(chr(idx)) * length + string_after_free_space
        string_with_dots = string_with_dots[:current_index] + str(chr(50000)) * length + string_with_dots[current_index + length:]
        string_with_dots = string_with_dots.strip(chr(50000))
else:
    raise InvalidArgChoice


sum = 0
for i in range(len(string_with_dots)):
    if ord(string_with_dots[i]) == 50000:
        continue
    sum += i * int(ord(string_with_dots[i]))

print(sum)