list_of_int = [42, 32, 255]

for member in list_of_int:
    print(member)
    print(format(member,'08b'))
    print('{:08b}'.format(member))
    print(f'{member:08b}')