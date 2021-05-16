type_list = [1, 'hello', [1, 2], (1, 2, 3), 1.2, True, {1: 2}]
for el in type_list:
    print(f'Element {el} has type {type(el)}')
