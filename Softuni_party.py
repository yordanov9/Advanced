n = int(input())
guests = set()

for _ in range(n):
    guests.add(input())

ticket = input()
arrived = set()
vip = set()
regular = set()

while not ticket == 'END':
    arrived.add(ticket)
    if ticket[0].isdigit():
        if ticket not in vip:
            vip.add(ticket)
    else:
        regular.add(ticket)
    ticket = input()
print(len(guests.difference(arrived)))

sorted_vip = sorted(vip)
sorted_regular = sorted(regular)

for i in sorted_vip:
    print(i)
for k in sorted_regular:
    print(i)


