
def find_all_antennas(char_array):
    antennas = []
    for row in range(len(char_array)):
        for col in range(len(char_array[row])):
            if char_array[row][col] not in '.#':
                antennas.append((row, col))
    return antennas


def find_given_antenna(char_array_2_d, target_char):
    indexes = []
    for row in range(len(char_array_2_d)):
        for col in range(len(char_array_2_d[row])):
            if char_array_2_d[row][col] == target_char:
                indexes.append((row, col))
    return indexes



with open("8.txt", 'r') as file:
    input_char_arr = [list(line.rstrip('\n')) for line in file]
unique_positions = set()
for antenna in find_all_antennas(input_char_arr):
    unique_positions.add(antenna)
    others = find_given_antenna(input_char_arr, input_char_arr[antenna[0]][antenna[1]])
    for other in others:
        if other[0] is antenna[0] and other[1] is antenna[1]:
            continue
        modifiable_antenna = antenna
        modifiable_other = other
        while True:
            row_diff = modifiable_antenna[0] - modifiable_other[0]
            col_diff = modifiable_antenna[1] - modifiable_other[1]
            row_write_idx = modifiable_antenna[0] + row_diff
            col_write_idx = modifiable_antenna[1] + col_diff

            if row_write_idx < 0 or col_write_idx < 0:
                break

            try:
                if input_char_arr[row_write_idx][col_write_idx] == "#":
                    pass
                elif input_char_arr[row_write_idx][col_write_idx] == ".":
                    input_char_arr[row_write_idx][col_write_idx] = '#'
                    unique_positions.add((row_write_idx, col_write_idx))
                else:
                    unique_positions.add((row_write_idx, col_write_idx))
            except IndexError:
                break

            modifiable_other = (modifiable_antenna[0], modifiable_antenna[1])
            modifiable_antenna = (row_write_idx, col_write_idx)


print("Sadly I deleted the code for part 1. Here is part 2.")
print(len(unique_positions))