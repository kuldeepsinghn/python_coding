# from day_2_functions import check_common_elements
#
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_2 =[11,21,32,42,43,54,65,66]
# print("check at least one element is common or not if common then print is true :=",check_common_elements(list_1,list_2))
#
#
# # list_1=[1,2,3,4,5,6,7,8,9,10]
# # copy = copy_list(list_1)
# # print("original_list =",list_1)
# # print("copy of list :-",copy)
#
# # print(sum_of_list(list))
# #
# # ages = {
# #     "Peter": 10,
# #     "Isabel": 11,
# #     "Anna": 9,
# #     "Thomas": 10,
# #     "Bob": 10,
# #     "Joseph": 11,
# #     "Maria": 12,
# #     "Gabriel": 10,
# # }
# # n = 10
# # print(function(ages, n))
#
# # print(Oldest_person(ages))
#
# #
# # students = {
# #     "Peter": {"age": 10, "address": "Lisbon"},
# #     "Isabel": {"age": 11, "address": "Sesimbra"},
# #     "Anna": {"age": 9, "address": "Lisbon"},
# # }
# #
# # print(name_of_students(students))
#
# #
# # student_data = {'id1':
# #                     {'name': ['Sara'],
# #                      'class': ['V'],
# #                      'subject_integration': ['english, math, science']
# #                      },
# #                 'id2':
# #                     {'name': ['David'],
# #                      'class': ['V'],
# #                      'subject_integration': ['english, math, science']
# #                      },
# #                 'id3':
# #                     {'name': ['Sara'],
# #                      'class': ['V'],
# #                      'subject_integration': ['english, math, science']
# #                      },
# #                 'id4':
# #                     {'name': ['Surya'],
# #                      'class': ['V'],
# #                      'subject_integration': ['english, math, science']
# #                      },
# #                 }
# #
# # print(get_duplicates(student_data))
#
#

#
# dog = {}
# print(dog)
# dog['name'] = 'jd'
# dog['breed'] = 'labra'
# dog['color'] = 'golden'
# dog['age'] = 10
# dog['legs'] = 'four'
# print(dog)
#
#
# del dog
# print(dog)

# student = {'first_name': 'kuldeep', 'last_name' : 'singh', 'gender' : 'male', 'age' : 19, 'marital_status' : 'none', 'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#            'address' : 'lal_mandir', 'city' :'Jaipur', 'country'  : 'India' }
# print(student)
# print(len(student))
# print(student['skills'])
# print(type(student['skills']))
# student['skills'].append('HTML')
# print(student['skills'])
# student['skills'].append('JAVA')
# print(student['skills'])
#
# keys=student.keys()
# print(keys)
# values=student.values()
# print(values)
#
# print(student.items())
# del student['first_name']
# print(student)
#


# list practice

lst = list()
print(lst)

empty_list = list()
print(empty_list)

lst = []
print(lst)
print(len(lst))

fruits = ['banana', 'orange', 'mango', 'lemon']
print(len(fruits))

vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
print(len(vegetables))

lst = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]  # list containing different data types
print(type(lst))

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]  # we are accessing the first item using its index
print(first_fruit)  # banana
second_fruit = fruits[1]
print(second_fruit)  # orange
last_fruit = fruits[3]
print(last_fruit)  # lemon
# Last index
# last_index = len(fruits) - 1
# last_fruit = fruits[last_index]

last = fruits[-1]
print(last)

lst = ['item1', 'item2']
lst.insert(2, 'item')
print(lst)

lst = []
print(lst)

lst = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6']
print(lst)
print(len(lst))
print(lst[0])
mid = (len(lst) - 1) / 2
print(mid)
# print(lst[mid])?///////////////////////////////

lst = ['kuldeep', 19, 174, {'country': 'India', 'city': 'Jaipur'}]
print(lst)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
# find first element of companies
print(it_companies[0])
# find last element of companies
print(it_companies[-1])

# Print the list after modifying one of the companies
it_companies[0] = 'youtube'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('Microsoft')
print(it_companies)

# Insert an IT company in the middle of the companies list
midpoint = len(it_companies) // 2
it_companies = it_companies[0:midpoint] + ['Vi pro'] + it_companies[midpoint:]
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
companies=[x.upper() for x in it_companies]
print(companies)


# Join the it_companies with a string '#;
print(' '.join(it_companies))

# Check if a certain company exists in the it_companies list.
print(it_companies.index('youtube'))

# Sort the list using sort() method
print(sorted(it_companies))

# Reverse the list in descending order using reverse() method
print(sorted(it_companies, reverse=True))


