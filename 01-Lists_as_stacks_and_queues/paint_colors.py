from collections import deque

string = deque(input().split())
colors = []
main_colors = {"red", "yellow", "blue"}
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

while string:

    left_substring = string.popleft()
    right_substring = string.pop() if string else ''

    new_string_left = left_substring + right_substring
    new_string_right = right_substring + left_substring

    if (new_string_left in main_colors) or (new_string_left in secondary_colors):
        colors.append(new_string_left)
    elif (new_string_right in main_colors) or (new_string_right in secondary_colors):
        colors.append(new_string_right)
    else:
        index = len(string) // 2
        string.insert(index, left_substring[:-1])
        string.insert((index + 1), right_substring[:-1])

    while "" in string:
        string.remove("")

for color in colors:
    if color in secondary_colors:
        for c in secondary_colors[color]:
            if c not in colors:
                colors.remove(color)
                break

print(colors)



