def absolute_values(list):
    list = [float(el) for el in list]
    return [abs(el) for el in list]


ls = input().split()
print(absolute_values(ls))
