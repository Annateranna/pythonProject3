from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
result = []
for td in soup.find_all('td'):
    result.append(int(td.getText()))
print(sum(result))