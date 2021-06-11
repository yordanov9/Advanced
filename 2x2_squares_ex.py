rows, columns = [int(el) for el in input().split()]
matrix = []
res = 0
for row in range(rows):
    matrix.append([el for el in input().split()])

    if res > 0:
        print(res)
    else:
        print(0)