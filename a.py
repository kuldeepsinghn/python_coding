# create a variable and assign it an integer
num = 7
print(num)

# create a second variable and assign it a float
float_num = 2.123
print(float_num)

# create a third variable and assign it a Boolean value
bol_val = 1 <= 2
print(bol_val)

# re-assign a different integer to the first variable you created
num = 9
print(num)

var = 3 ** 8
print(var)

var1 = 10 // 3
print(var1)

""" create a variable, assign it a value of any data type,then use print()
 to display its assigned value in the output """
var = 98
print(var)

# use print() to print a value of any data type directly
print(type(var))

# use print() to display the result of an expression that uses at least 2 math operators
exp = 15 / 3 * 2 * 2 - (3 + 4)
print(exp)

"""In a .py file, write a program which calculates the subtotal of all 6 of these items using 
an expression.  The subtotal is just the sum of all of their prices"""

penne = 16.68 * 100
pasta_sauce = 6.98 * 100
garlic = 16.78 * 100
italian = 15.26 * 100
Bag = 3.00 * 100
meat_ball = 4.39 * 100

sub_total = (1668 + 698 + 1678 + 1526 + 300 + 439) / 100
print(sub_total)

ex_1 = 'This is a string'
ex_2 = "This is also a string"

ex_3 = "orange"
print(ex_3[2])
print("apple"[4])

# string slicing
print("apple"[:3])
print("apple"[2:5])
print("apple"[4:])

# concatination
# Strings Exercises


# Q.1 Create a variable and assign it the string "Just do it!"
new_var = "Just Do it!"
# Q.2 Access the "!" from the variable by index and print() it
print(new_var[10:])

# Q.3 Print the slice "do" from the variable
print(new_var[4:7])

# Q.4 Get and print the slice "it!" from the variable
print(new_var[8:])

# Q.5 Print the slice "Just" from the variable
print(new_var[:4])

# Q.6 Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.
print("Don't" + new_var[4:])

# type(), str(), and escape sequences exercises

# Q.1 Create a variable and assign it a float
ex_var = 2.43

# Q.2 Use print() and type() to print the data type of the variable in the output
print(type(ex_var))

# Q.3 Use str() on the variable from step 1 and concatenate it with the string " is a float." then use print() to display the result

print(type(ex_var))
print(str(ex_var) + " is a float")

# Q.4 print() the string "Hello, I'm [name], it's nice to meet you!" including quotes (you will need to use the \' or \"
# escape sequence depending on whether you enclose your strings in single quotes or double quotes.)
print("\"Hello, I\'m Kuldeep singh, it\'s nice to meet you! \"")

print("*******\n *****\n  ***\n   *")


#
#
# def information():
#     name = input("What is your name? ")
#     quest = input("What is your quest? ")
#     color = input("What is your fav color?")
#     print("So your name is "+ name, "your fav color is " +color,"Your quest is "+quest)
#
# print(information())


# num = int(input("Enter a integer number here :- "))
# print(type(num))
# print(num +10)

# function with no parameters exercise

# Q.1 Create a function called hello_world_printer() which takes no parameters and prints the string "hello world"

def hello_world_printer():
    print("hello world")


# Q.2 Call the function hello_world_printer()

hello_world_printer()

# function with 1 parameter exercise

#  Q.1 Create a function called name_printer which takes 1 parameter and prints it

# def name_printer(p1):
#     print(p1)
#
#
# name = input("Please enter your name.")
# name_printer(name)


# length= int(input("Enter the length "))
# width= int(input("Enter the width "))
# height= int(input("Enter the height "))

# def volume_of_rectangular_prism(length, width, height):
#     volume=length * width * height
#     print(volume)
#     return volume

# x=volume_of_rectangular_prism(length, width, height)

# celsius = int(input("Please enter an integer value for degrees celsius. "))
#
#
# def fahrenheit(cel):
#     return (18 * cel + 320) / 10
#
#
# print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")

# from random import randint
#
# fuel = randint(10,25)
# miles= randint(200,400)
#
# print(miles//fuel)
# print(fuel)
# print(miles)

#
# my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
#
# print(my_string.startswith("X"))
#
#
# num = 10**3
# print(num)
#
# marks = int(input("Please enter the student's score. "))
#
# if marks >= 90:
#     print("students score A grade" ,marks)
# else:
#     if marks >= 80:
#         print("students score B grade" ,marks)
#     else:
#         if marks >= 70:
#             print("students score C grade" ,marks)
#         else:
#             if marks >= 60:
#                 print("students score D grade" ,marks)
#             else:
#                 print("students is failed sorry :( " ,marks)
#
#
