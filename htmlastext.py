from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
s = str(html)
clear_s = s.replace('<code>', "├")
clear_s = clear_s.replace('</code>', '┤')
state = 0
inner_symbols = []
d = {}
result = []
for c in clear_s:
    if c == "├":
        state = 1
    elif state == 1 and c != '┤':
       inner_symbols.append(c)
    if c == '┤':
        state = 0
        inner_text = ''.join(inner_symbols)
        d[inner_text] = d.get(inner_text, 0) + 1
        inner_symbols = []
for k, v in d.items():
    if v == max(d.values()):
        result.append(k)
print(*sorted(result))
