from average_age_of_dict_ages import average_num
from length_of_dict_ages import length_ages
from length_of_dict_student import total_students_length
from function_to_find_exact_value import function
from Find_exact_name_based_on_address import function_2

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
x = "Lisbon"
student_dict_length = total_students_length(students)
print("length of students dict =", student_dict_length)

new_dict = function_2(students, x)
print("new_dictionary is based on the address =",new_dict)


n = 10
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

average_value = average_num(input_dictionary=ages)
print("Average of dictionary is :", average_value)

length_of_dict = length_ages(input_dictionary=ages)
print("length of my dictionary ages is :", length_of_dict)

new_dict = function(ages, n)
print("new_dict based on n value =", new_dict)
