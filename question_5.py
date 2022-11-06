"""question - How many students are in the "students" dict? Use the appropriate function."""

"""here I am creating a new function and its name is students_length and in function  i passed a dictionary named students
as parameter """
def students_length(students):
    """ Here I print the input dictionary because when it prints I see the dictionary, so It's easy to calculate the
        length"""
    print(" input is this ", students)
    """Here I am using len() function to determine the length of dictionary and I assign the value of len() 
         function in a variable name total_length"""
    total_length = len(students)
    """Here I return the length to get output of the above function"""
    return total_length


students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
"""Here I called function and assign the value of function in a variable"""
length_of_dictionary_students= students_length(students)
"""here I am calling the variable in which function was assigned"""
print(length_of_dictionary_students)