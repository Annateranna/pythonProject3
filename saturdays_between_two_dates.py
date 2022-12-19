from datetime import date

def saturdays_between_two_dates(start, end):
    saturday = 0
    if start > end:
        date_list = [date.fromordinal(i) for i in range(end.toordinal(), start.toordinal() + 1)]
    else:
        date_list = [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]
    for d in date_list:
        if d.weekday() == 5:
            saturday += 1
    return saturday


date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))