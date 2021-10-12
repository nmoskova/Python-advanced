rows, columns = [int(x) for x in input().split()]
word = input()
matrix = []
word_i = 0

for row in range(rows):
    matrix.append([None] * columns)
    for column in range(columns):
        if row % 2 == 0:
            matrix[row][column] = word[word_i]
        else:
            matrix[row][columns - 1 - column] = word[word_i]
        word_i = (word_i + 1) % len(word)

[print(''.join(row)) for row in matrix]