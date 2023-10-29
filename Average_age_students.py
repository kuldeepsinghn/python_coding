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
# from itertools import zip_longest
#
# # def average_age():
# #     values = ages.values()
# #     age_sum = sum(values)
# #     print("Total age :", age_sum)
# #
# #     age_length = len(ages)
# #     print("length of total ages :" ,age_length)
# #
# #     average = age_sum / age_length
# #     return average
# #
# #
# # print("The average of total age is :", average_age())
#
#
# color=[('red',1),('blue',2),('green',3)]
# d = dict(color)
# print(d)
#
# l1=[1,2,3,4]
# l2=['a','b','c','d']
#
# dic = zip(l1,l2)
# print(dict(dic))
#
# d1=zip(l1,l2)
# print(dict(d1))
#
# l=[1,2,3,4,5,6]
# l3=['a','b','c','d']
#
# d1 = zip_longest(l,l3)
# print(dict(d1))
#
# d1 = zip_longest(l,l3, fillvalue='x')
# print(dict(d1))
#
#
#
# l1=[{1:'a',2:'b'},{3:'c',4:'d'}]
# d1={}
# for i in l1:
#     d1.update(i)
#
# print (d1)
# #Output:{1: 'a', 2: 'b', 3: 'c', 4: 'd'}


students = [
    {'name': 'Alice', 'grades': [90, 85, 95]},
    {'name': 'Bob', 'grades': [75, 80, 85]},
    {'name': 'Charlie', 'grades': [95, 80, 70]},
    {'name': 'Dave', 'grades': [60, 75, 90]},
    {'name': 'Eve', 'grades': [85, 90, 95]},
    {'name': 'Frank', 'grades': [70, 80, 90]}
]
def sort_grades(input_list):
    sort_grade_dict = {}
    total = 0
    for students_data in input_list:
        # print(i)
        total = 0
        for i in students_data['grades']:
            total += i

        avg = total / len(students_data['grades'])
        sort_grade_dict[students_data['name']] = [avg]
        sorted_dict_by_grade = sorted(sort_grade_dict.items(), key=lambda x: x[1], reverse = True)
        # sorted_dict_by_name=sorted(students, key=lambda students: (-avg(students), students['name']))

    return sort_grade_dict, sorted_dict_by_grade


x,y= sort_grades(input_list=students)
print(x)
print(y)
