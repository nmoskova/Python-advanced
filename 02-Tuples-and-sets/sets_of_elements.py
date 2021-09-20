n, m = input().split()
n, m = int(n), int(m)

first_set = {input() for _ in range(n)}
second_set = {input() for _ in range(m)}

unique_set = first_set.intersection(second_set)
[print(el) for el in unique_set]