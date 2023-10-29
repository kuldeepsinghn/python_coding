"""you are given a list of integers. Write a function
that takes this list as input and returns the sum of all even numbers in the list multiplied by
 the largest odd number in the list. If there are no even numbers in the list, the function should return 0.

For example, given the list [1, 2, 3, 4, 5], the function should return (2 + 4) * 5 = 30.
 Given the list [1, 3, 5, 7], the function should return 0.
Write a function called sum_even_times_max_odd that takes a list of integers as input and returns
 the result according to the rules above."""


def sum_even_times_max_odd(input_list):
    even_numbers = []
    odd_number = []
    total = 0
    max_oddnum = 0
    answer = 0
    for i in input_list:
        if i % 2 == 0:
            even_numbers.append(i)
            total = total + i

        if i % 2 != 0:
            odd_number.append(i)
            if i > max_oddnum:
                max_oddnum = i

    answer = total * max_oddnum

    return even_numbers, total, odd_number, max_oddnum, answer


x, y, z, a, b = sum_even_times_max_odd(input_list=[3, 5, 7])
print(f"Even number in list {x}")
print(f"Sum of all even numbers= {y}")
print(f"odd numbers in list {z}")
print(f"max odd number in list {a}")
print(f"answer of the program is {b}")


def max_of_two(x, y):
    if x > y:
        return x
    return y


print(max_of_two(10, 12))


def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))


print(max_of_three(3, 6, -5))


def sum_elements(numbers):
    total = 0
    for x in numbers:
        total += x
    return total


print(sum_elements([8, 2, 3, 0, 7]))


def different_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x


print(different_list([1, 2, 3, 3, 3, 3, 4, 5]))


def prime_number(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True;
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
        return True


print(prime_number(9))


def concatenate_list_data(list_1):
    result = ''
    for element in list_1:
        result += str(element)
    return result


print(concatenate_list_data([1, 5, 12, 2]))


def my_func(x):
    return list(set(x))


result = my_func([11, 12, 13, 11, 15, 18, 18, 22, 20, 16, 12])
print(result)


def my_func(x, y):
    return x[y]


result = my_func(list(range(2, 25, 2)), 4)
print(result)


var = 10

def my_func(x):
    var = 5
    print(x * var)


my_func(20)