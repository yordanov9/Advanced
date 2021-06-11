from collections import deque

n = int(input())
stack = []

for i in range(n):
    command = input().split()
    if command[0] == '1':
        stack.append(int(command[1]))

    elif command[0] == '2':
        if len(stack) > 0:
            stack.pop()

    elif command[0] == '3':
        if len(stack) > 0:
            print(max(stack))

    elif command[0] == '4':
        if len(stack) > 0:
            print(min(stack))

reversed = []

for i in range(len(stack)):
    reversed.append(stack.pop())
print(*reversed, sep=', ')
