import datetime


some = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

selected_day = datetime.date(2020,5,20)
print(selected_day)
print(f'selected_day:{selected_day}')
print(selected_day.weekday())

print(some[selected_day.weekday()])

