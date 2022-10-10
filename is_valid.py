def is_valid(string):
    return all([string.isdigit(), not string.isspace(), len(string) >= 4, len(string) <= 6])


print(is_valid('4367'))
print(is_valid('92134'))
print(is_valid('89abc1'))
print(is_valid('900876'))
print(is_valid('49 83'))
