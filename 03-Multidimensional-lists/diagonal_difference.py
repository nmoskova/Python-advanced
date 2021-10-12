rows = int(input())
matrix = []

diagonals_sum = {"primary": 0, "secondary": 0}

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows):
    el_primary = matrix[row][row]
    diagonals_sum["primary"] += el_primary
    el_secondary = matrix[row][rows - row - 1]
    diagonals_sum["secondary"] += el_secondary

print(abs(diagonals_sum['primary'] - diagonals_sum['secondary']))
