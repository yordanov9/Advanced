matrix = [[int(el) for el in input().split(', ')] for _ in range(int(input()))]
even_matrix = [[num for num in sublist if num % 2 == 0] for sublist in matrix]
print(even_matrix)