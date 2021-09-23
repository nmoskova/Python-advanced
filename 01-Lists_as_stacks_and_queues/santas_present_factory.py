from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

count_presents = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}

while materials and magic_level:
    current_material = materials[-1]
    current_magic = magic_level[0]

    multiplication = current_material * current_magic

    if current_material == 0 and current_magic == 0:
        materials.pop()
        magic_level.popleft()
        continue
    elif current_material == 0:
        materials.pop()
    elif current_magic == 0:
        magic_level.popleft()

    if multiplication in presents:
        count_presents[presents[multiplication]] += 1
        materials.pop()
        magic_level.popleft()

    elif multiplication > 0:
        magic_level.popleft()
        materials[-1] += 15

    elif multiplication < 0:
        multiplication = current_material + current_magic
        materials.pop()
        magic_level.popleft()
        materials.append(multiplication)

if (count_presents["Doll"] > 0 and count_presents["Wooden train"] > 0) or \
        (count_presents["Teddy bear"] > 0 and count_presents["Bicycle"] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(m) for m in materials][::-1])}")
if magic_level:
    print(f"Magic left: {', '.join([str(m) for m in magic_level])}")

count_presents = {key: value for (key, value) in count_presents.items() if value > 0}
[print(f"{present}: {count}") for (present, count) in sorted(count_presents.items())]