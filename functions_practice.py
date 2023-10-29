# syntax
# Declaring a function
# def function_name():
# codes

# Calling a function
# function_name()

# functions calling with parameters

def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)


generate_full_name()  # calling a function


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)


add_two_numbers()


# Function Returning a Value - Part 1

def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total


print(add_two_numbers())


# Function with Parameters

# syntax
# Declaring a function
# def function_name(parameter):
#     codes
#     codes
#
#
# # Calling function
# print(function_name(argument))


def greetings(name):
    message = name + ', welcome to Python for Everyone!'
    return message


print(greetings('Asabeneh'))


def add_ten(num):
    ten = 10
    return num + ten


print(add_ten(90))


def square_number(x):
    return x * x


print(square_number(2))


def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area


print(area_of_circle(10))


def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    print(total)


print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050


# Two Parameter: A function may or may not have a parameter or parameters.

# syntax
# Declaring a function
# def function_name(para1, para2):
#     codes
#     codes
#
#
# # Calling function
# print(function_name(arg1, arg2))


def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print('Full Name: ', generate_full_name('Asabeneh', 'Yetayeh'))


def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum


print('Sum of two numbers: ', sum_two_numbers(1, 9))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age;


print('Age: ', calculate_age(2021, 1819))


def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + ' N'  # the value has to be changed to a string first
    return weight


print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))


# Passing Arguments with Key and Value

# syntax
# Declaring a function
# def function_name(para1, para2):
#     codes
#     codes
# Calling function
# print(function_name(para1 = 'John', para2 = 'Doe')) # the order of arguments does not matter here

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    print(full_name)


print(print_fullname(firstname='Asabeneh', lastname='Yetayeh'))


def add_two_numbers(num1, num2):
    total = num1 + num2
    print(total)


print(add_two_numbers(num2=3, num1=2))  # Order does not matter


def is_even_num(lst):
    even_num = []
    for n in lst:
        if n % 2 == 0:
            even_num.append(n)
    return even_num


print(is_even_num(lst=[1, 2, 3, 4, 5, 6, 7, 8, 9]))




def greetings(name='Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message


print(greetings())
print(greetings('Asabeneh'))


def generate_full_name(first_name='Asabeneh', last_name='Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())
print(generate_full_name('David', 'Smith'))


def calculate_age(birth_year, current_year=2021):
    age = current_year - birth_year
    return age;


print('Age: ', calculate_age(1821))


def unique_list(lst):
    new_lst = []
    for a in lst:
        if a not in new_lst:
            new_lst.append(a)
    return new_lst


print(unique_list(lst = [1, 2, 3, 3, 3, 3, 4, 5]))

""""""
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


print(multiply((8, 2, 3, -1, 7)))


def weight_of_object(mass, gravity=9.81):
    weight = str(mass * gravity) + ' N'  # the value has to be changed to string first
    return weight


print('Weight of an object in Newtons: ', weight_of_object(100))  # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62))  # gravity on the surface of the Moon

"""here we create a function name add_two_numbers in which we pass two arguments num1 and num2"""


def add_two_numbers(num1, num2):
    """here i take a variable name total and add both numbers """
    total = num1 + num2
    """here i return the variable"""
    return total


"""i call the function """
print(add_two_numbers(2, 3))

"""here i make a function name is calculate age in which i pass two arguments current year and birth year to 
calculate age"""


def calculate_age(current_year, birth_year):
    """ here i take a varibale name  age and here i subtract birth year from current year to get age"""
    age = current_year - birth_year
    """here i return the age"""
    return age;


"""here i call the function"""
print('Age: ', calculate_age(2022, 2003))


def reverse_list(lst):
    l = []  # empty list

    # iterate to reverse the list
    for i in lst:
        # reversing the list
        l.insert(0, i)
    # printing result
    return l


print(reverse_list(lst=[1, 2, 3, 4, 5, 6, 7, 8, 9]))


def string_reverse(str1):
    rev_str1 = ''
    index = len(str1)
    while index > 0:
        rev_str1 += str1[index - 1]
        index = index - 1
    return rev_str1


print(string_reverse('1234abcd'))


def print_list(lst):
    ls = []
    for i in lst:
        print(i)
    return i


print(print_list(lst=[1, 2, 3, 4, 5, 6]))


def add_item(lst, item):
    lst.append(item)
    return lst


lst = [1, 2, 3, 4, 5, 7]
print(add_item(lst, item=6))


def remove_items(lst, item):
    lst.remove(item)
    return lst


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(remove_items(lst, item=7))

# which checks if a number is prime.


# Program to check if a number is prime or not
