from collections import deque
import sys
from io import StringIO
#
# input_1 = """George
# Peter
# William
# Paid
# Michael
# Oscar
# Olivia
# Linda
# End
# """
#
# sys.stdin = StringIO(input_1)

superm_queue = deque()
while True:
    command = input()

    if command == "End":
        print(f"{len(superm_queue)} people remaining.")
        break

    if command == "Paid":
        while superm_queue:
            print(superm_queue.popleft())
    else:
        superm_queue.append(command)
