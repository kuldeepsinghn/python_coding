# from day_2_functions import function, function_2, average_age_students, average_num, oldest_person
from average_age_of_dict_ages import average_num
from length_of_dict_ages import length_ages
from length_of_dict_student import total_students_length
from function_to_find_exact_value import function
from Find_exact_name_based_on_address import function_2

#
# # num= 12

# # even_list=find_even_numbers(num)
# # print(even_list)
# # index_4_val=index_of_evens(even_list)
# #
# # print(index_4_val)
# #
# list =[1,2,3,4,5,6,7,8]
# #
# # print(even_number(list))
#
# #
# #
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

# ages_2 = {'kuldeep': 12,
#           'ritu': 10
#           }

# print(oldest_person(ages))

# print("average valuhe of dictionary ages is", average_num(input_dictionary=ages_2))
# print(ages_2)
# print(function(ages, n))

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


# x = "Sesimbra"
# print(function_2(students, x))
# x=average_age_students(students)
# print(x)


# # print(type(ages.values()))
# # print(ages.values())
# # print(average_num(ages))
# #
# # print(ages.values())
# print(oldest_person(ages))
#
#
# students = {
#     "Peter": {"age": 10, "address": "Lisbon"},
#     "Isabel": {"age": 11, "address": "Sesimbra"},
#     "Anna": {"age": 9, "address": "Lisbon"},
# }
#
# # print( "Three students in students_dict :" ,total_students(students))
