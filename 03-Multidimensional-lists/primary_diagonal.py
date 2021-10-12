rows = int(input())
matrix = []

diagonal_sum = 0
for row in range(rows):
    matrix.append([int(el) for el in input().split()])
    diagonal_sum += matrix[row][row]

print(diagonal_sum)