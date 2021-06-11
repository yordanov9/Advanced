# n = int(input())
# nums = []
# for _ in range(n):
#     nums.extend([int(el) for el in input().split(', ')])
# print(nums)

n = int(input())

matrix = [[int(el) for el in input().split(', ')] for i in range(n)]
flat_matrix = [num for sublist in matrix for num in sublist]
print(flat_matrix)
