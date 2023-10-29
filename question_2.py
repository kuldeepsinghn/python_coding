""" question - Implement a function that receives the ages dict and returns the average age."""

"""here I am creating a new function and its name is average_num and in function  i passed an input_dictionary
as parameter """


def average_num(input_dictionary):
    """ Here I print the input dictionary because when it prints, and I see the dictionary"""
    print("input is this", input_dictionary)
    """here i create a variable  total = 0"""
    total = 0
    """Here i am using for loop function to go inside the dictionary's values with the help of ' i ' i is only go 
      in values which is integers so give value like 1,2,3,4 etc"""
    for i in input_dictionary.values():
        """Now here I am using the total variable in for loop to calculate the sum of ages of dictionary 
        here first of all the value of total =0 then i=9 total assigns the i value and add the next value of i
        like this i calculate the sum of dictionary but for getting average i also needed length of dictionary"""
        total += i
        """Now i came outside the loop and calculate the length in new variable name is length"""
    length = len(input_dictionary)
    """here i have the sum of dictionary and the length of dictionary 
    the formula to getting average = sum/ length
    so here i take a new variable and calculate the average value """
    avg_val = total / length
    """here i return the value to get the output means the average value"""
    return avg_val


ages = {
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
average_of_dictionary = average_num(input_dictionary=ages)
"""here I am calling the variable in which function was assigned"""
print(average_of_dictionary)
