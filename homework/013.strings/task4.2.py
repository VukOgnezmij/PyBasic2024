list_of_int = [42, 32, 255]

for member in list_of_int:
    print(member)
    print(format(member,'b'))
    print('{0:b}'.format(member))
    print(f'{member:b}')