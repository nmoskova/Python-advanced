from collections import deque


def operation(current_bee: int, current_nectar: int, current_symbol: str):
    total = 0
    if current_symbol == "+":
        total = current_bee + current_nectar
    elif current_symbol == "*":
        total = current_bee * current_nectar
    elif current_symbol == "-":
        total = current_bee - current_nectar
    elif current_symbol == "/" and current_nectar != 0:  # винаги да се вклчва проверка и ако делителят == 0 !!!
        total = current_bee / current_nectar

    nectar.pop()
    bees.popleft()
    symbols.popleft()

    return abs(total)


bees = deque([int(b) for b in input().split()])
nectar = [int(n) for n in input().split()]
symbols = deque(input().split())
total_honey = 0

while bees and nectar:
    current_bee = bees[0]
    current_nectar = nectar[-1]
    current_symbol = symbols[0]

    if current_nectar < current_bee:
        nectar.pop()
        continue

    total_honey += operation(current_bee, current_nectar, current_symbol)

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join([str(b) for b in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(b) for b in nectar])}")
