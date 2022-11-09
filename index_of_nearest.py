def index_of_nearest(numbers, number):
    result = -1
    if numbers != []:
        temp = [abs(i - number) for i in numbers]
        result = temp.index(min(temp))
    return result


print(index_of_nearest([7, 5, 4, 4, 3], 4))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([], 17))