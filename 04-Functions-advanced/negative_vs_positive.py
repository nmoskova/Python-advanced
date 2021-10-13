sequence = [int(x) for x in input().split()]
positives = sum(filter(lambda x: x >= 0, sequence))
negatives = sum(filter(lambda x: x < 0, sequence))


print(negatives)
print(positives)
if abs(negatives) > positives:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")