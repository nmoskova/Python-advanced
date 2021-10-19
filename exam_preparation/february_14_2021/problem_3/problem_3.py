from collections import deque


def stock_availability(*args):
    args = deque(args)
    boxes = args.popleft()
    action = args.popleft()

    if action == "delivery" and len(args) > 0:
        for box in args:
            boxes.append(box)

    elif action == "sell" and len(args) == 0:
        if len(boxes) > 1:
            boxes = boxes[1:]
        else:
            boxes = []

    elif action == "sell" and len(args) > 0:
        parameter = args[0]
        if isinstance(parameter, int):
            for arg in args:
                if arg >= len(boxes):
                    boxes = []
                elif 0 <= arg < len(boxes):
                    boxes = boxes[parameter:]

        else:
            for arg in args:
                while arg in boxes:
                    boxes.remove(arg)

    return boxes


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 1, 1))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

