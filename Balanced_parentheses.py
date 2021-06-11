parentheses = input()
stack = []
balance = True
for i in parentheses:
    if i in '[({':
        stack.append(i)
    elif i in '])}':
        if len(stack) == 0:
            balance = False
            break
        opening = stack.pop()
        if i == ']' and opening == '[':
            continue
        elif i == ')' and opening == '(':
            continue
        elif i == '}' and opening == '{':
            continue
        else:
            balance = False
            break

if balance:
    print('YES')
else:
    print('NO')



