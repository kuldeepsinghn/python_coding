""" Question - Implement a function that receives the students dict and an address, and returns a list
with names of all students whose address matches the address in the argument.
For instance, invoking "find_students(students, ’Lisbon’)" should return Peter and Anna."""


""" here I am creating a new function and its name is function_2 and in function I passed two arguments
one argument is dictionary and other one is a variable is created by me.
"""
def function_2(students, x):
    """Now I create a new dictionary in function to store name and address according to question"""
    new_dict = {}
    """ Now i am using for loop in this function to get key and value of dictionary here p is used for 
    'key' and q is used for ' value' """
    for p, q in students.items():
        # print(x, y)
        """Now i again used for loop in this function because in this dictionary we have dictionaries in 
        dictionary so i iterate loop in values of dictionary so i take two variable a and b here a is 
         is used for key in upper loop value q is used for value for upper loop value """
        for a, b in q.items():
            # print(a, b)
            """Here i apply condition in for loop so the condition is i compare the value of 2nd loop
             with the variable x if it is true then it returns the name according to address"""
            if x == b:
                """here i used my empty new dictionary and put the key in new dict with the address which was i 
                passed in variable x"""
                new_dict[p] = b
                """here i return value of new dict to get output """
    return new_dict


students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
""" i am calling function here in a variable"""
y = function_2(students, x='Lisbon')
"""here i print the variable to see the output"""
print(y)
