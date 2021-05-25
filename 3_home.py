def my_func(val1, val2, val3):
    val_list = [val1, val2, val3]
    min_val = val1
    for val in val_list:
        if min_val >= val:
            min_val = val
    val_list.remove(min_val)
    return sum(val_list)


print(my_func(1, 0, 4))
