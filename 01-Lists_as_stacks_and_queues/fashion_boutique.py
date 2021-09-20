clothes = [int(x) for x in input().split()]
max_capacity = int(input())
racks = 1
capacity = max_capacity

while clothes:
    current_clothing = clothes.pop()

    if current_clothing > capacity:
        capacity = max_capacity
        capacity -= current_clothing
        racks += 1

    else:
        capacity -= current_clothing

print(racks)
