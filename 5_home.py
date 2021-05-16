in_list = [7, 5, 3, 3, 2]
while True:
    try:
        in_val = int(input('Enter the number to exit enter the letter: '))
    except ValueError:
        print('Выход')
        break
    if in_val in in_list:
        in_list.insert(in_list.index(in_val), in_val)
        print(f'Converted list: {in_list}')
    else:
        if in_val > in_list[0]:
            in_list.insert(0, in_val)
            print(f'Converted list: {in_list}')
        else:
            in_list.append(in_val)
            print(f'Converted list: {in_list}')
