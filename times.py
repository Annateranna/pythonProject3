from datetime import date


florida_hurricane_dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
# присваиваем самую раннюю дату урагана в переменную first_date
first_date = sorted(florida_hurricane_dates)[0]

# конвертируем дату в ISO и RU формат
iso = 'Дата первого урагана в ISO формате: ' + str(first_date)
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')

print(iso)
print(ru)
print(us)