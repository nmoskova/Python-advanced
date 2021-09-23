from collections import deque


def valid_chocolate(choco: int):
    if choco <= 0:
        while choco <= 0:
            chocolate.pop()
            if chocolate:
                choco = chocolate[-1]
            else:
                return []
    return choco


def valid_cups_milk(cup: int):
    if cup <= 0:
        while cup <= 0:
            cups_milk.popleft()
            if cups_milk:
                cup = cups_milk[0]
            else:
                return []
    return cup


chocolate = [int(x) for x in input().split(", ")]
cups_milk = deque([int(x) for x in input().split(", ")])
milkshakes = 0

while chocolate and cups_milk and (milkshakes < 5):
    current_choco = valid_chocolate(chocolate[-1])
    current_cup = valid_cups_milk(cups_milk[0])

    if chocolate and cups_milk:
        if current_choco == current_cup:
            milkshakes += 1
            chocolate.pop()
            cups_milk.popleft()

        else:
            chocolate[-1] -= 5   # !!! бях намалила с 5 current_sum, което не влияе върху stack-а !!!
            cups_milk.append(cups_milk.popleft())

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if not chocolate:
    print("Chocolate: empty")
else:
    print(f"Chocolate: {', '.join([str(c) for c in chocolate])}")

if not cups_milk:
    print("Milk: empty")
else:
    print(f"Milk: {', '.join([str(c) for c in cups_milk])}")