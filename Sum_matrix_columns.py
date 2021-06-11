rows, columns = [int(el) for el in input().split(', ')]
matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

for col in range(columns):
    currrent_sum = 0
    for row in range(rows):
        currrent_sum += matrix[row][col]
    print(currrent_sum)
