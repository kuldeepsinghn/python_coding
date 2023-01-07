""" Q.1 - Given the code below, insert the correct negative index on line 3 in
order to get the last character in the string."""
# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[-1])

""" Q-2 - Given the code below, insert the correct positive index on line 3 in 
order to return the comma character from the string"""
# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[7])


"""Q.3 Given the code below, insert the correct negative index on line 3 in order 
to return the w character from the string."""

# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[-10])

"""Q-4 Given the code below, insert the correct method on line 3 in order to return 
the index of the B character in the string."""

# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.index("B"))

"""Q.5 Given the code below, insert the correct method on line 3 in order to return the 
number of occurrences of the letter o in the string."""

# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.count("o"))

"""Q.6 Given the code below, insert the correct method on line 3 in order 
to convert all letters in the string to uppercase
"""
# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.upper())

"""Q.7 Given the code below, insert the correct method on line 3 in order to get the 
index at which the substring Bitcoin starts."""
# program

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.find("Bitcoin"))

"""Q.8 Given the code below, insert the correct method on line 3 in order to check of the 
string starts with the letter X."""
# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.startswith("X"))

"""Q.9 Given the code below, insert the correct method on line 3 in order to convert all uppercase 
letters to lowercase and all lowercase letters to uppercase."""

# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.swapcase())

"""Q.10 Given the code below, insert the correct method on line 3 in order to remove all spaces (single 
Space characters from the keyboard) from the string"""
# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.replace (" ", ""))

"""Q.11 Given the code below, insert the correct method on line 3 in order to replace all the occurrences of 
letter i with the substring btc."""
# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.replace("i","btc"))

"""Q.12 Given the code below, insert the correct method on line 3 in order to split the entire string in two
 parts, using the comma as a delimiter."""
# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.split(","))

"""Q.13 Given the code below, insert the correct method on line 3 in order to join the 
characters of the string using the & symbol as a delimiter.
"""
# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print("&".join(my_string))

"""Q.14 Given the code below, insert the correct code on line 4 in order to concatenate my_string with the following string:

my_other_string = "Poor guy!" """
# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
my_other_string = "Poor guy!"

print(my_string + my_other_string)

"""Q.15 Given the code below, insert the correct method on line 3 in order to convert the first letter of each word
 in the string to uppercase"""

# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string.title())

"""Exercise 16 - Strings
Given the code below, use string formatting with the % operator on line 3 to map the values of 2010, 10k and Bitcoin to the
 corresponding formatting operators"""

# program
my_string = "In %s, someone paid %s %s for two pizzas."

print(my_string%("2010","10k","Bitcoin"))

"""Q.17 Given the code below, use string formatting with the format() method on line 3 to map the values of 2010,
 10k and Bitcoin to the corresponding formatting operators."""
# program
my_string = "In {}, someone paid {} {} for two pizzas."

print(my_string.format("2010","10k","Bitcoin"))

"""Q.18 Given the code below, use slicing and insert the correct code on line 3 in order to return the 
substring 2010 from the string. Use positive indexes """
# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[3:7])

"""Q.19 Given the code below, use slicing and insert the correct code on line 3 in order to 
return the substring Bitcoin from the string. Use negative indexes!"""
# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[-23:-16])

"""Exercise 20 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to 
return the first 12 characters in the string. Use a single, positive index!"""
# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[:12])

"""Exercise 21 - Strings
Given the code below, use slicing and insert the correct code on line 3 in 
order to return the last 9 characters of the string. Use a single, negative index!"""
# program

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[-9:])

"""Q.22 Given the code below, use slicing and insert the correct code on line 3 in 
order to return the entire string in reversed order."""
# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[::-1])

"""Exercise 23 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to 
return every 7th character of the string, starting with the first character.
The final result should be I,n top"""
# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[::7])

"""Exercise 24 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return the
 string except the first 10 characters. Use a single, positive index!"""
# program
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[10:])

"""
Exercise 25 - Strings
Given the code below, use slicing and insert the correct code on line 3 in order to return the string except 
the last 4 characters. Use a single, negative index!"""
# program

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[:-4])