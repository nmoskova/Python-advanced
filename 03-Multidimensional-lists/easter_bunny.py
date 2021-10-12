def check_best_ways(matrix: list, row: int, col: int):
    direction_up = float('-inf')
    position_direction_up = []
    up_sum = 0
    for r in range(row - 1, -1, -1):
        if matrix[r][col] == "X":
            break
        up_sum += matrix[r][col]
        direction_up = up_sum
        position_direction_up.append([r, col])

    direction_down = float('-inf')
    position_direction_down = []
    down_sum = 0
    for r in range(row + 1, rows):
        if matrix[r][col] == "X":
            break
        down_sum += matrix[r][col]
        direction_down = down_sum
        position_direction_down.append([r, col])

    direction_left = float('-inf')
    left_sum = 0
    position_direction_left = []
    for c in range(col - 1, -1, -1):
        if matrix[row][c] == "X":
            break
        left_sum += matrix[row][c]
        direction_left = left_sum
        position_direction_left.append([row, c])

    direction_right = float('-inf')
    right_sum = 0
    position_direction_right = []
    for c in range(col + 1, rows):
        if matrix[row][c] == "X":
            break
        right_sum += matrix[row][c]
        direction_right = right_sum
        position_direction_right.append([row, c])

    best_way = max(direction_up, direction_down, direction_left, direction_right)

    if best_way == direction_up:
        return {"up": {"value": direction_up, "position": position_direction_up}}
    elif best_way == direction_down:
        return {"down": {"value": direction_down, "position": position_direction_down}}
    elif best_way == direction_left:
        return {"left": {"value": direction_left, "position": position_direction_left}}
    elif best_way == direction_right:
        return {"right": {"value": direction_right, "position": position_direction_right}}


rows = int(input())
matrix = []
bunny_position = None

for row in range(rows):
    matrix.append([el if el.isalpha() else int(el) for el in input().split()])
    for col in range(rows):
        el = matrix[row][col]
        if el == "B":
            bunny_position = (row, col)

best_way = check_best_ways(matrix, bunny_position[0], bunny_position[1])

for key, value in best_way.items():
    print(key)
    for v in best_way[key]["position"]:
        print(v)
    print(best_way[key]["value"])