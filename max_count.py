def count_numbers(num):
    s = str(num)
    amount = 0
    for c in s:
        amount += int(c)
    return amount
    
    
l = [i for i in range(1, int(input()) + 1)]
result = {}
for i in l:
    result[count_numbers(i)] = result.get(count_numbers(i), 0) + 1
print(max(result.values()))


    
        