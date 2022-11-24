"""question - How many students are in the dictionary? Search for the "len" function."""


"""here I am creating a new function and its name is length_ages and in function  i passed an input_dictionary
as parameter """
def length_ages(input_dictionary):
    """ Here I print the input dictionary because when it prints I see the dictionary so It's easy to calculate the
    length"""
    print("Input dict is", input_dictionary)
    """Here I am using len() function to determine the length of dictionary and I assign the value of len() 
     function in a variable name length"""
    length = len(input_dictionary)
    """Here I return the length to get output of the above function"""
    return length



age = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}
"""Here I called function and assign the value of function in a variable"""
length_of_dictionary = length_ages(input_dictionary= age)
"""here I am calling the variable in which function was assigned"""
print(length_of_dictionary)