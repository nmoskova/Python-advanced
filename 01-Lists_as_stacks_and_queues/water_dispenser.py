from collections import deque
import sys
from io import StringIO
#
# input_1 = """2
# Peter
# Amy
# Start
# 2
# refill 1
# 1
# End
# """
#
# input_2 = """10
# Peter
# George
# Amy
# Alice
# Start
# 2
# 3
# 3
# 3
# End
# """
#
# # sys.stdin = StringIO(input_1)
# sys.stdin = StringIO(input_2)

queue = deque()
liters = int(input())

command = input()
while not command == "Start":
    queue.append(command)

    command = input()

while True:
    command = input()

    if command == "End":
        break

    if command.startswith("refill"):
        liters_refill = int(command.split()[1])
        liters += liters_refill
    else:
        liters_pour = int(command)
        person_to_remove = queue.popleft()

        if liters_pour > liters:

            print(f"{person_to_remove} must wait")
        else:
            liters -= liters_pour
            print(f"{person_to_remove} got water")

print(f"{liters} liters left")