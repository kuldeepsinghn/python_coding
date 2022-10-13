
from day_1_functions import num

def find_even_numbers(num):
    evens = []
    for i in range(num + 1):
        if i % 2 == 0:
            evens.append(i)

    return evens


print(find_even_numbers(num))



from day_1_functions import num

def Table(num):
    for x in range(1, 11):
        Y=(num, 'X' , x, '=', num * x)
        print(Y)
    return  Y

print(Table(num))
