from datetime import date

def get_date_range(start, end):
    if start > end:
        return []
    else:
        date_list = [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]
        return date_list


date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)


print(*get_date_range(date1, date2), sep='\n')