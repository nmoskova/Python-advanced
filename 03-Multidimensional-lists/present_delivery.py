def is_index_valid(size: int, row: int, col: int):
    return row in range(size) and col in range(size)


def cookie_generous(matrix: list, directions: dict, row: int, col: int, good_kids_left: int, presents: int):
    for direction, step in directions.items():
        curr_row, curr_col = step(row, col)
        if matrix[curr_row][curr_col] == "C" or matrix[curr_row][curr_col] == "-":
            continue
        elif matrix[curr_row][curr_col] == "V":
            good_kids_left -= 1

        matrix[curr_row][curr_col] = "-"
        presents -= 1
        if presents == 0 or good_kids_left == 0:
            return good_kids_left, presents
    return good_kids_left, presents


presents = int(input())
size = int(input())
matrix = []

good_kids = 0
santa_row, santa_col = 0, 0
for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "S":
            santa_row, santa_col = row, col
        elif matrix[row][col] == "V":
            good_kids += 1


directions = {
    "up": lambda r, c: (r-1, c),
    "down": lambda r, c: (r+1, c),
    "left": lambda r, c: (r, c-1),
    "right": lambda r, c: (r, c+1)
}

good_kids_left = good_kids
current_row, current_col = santa_row, santa_col
while True:
    command = input()
    if command == "Christmas morning":
        break

    matrix[current_row][current_col] = '-'
    current_row, current_col = directions[command](current_row, current_col)
    if not is_index_valid(size, current_row, current_col):
        break

    if matrix[current_row][current_col] == "-":
        continue
    elif matrix[current_row][current_col] == "V":
        good_kids_left -= 1
        presents -= 1
    elif matrix[current_row][current_col] == "C":
        good_kids_left, presents = cookie_generous(matrix, directions, current_row, current_col, good_kids_left, presents)

    if good_kids_left == 0 or presents == 0:
        break


matrix[current_row][current_col] = "S"
if presents == 0 and good_kids_left > 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row)

if good_kids_left == 0:
    print(f"Good job, Santa! {good_kids} happy nice kid/s.")
else:
    print(f"No presents for {good_kids_left} nice kid/s.")