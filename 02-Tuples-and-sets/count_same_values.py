numbers = [float(num) for num in input().split()]
nums_dict = {}

for el in numbers:
    if el not in nums_dict:
        nums_dict[el] = 0
    nums_dict[el] += 1

[print(f"{el:.1f} - {occurence} times") for el, occurence in nums_dict.items()]