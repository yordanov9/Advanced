string = list(input())
res = []

for i in range(len(string)):
    res.append(string.pop())

print(*res, sep='')
