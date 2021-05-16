in_list = input('Enter values separated by a space: ').split()
print(f'Entered list: {in_list}')

cnt = 0
while cnt != (len(in_list) // 2):
    in_list[2 * cnt], in_list[2 * cnt + 1] = in_list[2 * cnt + 1], in_list[2 * cnt]
    cnt += 1

print(f'Converted list: {in_list}')
