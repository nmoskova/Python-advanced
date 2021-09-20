from collections import deque

duration_green_light = int(input())
free_window = int(input())

cars_queue = deque()
there_is_a_crash = False
ch_hit = ''
current_car = ''
cars_passed = 0

while True:
    command = input()

    if command == "END":
        break

    if command == 'green':
        time_left = duration_green_light

        for _ in range(len(cars_queue)):

            if time_left > 0:
                current_car = cars_queue.popleft()
                if len(current_car) > time_left + free_window:
                    ch_hit = current_car[time_left+free_window]
                    there_is_a_crash = True
                else:
                    time_left -= len(current_car)
                    cars_passed += 1
            else:
                break
    else:
        cars_queue.append(command)

    if there_is_a_crash:
        break

if there_is_a_crash:
    print(f"A crash happened!")
    print(f"{current_car} was hit at {ch_hit}.")
else:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")