command = input()
odd_even = 0 if command == "Even" else 1

numbers = [int(x) for x in input().split()]
result = sum(filter(lambda x: x % 2 == odd_even, numbers)) * len(numbers)
print(result)