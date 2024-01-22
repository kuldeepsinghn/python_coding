# Q1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(a,b):
    return a+b

print(add_two_numbers(a=10,b=20))

# Q2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    pi = 3.14
    area= pi*r**2
    return area

print(area_of_circle(r=10))
# Q3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if
# all the list items are number types. If not do give a reasonable feedback.

#Q4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which
# converts °C to °F, convert_celsius_to-fahrenheit.

def c_into_f(c):
    f = (c*9/5)+32

    return f

print(c_into_f(c =40))

# Q 5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter,
# Spring or Summer.
def check_season(month):
    month_to_season = {
        1: 'Winter', 2: 'Winter', 3: 'Spring',
        4: 'Spring', 5: 'Spring', 6: 'Summer',
        7: 'Summer', 8: 'Summer', 9: 'Autumn',
        10: 'Autumn', 11: 'Autumn', 12: 'Winter'
    }

    if not (1 <= month <= 12):
        return "Invalid month. Please enter a number between 1 and 12."
    season = month_to_season[month]

    return season


result = check_season(1)
print(result)

result_invalid_month = check_season(13)
print(result_invalid_month)



# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        raise ValueError("Error: The x-coordinates must be different to calculate the slope.")
    slope = (y2 - y1) / (x2 - x1)

    return slope

x1, y1 = 2, 3
x2, y2 = 5, 7

slope = calculate_slope(x1, y1, x2, y2)
print(slope)


"""Certainly! The solutions of a quadratic equation 
�
�
2
+
�
�
+
�
=
0
ax 
2
 +bx+c=0 can be found using the quadratic formula:"""


import cmath
def solve_quadratic_eqn(a, b, c):

    underroot = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + underroot) / (2 * a)
    root2 = (-b - underroot) / (2 * a)

    return root1, root2
a = 1
b = -3
c = 2

solutions = solve_quadratic_eqn(a, b, c)
print(solutions)


# Q Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(input_list):
    for i in input_list:
        print(i)
    return None

print(print_list(input_list = [1,2,3,4,5,6,7,8]))


# Q Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (
# use loops).

def reverse_list(input_list):
    reversed_list = []
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list

# Example usage:
input_list = [1, 2, 3, 4, 5]
result = reverse_list(input_list)
print(result)


# Q Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_item(input_list):
    capitalized_list=[]
    for item in input_list:
        capitalized_list.append(str(item).capitalize())
    return capitalized_list

print(capitalize_list_item(input_list= ['apple', 'banana', 'cherry', 'date']))


"""Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]"""


def add_item(input_list,items):
    new_list =[]
    new_list= input_list.copy()
    new_list.append(items)
    return new_list


print(add_item(input_list= ['Potato', 'Tomato', 'Mango', 'Milk'], items= 'meat'))

"""Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
"""

print(5//2)