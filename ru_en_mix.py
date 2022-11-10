dictionary = {'en': "AaBCcEeHKMOoPpTXxy", 'ru': "АаВСсЕеНКМОоРрТХху"}
c1, c2, c3 = [input() for _ in range(3)]
if (c1 in dictionary['en']) and (c2 in dictionary['en']) and (c3 in dictionary['en']):
    print('en')
elif (c1 in dictionary['ru']) and (c2 in dictionary['ru']) and (c3 in dictionary['ru']):
    print('ru')
else:
    print('mix')