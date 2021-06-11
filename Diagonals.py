n = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(n)]
output = [matrix[i][i] for i in range(n)]
second_output = [matrix[i][n-1-i] for i in range(n)]
print(f'First diagonal: {", ".join([str(el) for el in output])}. Sum: {sum(output)}')
print(f'Second diagonal: {", ".join([str(el) for el in second_output])}. Sum: {sum(second_output)}')