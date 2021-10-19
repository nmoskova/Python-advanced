def out_of_range(size: int, row: int, col: int):
    return True if row not in range(size) or col not in range(size) else False


word = input()
size = int(input())

field = []
player_position = None
for row in range(size):
    field.append(list(input()))
    for col in range(size):
        if field[row][col] == "P":
            player_position = (row, col)


directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1)
}

for _ in range(int(input())):
    command = input()

    if command not in directions:
        continue
    current_row, current_col = directions[command](player_position[0], player_position[1])

    if out_of_range(size, current_row, current_col):
        if len(word) > 0:
            word = word[:(len(word)-1)]
        continue

    symbol = field[current_row][current_col]
    if symbol.isalpha():
        word += symbol

    field[player_position[0]][player_position[1]] = "-"
    field[current_row][current_col] = "P"
    player_position = (current_row, current_col)

print(word)
[print(''.join(row)) for row in field]

