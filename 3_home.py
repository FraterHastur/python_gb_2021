number_month = int(input('Enter month number: '))

month_list = ['winter', 12,
              'winter', 1,
              'winter', 2,
              'spring', 3,
              'spring', 4,
              'spring', 5,
              'summer', 6,
              'summer', 7,
              'summer', 8,
              'autumn', 9,
              'autumn', 10,
              'autumn', 11]

month_dict = {12: 'Winter',
              1: 'Winter',
              2: 'Winter',
              3: 'Spring',
              4: 'Spring',
              5: 'Spring',
              6: 'Summer',
              7: 'Summer',
              8: 'Summer',
              9: 'Autumn',
              10: 'Autumn',
              11: 'Autumn'}
print(f'Your month is {number_month} in list - {month_list[month_list.index(number_month) - 1]}')
print(f'Your month is {number_month} in dictionary - {month_dict[number_month]}')
