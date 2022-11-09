def filter_anagrams(word, words):
    result = []
    for w in words:
        temp = w
        count = 0
        for k in word:
            if k in temp:
                temp = temp.replace(k, '', 1)
                count += 1
        if len(temp) == 0 and count == len(word):
            result.append(w)
    return result

word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))
print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))
print(filter_anagrams('стекло', []))
print(filter_anagrams('клоун', ['колдун', 'кулон', 'уклон', 'кол']))