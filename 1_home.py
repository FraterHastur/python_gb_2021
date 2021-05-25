def division(val1, val2):
    try:
        result = val1 / val2
    except ZeroDivisionError:
        result = f'ZeroDivisionError val2 is 0'
    return result


print(division(1, 2))
print(division(0, 2))
print(division(1, 0))
