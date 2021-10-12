rows = int(input())
matrix = []
symbol_found = False

for row in range(rows):
    matrix.append(list(input()))

symbol = input()
for row in range(rows):
    if symbol_found:
        break

    for column in range(rows):
        if matrix[row][column] == symbol:
            symbol_found = True
            print(f"({row}, {column})")
            break

if not symbol_found:
    print(f"{symbol} does not occur in the matrix")