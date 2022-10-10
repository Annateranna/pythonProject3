def same_parity(numbers):
    return list(filter(lambda n: n % 2 == numbers[0] % 2, numbers))


print(same_parity([-7, 0, 67, -9, 70, -29, 90]))
print(same_parity([6, 0, 67, -7, 10, -20]))

