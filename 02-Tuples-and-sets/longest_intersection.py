n = int(input())
longest_intersection = set()

for _ in range(n):
    first_range, second_range = input().split("-")
    first_start, first_end = first_range.split(",")
    second_start, second_end = second_range.split(",")

    first_set = {el for el in range(int(first_start), int(first_end) + 1)}
    second_set = {el for el in range(int(second_start), int(second_end) + 1)}
    intersected = first_set.intersection(second_set)

    if len(intersected) > len(longest_intersection):
        longest_intersection = intersected

print(f"Longest intersection is {sorted(longest_intersection)} with length {len(longest_intersection)}")
