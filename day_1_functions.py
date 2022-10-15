from day_2_functions import average_num, total_students, average_age_students

# num= 12
#
# even_list=find_even_numbers(num)
# print(even_list)
# index_4_val=index_of_evens(even_list)
#
# print(index_4_val)
#
# list =[1,2,3,4,5,6,7,8]
#
# print(even_number(list))

#
#
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

print(average_num(ages))



students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

print( "Three students in students_dict :" ,total_students(students))
print(average_age_students(students))