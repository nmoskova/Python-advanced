def get_magic_triangle(n: int):
    triangle = []
    for row in range(n):
        triangle.append([])
        for col in range(row + 1):

            el = None
            if col == 0 or col == row:
                el = 1
            else:
                el = triangle[row-1][col-1] + triangle[row-1][col]

            triangle[row].append(el)

    return triangle


get_magic_triangle(5)