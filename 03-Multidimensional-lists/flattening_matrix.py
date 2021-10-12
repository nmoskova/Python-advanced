rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(n) for n in input().split(", ")])

print(matrix)