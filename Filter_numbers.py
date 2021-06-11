# def is_divisible(n):
#     divisible = [num for num in range(2, 11) if n % num == 0]
#     return True if divisible else False
#
#
# start = int(input())
# end = int(input())
# print([num for num in range(start, end + 1) if is_divisible(num)])

start = int(input())
end = int(input())
print([num for num in range(start, end + 1) if [divisor for divisor in range(2,11) if num % divisor == 0]])
