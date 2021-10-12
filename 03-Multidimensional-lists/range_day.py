def valid_index(field: list, row: int, col: int):
    return row in range(len(field)) and col in range(len(field))


def move_command(field: list, direction: str, steps: int, row: int, col: int):
    current_row, current_col = row, col
    if direction == "up":
        current_row = row - steps
    elif direction == "down":
        current_row = row + steps
    elif direction == "left":
        current_col = col - steps
    elif direction == "right":
        current_col = col + steps

    if valid_index(field, current_row, current_col) and field[current_row][current_col] == ".":
        return current_row, current_col

    return row, col


def shoot_command(field: list, direction: str, row: int, col: int, current_targets: int):
    current_row, current_col = row, col

    while True:
        if direction == "up":
            current_row -= 1
        elif direction == "down":
            current_row += 1
        elif direction == "left":
            current_col -= 1
        elif direction == "right":
            current_col += 1

        if not valid_index(field, current_row, current_col):
            return current_targets

        if field[current_row][current_col] == "x":
            current_targets -= 1
            field[current_row][current_col] = "."
            targets_shot_position.append([current_row, current_col])
            return current_targets


size = 5
field = []

targets_count = 0
position_row, position_col = 0, 0
for row in range(size):
    field.append(input().split())
    for col in range(size):
        if field[row][col] == "A":
            position_row, position_col = row, col
        elif field[row][col] == "x":
            targets_count += 1

targets_shot_position = []
current_row, current_col, current_targets = position_row, position_col, targets_count

commands_count = int(input())
for _ in range(commands_count):
    command = input().split()
    direction = command[1]

    if command[0] == "move":
        steps = int(command[2])
        current_row, current_col = move_command(field, direction, steps, current_row, current_col)

    elif command[0] == "shoot":
        current_targets = shoot_command(field, direction, current_row, current_col, current_targets)

    if current_targets == 0:
        break

if current_targets == 0:
    print(f"Training completed! All {targets_count} targets hit.")
else:
    print(f"Training not completed! {current_targets} targets left.")

for target_position in targets_shot_position:
    print(target_position)