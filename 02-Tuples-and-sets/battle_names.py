n = int(input())
even = set()
odd = set()

for row in range(1, n + 1):
    name = input()
    ch_sum = sum([ord(ch) for ch in name])

    value = ch_sum // row

    if value % 2 == 0:
        even.add(value)
    else:
        odd.add(value)

even_sum = sum(even)
odd_sum = sum(odd)

result = set()
if odd_sum == even_sum:
    result = odd.union(even)
elif odd_sum < even_sum:
    result = odd.symmetric_difference(even)
else:
    result = odd.difference(even)

result = {str(el) for el in result}
print(', '.join(result))


