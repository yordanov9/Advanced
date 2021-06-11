def remove_vowels(txt):
    removed = [el for el in txt if el.lower() not in ['a', 'o', 'u', 'e', 'i']]
    return ''.join(removed)


def is_vowel(char):
    if char in 'aeouei':
        return True
    return False


print(remove_vowels(input()))
print(''.join([char for char in input() if not is_vowel(char)]))
