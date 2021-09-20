parentheses = input()
stack_opening_brackets = []
pairs = {
    '(': ')',
    '{': '}',
    '[': ']'
}

balanced = True
for el in parentheses:

    if el in "({[":
        stack_opening_brackets.append(el)
    else:

        if len(stack_opening_brackets) > 0:
            opening_bracket = stack_opening_brackets.pop()
            closing_bracket = el

            if pairs[opening_bracket] != closing_bracket:
                balanced = False
                break
        else:
            balanced = False
            break

if balanced and len(stack_opening_brackets) == 0:
    print("YES")
else:
    print("NO")

