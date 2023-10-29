# a = 3
# if a > 0:
#     print('A is a positive number')
# # A is a positive number
#
# a = 3
# if a < 0:
#     print('A is a negative number')
# else:
#     print('A is a positive number')
#
#
# a = 0
# if a > 0:
#     print('A is a positive number')
# elif a < 0:
#     print('A is a negative number')
# else:
#     print('A is zero')
#
# # if else  and logical operator
#
# a = 0
# if a > 0 and a % 2 == 0:
#         print('A is an even and positive integer')
# elif a > 0 and a % 2 !=  0:
#      print('A is a positive integer')
# elif a == 0:
#     print('A is zero')
# else:
#     print('A is negative')
#
# # if else or logical operator
#
# user = 'James'
# access_level = 3
# if user == 'admin' or access_level >= 4:
#         print('Access granted!')
# else:
#     print('Access denied!')
#
#
def Eligibility(n):
    print("enter your age = ", n)
    if (n > 18):
        print("you are eligible for driving")
    else:
        print("your are not eligible for driving")


print(Eligibility(n=23))


def result():
    print("Enter Marks Obtained in 5 Subjects: ")
    markOne = int(input("English = "))
    markTwo = int(input("Science = "))
    markThree = int(input("Maths = "))
    markFour = int(input("G.K = "))
    markFive = int(input("social science = "))

    tot = markOne + markTwo + markThree + markFour + markFive
    avg = tot / 5

    if 91 <= avg <= 100:
        print("Your Grade is A1")
    elif 81 <= avg < 91:
        print("Your Grade is A2")
    elif 71 <= avg < 81:
        print("Your Grade is B1")
    elif 61 <= avg < 71:
        print("Your Grade is B2")
    elif 51 <= avg < 61:
        print("Your Grade is C1")
    elif 41 <= avg < 51:
        print("Your Grade is C2")
    elif 33 <= avg < 41:
        print("Your Grade is D")
    elif  21 <= avg < 33:
        print("Your Grade is E1")
    elif avg >= 0 and avg < 21:
        print("Your Grade is E2")
    else:
        print("Invalid Input!")


print(result())


# fruits = ['banana', 'orange', 'mango', 'lemon']
# for i in fruits:
#     if i!= fruits:


def find_length(student):
    for key, value in student.items():
        print(key, value)
    return key, value


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
    if not x % 2:
        count_even += 1
    else:
        count_odd += 1
print("Number of even numbers :", count_even)
print("Number of odd numbers :", count_odd)

print(
    "List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")

if month_name == "February":
    print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
    print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 day")
else:
    print("Wrong month name")

year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30

day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))
