in_string = input('Enter strings separated by a space: ').split()

for numb, val in enumerate(in_string):
    if len(val) >= 10:
        print(f'{numb + 1} : {val[:10]}')
    else:
        print(f'{numb + 1} : {val}')
