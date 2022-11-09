def choose_plural(amount, declensions):
    if amount < 11 and (20 <= amount < 100):
        end = amount % 10
        if end == 1:
            final = f'{amount} {declensions[0]}'
        elif 2 <= end <= 4:
            final = f'{amount} {declensions[1]}'
        else:
            final = f'{amount} {declensions[2]}'
    else:
        end = amount % 100
        if 11 <= end <= 20:
            final = f'{amount} {declensions[2]}'
        elif 2 <= end % 10 <= 4:
            final = f'{amount} {declensions[1]}'
        elif end % 10 == 1:
            final = f'{amount} {declensions[0]}'
        else:
            final = f'{amount} {declensions[2]}'

    return final


print(choose_plural(321, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
print(choose_plural(512312, ('цент', 'цента', 'центов')))
print(choose_plural(23424157, ('огурец', 'огурца', 'огурцов')))
print(choose_plural(240, ('курица', 'курицы', 'куриц')))
print(choose_plural(111223, ('копейка', 'копейки', 'копеек')))
print(choose_plural(11, ('стул', 'стула', 'стульев')))
print(choose_plural(3458438435812, ('доллар', 'доллара', 'долларов')))