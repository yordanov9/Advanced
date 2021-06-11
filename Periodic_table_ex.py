n = int(input())
unique_elements = set()

for _ in range(n):
    unique_elements = unique_elements.union(set(input().split()))

print(*unique_elements, sep='\n')