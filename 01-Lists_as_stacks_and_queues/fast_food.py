from collections import deque

qty_food = int(input())
orders = deque([int(x) for x in input().split()])
biggest_order = max(orders)

while orders:

    if orders[0] > qty_food:
        break

    qty_food -= orders.popleft()

orders = [str(x) for x in orders]

print(biggest_order)
if orders:
    print(f"Orders left: {' '.join(orders)}")
else:
    print("Orders complete")

