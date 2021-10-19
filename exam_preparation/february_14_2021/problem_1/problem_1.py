from collections import deque

explosives = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

division = {
    "divisible_by_three": lambda total: total % 3 == 0,
    "divisible_by_five": lambda total: total % 5 == 0
}

firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

while firework_effects and explosive_power:
    if all([True if value >= 3 else False for value in explosives.values()]):
        break

    firework = firework_effects[0]
    explosive = explosive_power[-1]

    if firework <= 0:
        firework_effects.popleft()
        continue

    if explosive <= 0:
        explosive_power.pop()
        continue

    total = firework + explosive

    divisible_by_three = division["divisible_by_three"](total)
    divisible_by_five = division["divisible_by_five"](total)

    if divisible_by_three and divisible_by_five:
        explosives["Crossette Fireworks"] += 1
    elif divisible_by_three and not divisible_by_five:
        explosives["Palm Fireworks"] += 1
    elif not divisible_by_three and divisible_by_five:
        explosives["Willow Fireworks"] += 1
    else:
        firework_effects.popleft()
        firework_effects.append(firework-1)
        continue

    firework_effects.popleft()
    explosive_power.pop()

perfect_fireshow = all([True if value >= 3 else False for value in explosives.values()])
if perfect_fireshow:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")

if explosive_power:
    print(f" Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

for expl, count in explosives.items():
    print(f"{expl}: {count}")