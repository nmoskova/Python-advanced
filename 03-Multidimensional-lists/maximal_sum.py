import sys
rows, columns = [int(x) for x in input().split()]
matrix = []
maximal_sum = -sys.maxsize
position = None

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows - 2):
    for col in range(columns - 2):
        elements_sum = matrix[row][col] + matrix[row][col+1] + matrix[row][col+2] +\
            matrix[row+1][col] + matrix[row+1][col+1] + matrix[row+1][col+2] +\
            matrix[row+2][col] + matrix[row+2][col+1] + matrix[row+2][col+2]
        if elements_sum > maximal_sum:
            maximal_sum = elements_sum
            position = (row, col)

row = position[0]
col = position[1]

print(f"Sum = {maximal_sum}")
print(f"{matrix[row][col]} {matrix[row][col+1]} {matrix[row][col+2]}\n\
{matrix[row+1][col]} {matrix[row+1][col+1]} {matrix[row+1][col+2]}\n\
{matrix[row+2][col]} {matrix[row+2][col+1]} {matrix[row+2][col+2]}")