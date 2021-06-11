def read_matrix(rows):
    matrix = []

    for i in range(rows):
        matrix.append([])
        for el in input().split():
            inner_list = matrix[-1]
            inner_list.append(int(el))
    return matrix


n = int(input())
sum = 0
m = read_matrix(n)
primary = 0
secondary = 0
for i in range(n):
    primary += m[i][i]
for j in range(n):
    secondary += m[len(m) - 1 - j][j]

print(abs(primary - secondary))
