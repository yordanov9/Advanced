def round_numbers(list):
    list = [float(el) for el in list]
    return [round(x) for x in list]


ls = input().split()
print(round_numbers(ls))
