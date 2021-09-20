from collections import deque

children = deque(input().split())
n = int(input())

child_to_remove = ''
while children:

    for _ in range(n-1):
        children.append(children.popleft())

    if len(children) > 1:
        child_to_remove = children.popleft()
        print(f"Removed {child_to_remove}")
    else:
        break

print(f"Last is {' '.join(children)}")