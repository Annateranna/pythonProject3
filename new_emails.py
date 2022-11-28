existing_logins = []
exit_logins = []
for _ in range(int(input())):
    existing_logins.append(input().split('@')[0])
for _ in range(int(input())):
    name = input()
    if name not in existing_logins:
        exit_logins.append(name + '@beegeek.bzz')
        existing_logins.append(name)
    else:
        count = 1
        name_new = name
        while name_new in existing_logins:
            name_new = name + str(count)
            count += 1
        else:
            exit_logins.append(name_new + '@beegeek.bzz')
            existing_logins.append(name_new)
print(*exit_logins, sep='\n')