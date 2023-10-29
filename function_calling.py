# # # from question_2 import average_num
# # # from question_1 import length_ages
# # # from question_5 import total_students_length
# # # from question_7 import function_2
# # # from question_4 import function
# # # from question_3 import oldest_person
# # # from question_6 import average_students
# # #
# # # students = {
# # #     "Peter": {"age": 10, "address": "Lisbon"},
# # #     "Isabel": {"age": 11, "address": "Sesimbra"},
# # #     "Anna": {"age": 9, "address": "Lisbon"},
# # # }
# # # print(average_students(students))
# # #
# # # x = "Lisbon"
# # # student_dict_length = total_students_length(students)
# # # print("length of students dict =", student_dict_length)
# # #
# # # new_dict = function_2(students, x)
# # # print("new_dictionary is based on the address =", new_dict)
# # #
# # # n = 10
# # # ages = {
# # #     "Peter": 10,
# # #     "Isabel": 11,
# # #     "Anna": 9,
# # #     "Thomas": 10,
# # #     "Bob": 10,
# # #     "Joseph": 11,
# # #     "Maria": 12,
# # #     "Gabriel": 10,
# # # }
# # #
# # # average_value = average_num(input_dictionary=ages)
# # # print("Average of dictionary is :", average_value)
# # #
# # # length_of_dict = length_ages(input_dictionary=ages)
# # # print("length of my dictionary ages is :", length_of_dict)
# # #
# # # new_dict = function(ages, n)
# # # print("new_dict based on n value =", new_dict)
# # #
# # # print(oldest_person(ages))
# #
# #
# # def my_function(a, b):
# #     return a + b
# #
# #
# # print(my_function(a=10, b=20))
# #
# #
# # def sum_two_numbers(num_one, num_two):
# #     sum = num_one + num_two
# #
# #     return sum
# #
# #
# # print(sum_two_numbers(num_two=10, num_one=40))
# #
# #
# # def remove_items(lst, item):
# #     lst.remove(item)
# #     return lst  # it is used to get out from function
# #
# #
# # remove_items(lst=[1, 2, 4, 5, 6, 7, 8], item=8)
# # new_list = remove_items(lst=[1, 2, 4, 5, 6, 7, 8], item=8)  # new_list os a varibale used to store the function
# # print(new_list)  # used to display
# #
# #
# # def remove_duplicates(lst):
# #     new_lst = []
# #     for i in lst:
# #         if i not in new_lst:
# #             new_lst.append(i)
# #     return new_lst
# #
# #
# # print(remove_duplicates(lst=[111111.1.1.1,2,2,3,5,6,7,7,7,8,9,9,9,0]))
# #
# #
# #
#
# # num2,num3
#
# # find max of three number
#
# # def max_of_three_number(num1,num2,num3):
# def max_of_three_number(list1):
#     # numbers=[num1,num2,num3]#0=1,1=2
#     max_num=list1[0]# 0= num1
#     for i in list1[1:]:
#         if i > max_num:
#             max_num=i
#     print(max_num)
#     # return max_num
#
# x=max_of_three_number(list1=[1,2,3,4,6,87,9,0,98,65])
# print(x)
#
#
#
#
#
#
#
# Sample dictionary
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}

# The value you want to find the key for
search_value = 2

# Initialize an empty list to store keys with the matching value
matching_keys = []

# Iterate through the dictionary
for key, value in my_dict.items():
    if value == search_value:
        matching_keys.append(key)

print(matching_keys)

# Print the keys that match the value
# if matching_keys:
#     print(f"The key(s) with the value {search_value} is/are: {', '.join(matching_keys)}")
# else:
#     print(f"No key found with the value {search_value}")


my_dict = {"ritu": 4, "kitu": 5, "ridhi": 9, "sidhi": 6}

# Initialize variables to store the maximum key and value
max_key = None
max_value = float('-inf')  # Start with negative infinity as the initial maximum value

# Iterate through the dictionary
for key, value in my_dict.items():
    if value > max_value:
        max_key = key
        max_value = value

print(f"The key with the maximum value is '{max_key}' with a value of {max_value}.")



def get_max_value(input_dict):

    max_key = None
    max_value = float('-inf')  # Start with negative infinity as the initial maximum value
    result_list=[]
    result_dict={}
    for key, value in input_dict.items():
        if value > max_value:
            max_key = key
            max_value = value
            # result_dict = {"max_key" : 'key',
            #                "max_value" : 'value'}

    # Create a dictionary to store the result
    # result_dict = {"max_key": max_key, "max_value": max_value}
    result_dict[max_key]=max_value
    result_list.append(result_dict)
    return result_list

# Example dictionary
my_dict = {"ritu": 14, "kitu": 4, "ridhi": 9, "sidhi": 6}

# Call the function to get the result
result = get_max_value(my_dict)

# Print the result
print("Result:", result)



