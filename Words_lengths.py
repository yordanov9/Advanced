# text_dict = {k:len(k) for k in input().split(', ')}
# for k, v in text_dict.items():
#     print(f'{k} -> {v}', end=', ')
#

print(', '.join([f'{word} -> {len(word)}' for word in input().split(', ')]))
