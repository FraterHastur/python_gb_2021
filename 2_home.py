time_input = int(input('Input Time in seconds: '))
# If next day
if time_input > 86400:
    time_input = time_input - 86400
    time_hour = time_input // 3600
    time_seconds = time_input % 60
    time_minutes = (time_input - (time_hour * 3600) - time_seconds) // 60
    print(f'{time_hour}:{time_minutes}:{time_seconds}')
# if this day
else:
    time_hour = time_input // 3600
    time_seconds = time_input % 60
    time_minutes = (time_input - (time_hour * 3600) - time_seconds) // 60
    print(f'{time_hour}:{time_minutes}:{time_seconds}')
