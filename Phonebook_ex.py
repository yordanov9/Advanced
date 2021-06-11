data = input()
phonebook = {}
while not data.isdigit():
    name, phone = data.split('-')
    phonebook[name] = phone
    data = input()

for _ in range(int(data)):
    name = input()
    if phonebook.get(name):
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')
