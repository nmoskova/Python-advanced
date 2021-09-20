expression = input()
stack = []

for i, ch in enumerate(expression):

    if expression[i] == "(":
        stack.append(i)
    elif expression[i] == ")":
        start_i = stack.pop()
        end_i = i + 1
        print(expression[start_i:end_i])