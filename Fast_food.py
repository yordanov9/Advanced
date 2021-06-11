from collections import deque

quantity = int(input())
orders = deque()

for order in input().split():
    orders.append(int(order))

max_order = (max(orders))

for i in range(len(orders)):
    order = orders.popleft()
    if order <= quantity:
        quantity -= order
    else:
        orders.appendleft(order)
        break

print(max_order)

as_str = [str(el) for el in orders]
if len(orders) == 0:
    print('Orders complete')
else:
    print(f'Orders left: {" ".join(as_str)}')