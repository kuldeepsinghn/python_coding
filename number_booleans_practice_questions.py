"""Exercise 26 - Numbers & Booleans
Given the code below, use the correct function on line 3 in order to convert num1 from integer to float."""

# program
num1 = 25

num2 = 1.87

print(type(num2))

"""Exercise 27 - Numbers & Booleans
Given the code below, use the correct function on line 3 in order to convert num1 from float to integer."""
# program
num1 = 13.67

num2 = int(num1)

print(type(num2))

"""Exercise 28 - Numbers & Booleans
Given the code below, use the correct math operator in between num1 and num2 on line 4 in order 
to obtain the result shown."""
# program
num1 = 25
num2 = 8

num3 = num1 %num2

"""Exercise 29 - Numbers & Booleans
Given the code below, use the correct math operator in between num1 and num2 on line 4 in order to obtain 
the result shown."""
# program
num1 = 10
num2 = 3

num3 = num1 ** num2

"""Exercise 30 - Numbers & Booleans
Given the code below, use the correct math operator in between num1 and num2 on line 4 in order to obtain 
the result shown."""

# program
num1 = 5
num2 = 2

num3 = num1 //num2

"""Exercise 31 - Numbers & Booleans
Given the code below, use the correct function on line 3 in order to obtain the distance between num1 and 0
"""
# program
num1 = -11

num2 = abs(num1)

print(num2 == 11) #should result in True

"""Exercise 32 - Numbers & Booleans
# Given the code below, use the correct function on line 4 in order to raise num1 to the power of num2."""
# program
num1 = 10
num2 = 5

num3 =pow(num1, num2)

"""Exercise 33 - Numbers & Booleans
Given the code below, use the correct logical operator in between the two expressions on line 1 in order for the final result to be False."""
# program
result = ((25 % 7 + 10 / 2) % 3 == 0) and ((abs(-19) / 2 - 2) > 9)

print(result) #should return False

"""
Exercise 34 - Numbers & Booleans
Given the code below, use the correct logical operator in between the two expressions on line 1 in order for the final result to be True."""
# program
result = (min(pow(2, abs(3)), 9) == 3 ** 2 - 1) or (66 % 20 + 2 > 2 ** 3)

print(result) #should return True

"""Exercise 35 - Numbers & Booleans
Given the code below, use the correct function on line 1 (for which the argument sits inside the parentheses) in order for the final result to be False."""
# program
result = bool(150 % (10 ** 2 / 2))

print(result) #should return False

