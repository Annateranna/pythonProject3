from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
s = str(html)
print('Python' if s.count('Python') >= s.count('C++') else 'C++')