from collections import deque

num_pumps = int(input())
stations = deque()

for _ in range(num_pumps):
    stations.append(input().split())

for i in range(num_pumps):
    reservoir = 0
    completed = True

    for pump in stations:

        petrol = int(pump[0])
        distance = int(pump[1])
        reservoir += petrol

        if distance > reservoir:
            completed = False
            break
        reservoir -= distance

    if completed:
        print(i)
        break
    else:
        stations.append(stations.popleft())









