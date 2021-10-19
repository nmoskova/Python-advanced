def check_path_range(size: int, position: tuple):
    row, col = position[0], position[1]
    return row in range(size) and col in range(size)


size = int(input())
field = []

player_position = None
for row in range(size):
    field.append([x for x in input().split()])
    for col in range(size):
        if field[row][col] == "P":
            player_position = (row, col)

directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1)
}

coins = 0
player_path = []
while True:
    command = input()

    if command not in directions:
        continue

    current_row, current_col = player_position[0], player_position[1]
    player_position = directions[command](current_row, current_col)

    if not check_path_range(size, player_position) or field[player_position[0]][player_position[1]] == "X":
        coins //= 2
        break

    player_path.append(player_position)
    coins += int(field[player_position[0]][player_position[1]])

    if coins >= 100:
        break

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")
for position in player_path:
    print(f"[{position[0]}, {position[1]}]")



