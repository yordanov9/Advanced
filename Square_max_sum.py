rows, columns = [int(el) for el in input().split(", ")]
matrix = []
position = None
current_sum = 0
max_sum = 0

for row in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

for row in range(rows-1, 0, -1):
    for col in range(columns-1,0,-1):
        current_sum = matrix[row][col] + matrix[row][col - 1] + matrix[row - 1][col] + matrix[row - 1][col - 1]
        if current_sum >= max_sum:
            max_sum = current_sum
            position = (row, col)

row, col = position
print(matrix[row - 1][col - 1], matrix[row - 1][col])
print(matrix[row - 1][col - 1], matrix[row][col])
print(max_sum)
