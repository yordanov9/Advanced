import re


def replace_symbol(line):
    return re.sub(r"[-,\.\!\?]", '@', line)


with open('text.txt', 'r') as file:
    lines = file.readlines()
    for line in range(len(lines)):
        if line % 2 == 0:
            reversed_output = replace_symbol(lines[line]).split()
            print(' '.join(reversed_output[::-1]))
