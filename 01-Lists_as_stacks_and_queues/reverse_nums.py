to_reverse = input().split()

reversed_stack = []

while to_reverse:
    reversed_stack.append(to_reverse.pop())

print(" ".join(reversed_stack))

