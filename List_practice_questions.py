"""Exercise 36 - Lists
Given the code below, use the correct method on line 3 in order to find out the number of elements in my_list"""
# program

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

char = len(my_list)

print(char)

"""Exercise 37 - Lists
Given the code below, use the correct code on line 3 in order to remove the element of my_list located at index 5."""
# program
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.pop(5)

print(my_list)

"""Exercise 38 - Lists
Given the code below, use the correct method on line 3 in order to add the element 'C++' at the end of my_list.
"""
# program
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.append("C++")

print(my_list)

"""Exercise 39 - Lists
Given the code below, use the correct method on line 3 in order to remove the element 30 from my_list.
"""
# program
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.pop(3)

print(my_list)

"""Exercise 40 - Lists
Given the code below, use the correct method on line 3 in order to return the index of the element 10.5 in my_list.
"""
# program
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

index = my_list.index(10.5)

print(index)

"""Exercise 41 - Lists
Given the code below, use the correct method on line 3 in order to insert the element 77 at index 4 in my_list.
"""
# program
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.insert(4, 77)

print(my_list)

"""Exercise 42 - Lists
Given the code below, use the correct method on line 3 in order to concatenate my_list with [100, 101, 102], by
 adding the latter at the end of my_list"""
# program
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_list.extend([100,101,102])

print(my_list)

"""Exercise 43 - Lists
Given the code below, use the correct method on line 3 in order to find out how many times does the element 20 occur 
in my_list."""
# program
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

howmany = my_list.count(20)

print(howmany)

"""Exercise 44 - Lists
Given the code below, use the correct function on line 3 in order to sort the elements of my_list in ascending order."""

# program
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

asc = sorted(my_list)

print(asc)

"""Exercise 45 - Lists
Given the code below, use the correct function (and argument) on line 3 in order to sort the elements of my_list
 in descending order."""
# program
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

asc = sorted(my_list, reverse= True)

print(asc)

"""Exercise 46 - Lists
Given the code below, use the correct function on line 3 in order to find out the smallest number in my_list."""
# program
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

small = min(my_list)

print(small)

"""Exercise 47 - Lists
Given the code below, use the correct function on line 3 in order to find out the largest number in my_list."""
# program
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

large = max(my_list)

print(large)

"""Exercise 48 - Lists
Given the code below, use the correct function on line 3 in order to get the sum of all the elements of my_list.
"""
# program
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

add = sum(my_list)

print(add)


# Exercise 49 - Lists
# Given the code below, use the correct method on line 3 in order to delete all the elements from my_list and obtain
# an empty list.

my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

my_list.clear()

print(my_list)

# Exercise 50 - Lists
# Given the code below, use the correct operators and parentheses on line 3 in order to add the elements of
# [30.01, 30.02, 30.03] to my_list and multiply the resulting list by 2.

my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]

add = (my_list + [30.01, 30.02, 30.03])*2

print(add)

"""Exercise 51 - Lists
Given the code below, use the correct code on line 3 in order to return
 the element 20 from my_list based on its index."""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

element = my_list[2]

print(element)

"""Exercise 52 - Lists
Given the code below, use the correct code on line 3 in order to return the element Java from my_list based on its index (negative).
"""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

element = my_list[-2]

print(element)

"""Exercise 53 - Lists
Given the code below, use the correct code on line 3 in order to return a slice made of [30, 'Python', 'Java'] 
from my_list based on positive indexes."""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[3:6]

print(my_slice)

"""Exercise 54 - Lists
Given the code below, use the correct code on line 3 in order to return a slice made of [30, 'Python', 'Java'] from 
my_list based on negative indexes."""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[-4:-1]

print(my_slice)

"""Exercise 55 - Lists
Given the code below, use the correct code on line 3 in order to return my_list except the first 3 elements, 
using a single, positive index."""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[3:]

print(my_slice) #[30, 'Python', 'Java', 'Ruby']

"""Exercise 56 - Lists
Given the code below, use the correct code on line 3 in order to return my_list except the last 4 elements, 
using a single, negative index."""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[:3]

print(my_slice) #[10, 10.5, 20]

"""Exercise 57 - Lists
Given the code below, use the correct code on line 3 in order to return my_list except the first 3 elements, using a single, negative index.
"""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[-4:]

print(my_slice) #[30, 'Python', 'Java', 'Ruby']

"""Exercise 58 - Lists
Given the code below, use the correct code on line 3 in order to return my_list except the last 2 elements,
 using a single, positive index."""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[:5]

print(my_slice) #[10, 10.5, 20, 30, 'Python']

"""Exercise 59 - Lists
Given the code below, use the correct code on line 3 in order to return every third element of my_list starting with 
the first element of the list."""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[::3]

print(my_slice) #[10, 30, 'Ruby']

"""Exercise 60 - Lists
Given the code below, use the correct code on line 3 in order to return every fourth element of my_list starting with 
the last element of the list."""

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

my_slice = my_list[::-4]

print(my_slice) #['Ruby', 20]

