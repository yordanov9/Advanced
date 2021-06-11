numbers = [int(el) for el in input().split(', ')]

positive = [el for el in numbers if el >= 0]
negative = [el for el in numbers if el < 0]
even = [el for el in numbers if el % 2 == 0]
odd = [el for el in numbers if el % 2 != 0]

as_str_pos = [str(el) for el in positive]
print('Positive:', ', '.join(as_str_pos))
as_str_neg = [str(el) for el in negative]
print('Negative:', ', '.join(as_str_neg))
as_str_even = [str(el) for el in even]
print('Even:', ', '.join(as_str_even))
as_str_odd = [str(el) for el in odd]
print('Odd:', ', '.join(as_str_odd))


