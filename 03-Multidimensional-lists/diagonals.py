rows = int(input())
matrix = []

primary_diagonal = {"sum": 0, "elements": []}
secondary_diagonal = {"sum": 0, "elements": []}

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

for row in range(rows):
    el_primary = matrix[row][row]
    primary_diagonal["sum"] += el_primary
    primary_diagonal["elements"].append(el_primary)
    el_secondary = matrix[row][rows - row - 1]
    secondary_diagonal["sum"] += el_secondary
    secondary_diagonal["elements"].append(el_secondary)

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal['elements']])}. Sum: {primary_diagonal['sum']}\n\
Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal['elements']])}. Sum: {secondary_diagonal['sum']}")