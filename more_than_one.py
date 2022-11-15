l = input().split()
final = set()
for c in l:
    i = l.index(c)
    temp = l[:i] + l[i + 1:]
    if c in temp:
        final.add(c)
print(*sorted(final, key=int))


