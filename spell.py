def spell(*args):
    words = [w.lower() for w in args]
    d = {}
    for t in words:
        d.update(dict.fromkeys(t[0], 0))
    for k in d.keys():
        for w in words:
            if k == w[0] and d[k] <= len(w):
                d[k] = len(w)
    return d


words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))
print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))

