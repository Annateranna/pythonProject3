def likes(names):
    result = 'Никто не оценил данную запись'
    if len(names) == 1:
        result = f'{names[0]} оценил(а) данную запись'
    if len(names) == 2:
        result = f'{names[0]} и {names[1]} оценили данную запись'
    if len(names) == 3:
        result = f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    if len(names) > 3:
        result = f'{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись'
    return result


print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))
