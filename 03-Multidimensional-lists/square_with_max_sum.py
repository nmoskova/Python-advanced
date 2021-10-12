rows, columns = [int(x) for x in input().split(", ")]
matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

max_sum = 0
position = None
for row in range(rows-1, 0, -1):
    for col in range(columns-1, 0, -1):
        sum_numbers = matrix[row][col] + matrix[row][col-1] +\
            matrix[row-1][col] + matrix[row-1][col-1]
        if sum_numbers >= max_sum:
            max_sum = sum_numbers
            position = (row, col)

row = position[0]
col = position[1]
print(f"{matrix[row-1][col-1]} {matrix[row-1][col]}\n{matrix[row][col-1]} {matrix[row][col]}")
print(max_sum)