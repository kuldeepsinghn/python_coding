"""Write a Python function sort_grades that takes a list of student dictionaries,
where each dictionary contains a student's name (a string) and a list of their grades
(a list of integers), and returns a new list of dictionaries sorted by the
 students' average grade in descending order. If two or more students have the same average grade,
 they should be sorted in alphabetical order by name."""

students = [
    {'name': 'Alice', 'grades': [90, 85, 95]},
    {'name': 'Bob', 'grades': [75, 80, 85]},
    {'name': 'Charlie', 'grades': [95, 80, 70]},
    {'name': 'Dave', 'grades': [60, 75, 90]},
    {'name': 'Eve', 'grades': [85, 90, 95]},
    {'name': 'Frank', 'grades': [70, 80, 90]}
]


# def sort_grades(input_list):
#     sort_grade_list = []
#     for students_data in input_list:
#         sort_grade_dict = {}
#         # print(i)
#         total = 0
#         for i in students_data['grades']:
#             total += i
#
#         avg = total / len(students_data['grades'])
#         # sort_grade_dict[students_data['name']] = [avg]
#         sort_grade_dict[students_data['name']] = students_data['grades']
#         # sort_grade_dict_1 = sorted(sort_grade_dict.items(), key=lambda x:x[1], reverse=True)
#         # converted_dict = dict(sort_grade_dict_1)
#         sort_grade_list.append(sort_grade_dict)
#
#     return sort_grade_list
#
#
# x = sort_grades(input_list=students)
# print(x)
# # print(y)




def sort_grades(input_list):
    ret_list = []
    for student in input_list:
        sum = 0
        for grade in student['grades']:
            sum += grade
        avg = sum / len(student['grades'])
        student['avg'] = avg
        ret_list.append(student)
    ret_list = sorted(ret_list,key=lambda student:(- student['avg'],student['name']),reverse=False)
    return ret_list


x = sort_grades(input_list=students)
print(x)
