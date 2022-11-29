def convert(str):
    s = str.split()
    if s[2].strip('\n') == 'KB':
        s[1] = int(s[1]) * 1024
    elif s[2].strip('\n') == 'MB':
        s[1] = int(s[1]) * 1024 * 1024
    elif s[2].strip('\n') == 'GB':
        s[1] = int(s[1]) * 1024 * 1024 * 1024
    elif s[2].strip('\n') == 'B':
        s[1] = int(s[1])
    s[0] = s[0].split('.')
    return s

def convert_values(num):
    if num >= 1024 and num < 1024 * 1024:
        total = str(round(num / 1024)) + ' KB'
    elif num >= 1024 * 1024 and num < 1024 * 1024 * 1024:
        total = str(round(num / 1024 / 1024)) + ' MB'
    elif num >= 1024 * 1024 * 1024:
        total = str(round(num / 1024 / 1024 / 1024)) + ' GB'
    else:
        total = str(num) + ' B'
    return total


with open('files.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
    dictionary = {}
    for string in data:
        string = convert(string)
        dictionary[string[0][1]] = dictionary.get(string[0][1], []) + [string[0][0], string[1]]
    sorted_dict = sorted(dictionary.items())
    for d in sorted_dict:
        num = 0
        sorted_names = sorted(d[1], key=str)
        for i in range(len(sorted_names)):
            if type(sorted_names[i]) == str:
                print(sorted_names[i] + '.' + d[0])
            elif type(sorted_names[i]) == int:
                num += sorted_names[i]
        print('----------')
        print('Summary:', convert_values(num))
        print()
