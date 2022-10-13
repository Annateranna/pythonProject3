def print_given(*args, **kwargs):
    for i in args:
        print(i, type(i))
    temp = sorted(kwargs.items())
    for k in range(len(temp)):
        print(temp[k][0], kwargs[temp[k][0]], type(kwargs[temp[k][0]]))


print_given(b=2, d=4, c=3, a=1)
print()
print_given('apple', 'cherry', 'watermelon')
print()
print_given(1, [1, 2, 3], 'three', two=2)
