import re
import string
with open('words.txt') as file:
    searched_words = file.read().split()

occ = {}

with open('input.txt') as file:
    content = file.read().lower()
    for line in searched_words:
        result = re.findall(rf'((?<=(\-|s))is(?=(\.|), content))
        occ[line] = len(result)

sorted_result = sorted(occ.items(), key=lambda x: -x[1])
for k,v in sorted_result:
    print(f'{k} - {v}')
