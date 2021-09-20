from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles_capacity = [int(x) for x in input().split()]

wasted_water = 0
current_cup = cups_capacity[0]

while cups_capacity and bottles_capacity:
    current_bottle = bottles_capacity.pop()
    if current_cup <= 0:
        current_cup = cups_capacity[0]

    if current_bottle >= current_cup:
        wasted_water += (current_bottle - current_cup)
        current_cup -= current_bottle
        cups_capacity.popleft()

    else:
        current_cup -= current_bottle

bottles_capacity_str = [str(b) for b in bottles_capacity]
cups_capacity_str = [str(c) for c in cups_capacity]

if not cups_capacity and bottles_capacity:
    print(f"Bottles: {' '.join(bottles_capacity_str)}")

if not bottles_capacity and cups_capacity:
    print(f"Cups: {' '.join(cups_capacity_str)}")

print(f"Wasted litters of water: {wasted_water}")



