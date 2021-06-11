import re


def get_n(line, pattern):
    return len(re.findall(pattern, line, re.IGNORECASE))


letter_pattern = r'[a-z]'
punctuation_pattern = r"[',\.\!\?-]"

with open('text.txt', 'r') as file:
    lines = file.readlines()
    counter = 1
    for line in lines:
        n_letters = get_n(line, letter_pattern)
        n_punctuation = get_n(line, punctuation_pattern)
        output = f'Line {counter}: {line} ({n_letters})({n_punctuation})'
        counter += 1
    for line in lines:
        with open('output.txt', 'a') as f:
            f.writelines(output)