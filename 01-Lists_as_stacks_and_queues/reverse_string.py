string_to_reverse = input()
string_to_list = []

for ch in string_to_reverse:
    string_to_list.append(ch)

reversed_string = ''
while string_to_list:
    reversed_string += string_to_list.pop()

print(reversed_string)