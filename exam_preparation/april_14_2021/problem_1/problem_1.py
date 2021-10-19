from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]

orders_count = 0
while pizza_orders and employees:

    while pizza_orders and (pizza_orders[0] <= 0 or pizza_orders[0] > 10):
        pizza_orders.popleft()

    if not pizza_orders:
        break

    current_employee = employees.pop()

    if pizza_orders[0] <= current_employee:
        orders_count += pizza_orders[0]
        pizza_orders[0] -= current_employee
        continue

    while pizza_orders[0] > 0:
        if pizza_orders[0] <= current_employee:
            orders_count += pizza_orders[0]
            pizza_orders[0] -= current_employee
            break

        orders_count += current_employee
        pizza_orders[0] -= current_employee

        if employees:
            current_employee = employees.pop()
        else:
            break

if not pizza_orders:
    print(f"All orders are successfully completed!\n"
          f"Total pizzas made: {orders_count}")
    if employees:
        print(f"Employees: {', '.join([str(x) for x in employees])}")

if pizza_orders:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")
