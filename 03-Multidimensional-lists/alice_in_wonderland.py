def get_position(command: str, row: int, col: int):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1


def check_valid_index(next_row, next_col, size):
    return next_row in range(size) and next_col in range(size)


size = int(input())
matrix = []

alice_row, alice_col = 0, 0
for r in range(size):
    matrix.append(input().split())
    for c in range(size):
        if matrix[r][c] == "A":
            alice_row,  alice_col = r, c
            matrix[alice_row][alice_col] = '*'

alice_collected_enough_tea = False
tea = 0
current_row, current_col = alice_row, alice_col
while True:
    command = input()

    current_row, current_col = get_position(command, current_row, current_col)

    if not check_valid_index(current_row, current_col, size):
        break

    if matrix[current_row][current_col] == "R":
        matrix[current_row][current_col] = "*"
        break
    elif matrix[current_row][current_col] == ".":
        matrix[current_row][current_col] = "*"
        continue
    elif matrix[current_row][current_col] == "*":
        continue
    else:
        tea += int(matrix[current_row][current_col])
        matrix[current_row][current_col] = "*"

    if tea >= 10:
        alice_collected_enough_tea = True
        break

if alice_collected_enough_tea:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(' '.join(row)) for row in matrix]