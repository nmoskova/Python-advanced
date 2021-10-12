rows, columns = [int(x) for x in input().split()]
matrix = []
equal_elements = 0

for _ in range(rows):
    matrix.append([x for x in input().split()])

for row in range(rows - 1):
    for col in range(columns - 1):
        first_el = matrix[row][col]
        second_el = matrix[row+1][col]
        third_el = matrix[row][col+1]
        fourth_el = matrix[row+1][col+1]
        if first_el == second_el == third_el == fourth_el:
            equal_elements += 1

print(equal_elements)