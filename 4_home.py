number_input = input('Input positive integer: ')
value = int(number_input)
max_value = value % 10
value = value // 10
while value > 0:
    n_max = value % 10
    if n_max > max_value:
        max_value = n_max
        value = value // 10
    else:
        value = value // 10
print(max_value)

# Решение через цикл for. Не совсем понятно зачем использовать while просят
max_val = 0
for i in number_input:
    if max_val <= int(i):
        max_val = int(i)
print(max_val)
