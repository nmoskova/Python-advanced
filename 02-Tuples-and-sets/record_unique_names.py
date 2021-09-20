names_count = int(input())
names = {input() for _ in range(names_count)}

[print(x) for x in names]


