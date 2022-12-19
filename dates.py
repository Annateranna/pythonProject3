from datetime import date

early_hurricanes = 0
florida_hurricane_dates = [date(1987, 11, 15), date(1988, 3, 12), date(1976, 5, 12)]

for hurricane in florida_hurricane_dates:
    if hurricane.month < 6:
        early_hurricanes += 1

print(early_hurricanes)