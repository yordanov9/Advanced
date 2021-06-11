text = tuple(input())
occurrences = {}

for symbol in text:
    if symbol not in occurrences:
        occurrences[symbol] = 0
    occurrences[symbol] += 1

for k,v in sorted(occurrences.items()):
    if k != ' ':
        print(f'{k}: {v} time/s')
    else:
        print(f'Space: {v} time/s')
