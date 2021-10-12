rows = int(input())
matrix_even = []

for row_index in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix_even.append([n for n in row if n % 2 == 0])

print(matrix_even)