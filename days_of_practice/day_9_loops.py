#  Iterate 0 to 10 using for loop, do the same using while loop.
# for loop
for i in range(11):
    print(i)

# while loop
i = 0
while i <= 10:
    print(i)
    i += 1


#  Iterate 10 to 0 using for loop, do the same using while loop.

# for loop
for i in range(10, -1, -1):
    print(i)

#while loop
i = 10
while i >= 0:
    print(i)
    i -= 1



# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
for i in range(1, 8):
    print('#' * i)



# Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()  # Move to the next line after each row


# Print the following pattern:
#
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for i in range(11):
    result = i * i
    print(f"{i} x {i} = {result}")

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

lang =  ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for item in lang:
    print(item)


# Use for loop to iterate from 0 to 100 and print only even numbers

for number in range(101):
    if number % 2 == 0:
        print(number)


# Use for loop to iterate from 0 to 100 and print only odd numbers
for number in range(101):
    if number % 2 != 0:
        print(number)


# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.

total_sum = 0

for number in range(101):
    total_sum += number

print(f"The sum of all numbers is: {total_sum}")

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
sum_even = 0
sum_odd = 0

for number in range(101):
    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number
print(f"The sum of all evens is: {sum_even}")
print(f"The sum of all odds is: {sum_odd}")


# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']

reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)


# reverse method
reversed_fruits = list(reversed(fruits))
print(reversed_fruits)


#use slicing
reversed_fruits = fruits[::-1]
print(reversed_fruits)
