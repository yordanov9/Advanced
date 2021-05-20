string = list(input())
res = []

while len(string) > 0:
    res.append(string.pop())

print(*res, sep='')
