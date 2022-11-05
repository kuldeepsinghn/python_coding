from question_2 import average_num
from question_1 import length_ages
from question_5 import total_students_length
from question_7 import function_2
from question_4 import function
from question_3 import oldest_person

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
x = "Lisbon"
student_dict_length = total_students_length(students)
print("length of students dict =", student_dict_length)

new_dict = function_2(students, x)
print("new_dictionary is based on the address =", new_dict)

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

print(oldest_person(ages))
