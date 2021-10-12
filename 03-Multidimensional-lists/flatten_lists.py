string_to_list = input().split("|")
result = []

for i in range(len(string_to_list)-1, -1, -1):
    substring = string_to_list[i].split()
    result += substring

print(' '.join(result))
