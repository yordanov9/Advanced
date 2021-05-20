string = input()
stack = []

for i in range(len(string)):
    if string[i] == '(':
        stack.append(i)
    elif string[i] == ')':
        start_idx = stack.pop()
        print(string[start_idx:i + 1])
