from collections import deque

box = []

for clothing in input().split():
    box.append(int(clothing))
capacity = int(input())

n_of_racks = 1
rack_weight = 0

for i in range(len(box)):
    current_clothing = box.pop()
    if current_clothing + rack_weight > capacity:
        n_of_racks += 1
        rack_weight = 0
    rack_weight += current_clothing

print(n_of_racks)