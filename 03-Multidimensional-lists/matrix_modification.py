def check_index(row: int, col: int):
    if row in range(len(matrix)) and col in range(len(matrix)):
        return True

    print("Invalid coordinates")
    return False


rows = int(input())
matrix = []
valid_index = False

for row in range(rows):
    matrix.append([int(n) for n in input().split()])


while True:
    command = input()
    if command == "END":
        break

    command = [int(el) if el.isnumeric() else el for el in command.split()]
    action, row, col, value = command
    valid_index = check_index(row, col)
    if not valid_index:
        continue

    if action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value

for row in matrix:
    print(' '.join([str(el) for el in row]))