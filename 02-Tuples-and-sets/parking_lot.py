commands_count = int(input())
cars = set()

for _ in range(commands_count):
    direction, car_number = input().split(', ')
    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT":
        cars.remove(car_number)

if not cars:
    print("Parking Lot is Empty")
else:
    [print(car) for car in cars]