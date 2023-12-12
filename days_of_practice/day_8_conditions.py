# # Q1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback:
# # You are old enough to drive.
# # If below 18 give feedback to wait for the missing amount of years. Output
#
#
# age_str = input("Enter your age :")
# age = int(age_str)
# if age > 18:
#     print(" You are old enough to drive.")
# else:
#     year_you_wait = 18 - age
#     print(f"wait for the missing {year_you_wait} of years")
#
#
# #Q2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”)
# # to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger
# # differences, and a custom text if my_age = your_age. Output:
#
# my_age = 20
# your_age_str = input("enter your age :")
# your_age = int(your_age_str)
# if (your_age > my_age):
#     age_diff = your_age - my_age
#     print(f"you are {age_diff} bigger than me")
# elif(your_age == my_age):
#     print(f"wow! we are of same age")
# else:
#     small_me = my_age-your_age
#     print(f"you are {small_me}than me ")





#Q3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
# if a is less b return a is smaller than b, else a is equal to b. Output
#
# a_str = input("enter the value :")
# b_str = input("enter the value :")
# a = int(a_str)
# b = int(b_str)
#
#
# if(a>b):
#     print(" a is greater than b")
# elif(a==b):
#     print("a is equal to b")
# else:
#     print("b is greater than a")
#
#


#Q4Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

#
# score = float(input("Enter the student's score: "))
#
# if 80 <= score <= 100:
#     grade = 'A'
# elif 70 <= score < 80:
#     grade = 'B'
# elif 60 <= score < 70:
#     grade = 'C'
# elif 50 <= score < 60:
#     grade = 'D'
# elif 0 <= score < 50:
#     grade = 'F'
# else:
#     grade = 'Invalid Score'
#
#
# print(f"The student's grade is: {grade}")


#Q5 heck if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November,
# the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is
# Spring June, July or August, the season is Summer

#
# month = input("Enter the month: ")
#
#
# month = month.lower()
#
# # Check the season based on the month
# if month in ['september', 'october', 'november']:
#     season = 'Autumn'
# elif month in ['december', 'january', 'february']:
#     season = 'Winter'
# elif month in ['march', 'april', 'may']:
#     season = 'Spring'
# elif month in ['june', 'july', 'august']:
#     season = 'Summer'
# else:
#     season = 'Invalid Month'
#
# print(f"The season for {month.capitalize()} is: {season}")


# Q6 The following list contains some fruits:
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists
# print('That fruit already exist in the list')


fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruits = input("Enter a fruit: ")

if new_fruits in fruits:
    print(f"this {new_fruits} already exists in list")
else:
    fruits.append(new_fruits)
    print("modified_list: ", fruits)


#Q7 Here we have a person dictionary. Feel free to modify it!

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    skills_list = person['skills']

    if skills_list:
        midle_ele = len(skills_list)//2
        print(f"The middle skill is: {skills_list[midle_ele]}")
    else:
        print("skills is empty ")

else:
    print("skills doesn't exists in this dictionary")


# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    skills_list = person['skills']

    if 'Python' in skills_list:
        print("yes it exists")
    else:
        print("doesn't exists")
else:
    print("no existance")

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills_list = person['skills']

    if 'JavaScript' in skills_list and 'React' in skills_list:
        print("He is a front end developer")
    elif 'Node' in skills_list and 'Python' in skills_list and 'MongoDB' in skills_list:
        print("He is a backend developer")
    elif 'React' in skills_list and 'Node' in skills_list and 'MongoDB' in skills_list:
        print("He is a fullstack developer")
    else:
        print("Unknown title")
else:
    print("not existance")


# If the person is married and if he lives in Finland, print the information in the following format:
if 'skills' in person:
    skills_list = person['skills']
    if person.get('is_married') and person.get('country') == 'Finland':
        print("Married and lives in Finland.")

else:
    print("no")