rows, columns = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

while True:
    command = input()
    if command == "END":
        break
    valid_command = False

    if command.startswith("swap") and len(command.split()[1:]) == 4:
        row_1, col_1, row_2, col_2 = (int(x) for x in command.split()[1:])
        if row_1 in range(rows) and row_2 in range(rows) and col_2 in range(columns) and col_2 in range(columns):
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            valid_command = True

    print("Invalid input!") if not valid_command else [print(' '.join(row)) for row in matrix]
