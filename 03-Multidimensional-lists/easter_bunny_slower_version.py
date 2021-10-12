def check_possible_ways(matrix: list, row: int, col: int):

    possible_ways = {
        'up': {'value': float('-inf'), 'position': []},
        'down': {'value': float('-inf'), 'position': []},
        'left': {'value': float('-inf'), 'position': []},
        'right': {'value': float('-inf'), 'position': []},
    }

    up_sum = 0
    for r in range(row - 1, -1, -1):
        if matrix[r][col] == "X":
            break
        up_sum += matrix[r][col]
        possible_ways['up']['value'] = up_sum
        possible_ways['up']['position'].append([r, col])

    down_sum = 0
    for r in range(row + 1, rows):
        if matrix[r][col] == "X":
            break
        down_sum += matrix[r][col]
        possible_ways['down']['value'] = down_sum
        possible_ways['down']['position'].append([r, col])

    left_sum = 0
    for c in range(col - 1, -1, -1):
        if matrix[row][c] == "X":
            break
        left_sum += matrix[row][c]
        possible_ways['left']['value'] = left_sum
        possible_ways['left']['position'].append([row, c])

    right_sum = 0
    for c in range(col + 1, rows):
        if matrix[row][c] == "X":
            break
        right_sum += matrix[row][c]
        possible_ways['right']['value'] = right_sum
        possible_ways['right']['position'].append([row, c])

    return possible_ways


rows = int(input())
matrix = []
bunny_position = None

for row in range(rows):
    matrix.append([el if el.isalpha() else int(el) for el in input().split()])
    for col in range(rows):
        el = matrix[row][col]
        if el == "B":
            bunny_position = (row, col)

possible_ways = check_possible_ways(matrix, bunny_position[0], bunny_position[1])

for direction, value in sorted(possible_ways.items(), key=lambda x: (-x[1]['value'])):
    print(direction)
    for v in possible_ways[direction]['position']:
        print(v)
    print(possible_ways[direction]["value"])
    break
