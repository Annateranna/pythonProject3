n = int(input())
result = set(input().split(', '))
languages = [set(input().split(', ')) for i in range(n - 1)]
for i in range(n - 1):
    result = languages[i].intersection(result)
if result != set():
    print(*sorted(result), sep=', ')
else:
    print('Сериал снять не удастся')

