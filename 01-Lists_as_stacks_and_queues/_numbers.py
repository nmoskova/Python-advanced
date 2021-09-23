first_set = {int(el) for el in input().split()}
second_set = {int(el) for el in input().split()}

n = int(input())

for _ in range(n):
    data = input().split()
    command = " ".join(data[0:2])
    numbers = [int(num) for num in data[2:]]

    if command == "Add First":
        first_set.update(numbers)

    elif command == "Add Second":
        second_set.update(numbers)

    elif command == "Remove First":
        for num in numbers:
            if num in first_set:
                first_set.remove(num)

    elif command == "Remove Second":
        for num in numbers:
            if num in second_set:
                second_set.remove(num)

    elif command == "Check Subset":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

first_set_sorted = [str(num) for num in sorted(first_set)]
second_set_sorted = [str(num) for num in sorted(second_set)]

print(", ".join(first_set_sorted))
print(", ".join(second_set_sorted))