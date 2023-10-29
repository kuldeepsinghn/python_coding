# def function_2(students, x):
#     new_dict = {}
#     for p, q in students.items():
#         # print(p, q)
#         if x == q.get('address'):
#             new_dict[p]=x
#     return new_dict
#


#
# print(function_2(students, x= 'Lisbon'))


#
# def find_length(student):
#     for key, value in student.items():
#         len()
#         print(key, value)
#
#
# student = {
#     "Peter": {"age": 10, "address": "Lisbon"},
#     "Isabel": {"age": 11, "address": "Sesimbra"},
#     "Anna": {"age": 9, "address": "Lisbon"},
# }
#
# print(find_length(student))

def average_students(students):
    total = 0
    for i, j in students.items():
        total += students[i]['age']

    average = total / len(students.keys())
    return average




students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
print(average_students(students))
