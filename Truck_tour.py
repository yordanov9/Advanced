from collections import deque

n = int(input())
queue = deque()

for _ in range(n):
    gas_pump = input().split()
    queue.append([int(gas_pump[0]), int(gas_pump[1])])

for i in range(n):
    # can we make a circle
    fuel_tank = 0
    pumps = 0
    for gas_pump in queue:
        fuel, distance = gas_pump[0], gas_pump[1]
        fuel_tank += fuel
        if fuel_tank < distance:
            break
        fuel_tank -= distance
        pumps += 1
    if pumps == len(queue):
        print(i)
        break
    queue.rotate(-1)

