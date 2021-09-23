from collections import deque
import math

numbers = deque()
string_expression = input().split()
current_sum = 0

for el in string_expression:

    if el in "*+-/":
        current_sum = numbers.popleft()

        if el == "*":
            while numbers:
                current_sum *= numbers.popleft()
            numbers.append(current_sum)

        elif el == "+":
            while numbers:
                current_sum += numbers.popleft()
            numbers.append(current_sum)

        elif el == "-":
            while numbers:
                current_sum -= numbers.popleft()
            numbers.append(current_sum)

        elif el == "/":
            while numbers:
                current_sum /= numbers.popleft()

            numbers.append(math.floor(current_sum))

    else:
        numbers.append(int(el))

print(*numbers)