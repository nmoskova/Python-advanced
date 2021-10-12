def is_knight_removed(matrix: list, row: int, col: int):
    if row not in range(rows) or col not in range(rows):
        return False
    return matrix[row][col] == "K"


def affected_knights(matrix: list, row: int, col: int):
    result = 0
    if is_knight_removed(matrix, row - 2, col + 1):
        result += 1
    if is_knight_removed(matrix, row - 1, col + 2):
        result += 1
    if is_knight_removed(matrix, row + 1, col + 2):
        result += 1
    if is_knight_removed(matrix, row + 2, col + 1):
        result += 1
    if is_knight_removed(matrix, row + 2 , col - 1):
        result += 1
    if is_knight_removed(matrix, row + 1, col - 2):
        result += 1
    if is_knight_removed(matrix, row - 1, col - 2):
        result += 1
    if is_knight_removed(matrix, row - 2, col - 1):
        result += 1
    return result


rows = int(input())
matrix = []
knights_removed = 0

for row in range(rows):
    matrix.append(list(input()))

while True:
    pass

    max_knights_removed, row_knight, col_knight = 0, 0, 0

    for row in range(rows):
        for col in range(rows):

            if matrix[row][col] == "0":
                continue

            elif matrix[row][col] == "K":
                removed_knights = affected_knights(matrix, row, col)
                if removed_knights > max_knights_removed:
                    max_knights_removed, row_knight, col_knight = removed_knights, row, col

    if max_knights_removed == 0:
        break
    matrix[row_knight][col_knight] = "0"
    knights_removed += 1

print(knights_removed)

