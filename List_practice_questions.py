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
