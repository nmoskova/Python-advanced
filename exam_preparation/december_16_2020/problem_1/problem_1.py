from collections import deque


def below_zero(sex: int):
    return True if sex <= 0 else False


def leftover(sex: int):
    return True if sex % 25 == 0 else False


males_list = [int(x) for x in input().split()]
females_deque = deque([int(x) for x in input().split()])

matches = 0
while males_list and females_deque:
    male = males_list[-1]
    female = females_deque[0]

    if below_zero(male):
        males_list.pop()
        continue
    if below_zero(female):
        females_deque.popleft()
        continue

    if leftover(male):    # при грешен тест да проверя дали не може да има вариант, при който да е <=0 и да е % 25 == 0
        males_list.pop()
        if len(males_list) > 0:
            males_list.pop()
        continue
    if leftover(female):
        females_deque.popleft()
        if len(females_deque) > 0:
            females_deque.popleft()
            continue

    if male == female:
        matches += 1
        males_list.pop()
        females_deque.popleft()
    else:
        females_deque.popleft()
        males_list[-1] -= 2

print(f"Matches: {matches}")

if not males_list:
    print("Males left: none")
else:
    males_list_reversed = [str(x) for x in males_list[-1::-1]]
    print(f"Males left: {', '.join(males_list_reversed)}")

if not females_deque:
    print("Females left: none")
else:
    print(f"Females left: {', '.join([str(x) for x in females_deque])}")