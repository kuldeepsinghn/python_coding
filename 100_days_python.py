print("Hello world !")  # it is not code which is inside the double code

print("day 1 - python print function")
print("the function is declared like this")
print("print('what to print')")

print("heello world \nhello world \nhello world")

# string concatenation
print("hello" + " " + "kuldeep")

print("day -1 string manipulation")
print('string concatenation is done with the' " + " 'sign')
print('e.g. print("hello world")')
print("New lines will created with backslash and n ")

# print("what is your name ")
# # input function( a prompt for user)
#
# input("what is your name")

# print("hello"+" "+input("what is your name"))

# print(len(input("what is your pet name? ")))

# python variable

# name = input("Enter your name:- ")
# print(name)

# kuldeep_mobile= 9079724148
# print(kuldeep_mobile)
#
# length = len("kuldeep")
# print(length)
#
#
# a = input("a: ")
# b= input("b: ")
#
# c = a
# a = b
# b= c

# print("a =", a)
# print("b =", b)


# creating a greeting for your program
# print("welcome to the program generator ")

# 2 ask the user where the user grew up
# q=input("enter your city where u grew up? ")
# print(q)

# write a program that a digit in two digit number

# two_digit_number= input("Enter the number :-")
# print(type(two_digit_number))
#
# first_num= two_digit_number[0]
# second_num= two_digit_number[1]
#
# print(first_num)
# print(second_num)
#
# result= int(second_num) + int(first_num)
# print(result)

# create a program using maths fucntions and f-strings that tell how much day, week , month left in your life

age = input("Enter your current age")
age_as_int = int(age)
remaining_age = 90 - age_as_int
# print(remaining_age)

age_in_days= remaining_age * 365
age_in_weeks= remaining_age * 52
age_in_months = remaining_age * 12

print(f"your remaining days in your age are {age_in_days}, weeks are {age_in_weeks} and months are {age_in_months}")


# a = int("5") / int(2.7)
# print(a)

# writte a program to check the number is odd or even
# number = int(input("Enter any which you want :-"))
# if number % 2   == 0:
#     print("it is an even number")
# else:
#     print("it is an odd number")


height= input("Please enter your height here in meter:-")
weight= input("Please enter your weight here in kilograms:-")

bmi =(int(weight)/float(height)**2)
print(bmi)
if bmi < 18.5:
    print("you are under weight")
elif(bmi<=24):
    print("you are a healthy person")
elif(bmi<=30):
    print("you are over wieght you need to loose your weight")
elif(bmi<=35):
    print("you are obse")
else:
    print("you are clinically obese")



year = int(input("Enter the year which you want check that is a leap or not a leap year"))
if year % 4 == 0:
    print("it is an leap year")
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("it is a leap year")
        else:
            print("not a leap year")
    else:
        print("it is not an leap year")
else:
    print("it is an leap year")


