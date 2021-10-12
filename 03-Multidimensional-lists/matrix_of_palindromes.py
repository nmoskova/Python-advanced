rows, columns = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(columns):
        palindrome = chr(97 + row) + chr(97 + row + col) + chr(97 + row)
        matrix[row].append(palindrome)

[print(' '.join(row)) for row in matrix]
