def convert(string):
    u, l = 0, 0
    for a in string:
        if a.isalpha():
            if a.isupper():
                u += 1
            else:
                l += 1
    if u > l:
        return string.upper()
    else:
        return string.lower()


print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))

