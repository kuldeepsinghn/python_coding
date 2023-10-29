# print("Hello world !")  # it is not code which is inside the double code
#
# print("day 1 - python print function")
# print("the function is declared like this")
# print("print('what to print')")
#
# print("heello world \nhello world \nhello world")
#
# # string concatenation
# print("hello" + " " + "kuldeep")
#
# print("day -1 string manipulation")
# print('string concatenation is done with the' " + " 'sign')
# print('e.g. print("hello world")')
# print("New lines will created with backslash and n ")
#
# # print("what is your name ")
# # # input function( a prompt for user)
# #
# # input("what is your name")
#
# # print("hello"+" "+input("what is your name"))
#
# # print(len(input("what is your pet name? ")))
#
# # python variable
#
# # name = input("Enter your name:- ")
# # print(name)
#
# # kuldeep_mobile= 9079724148
# # print(kuldeep_mobile)
# #
# # length = len("kuldeep")
# # print(length)
# #
# #
# # a = input("a: ")
# # b= input("b: ")
# #
# # c = a
# # a = b
# # b= c
# 
# # print("a =", a)
# # print("b =", b)
#
#
# # creating a greeting for your program
# # print("welcome to the program generator ")
#
# # 2 ask the user where the user grew up
# # q=input("enter your city where u grew up? ")
# # print(q)
#
# # write a program that a digit in two digit number
#
# # two_digit_number= input("Enter the number :-")
# # print(type(two_digit_number))
# #
# # first_num= two_digit_number[0]
# # second_num= two_digit_number[1]
# #
# # print(first_num)
# # print(second_num)
# #
# # result= int(second_num) + int(first_num)
# # print(result)
#
# # create a program using maths fucntions and f-strings that tell how much day, week , month left in your life
#
# age = input("Enter your current age")
# age_as_int = int(age)
# remaining_age = 90 - age_as_int
# # print(remaining_age)
#
# age_in_days = remaining_age * 365
# age_in_weeks = remaining_age * 52
# age_in_months = remaining_age * 12
#
# print(f"your remaining days in your age are {age_in_days}, weeks are {age_in_weeks} and months are {age_in_months}")
#
# # a = int("5") / int(2.7)
# # print(a)
#
# # writte a program to check the number is odd or even
# # number = int(input("Enter any which you want :-"))
# # if number % 2   == 0:
# #     print("it is an even number")
# # else:
# #     print("it is an odd number")
#
#
# height = input("Please enter your height here in meter:-")
# weight = input("Please enter your weight here in kilograms:-")
#
# bmi = (int(weight) / float(height) ** 2)
# print(bmi)
# if bmi < 18.5:
#     print("you are under weight")
# elif (bmi <= 24):
#     print("you are a healthy person")
# elif (bmi <= 30):
#     print("you are over wieght you need to loose your weight")
# elif (bmi <= 35):
#     print("you are obse")
# else:
#     print("you are clinically obese")
#
# year = int(input("Enter the year which you want check that is a leap or not a leap year"))
# if year % 4 == 0:
#     print("it is an leap year")
#     if (year % 100 == 0):
#         if (year % 400 == 0):
#             print("it is a leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("it is not an leap year")
# else:
#     print("it is an leap year")
#
#
# def Average_height_students(input_list):
#     total = 0
#     for i in input():
#         total += i
#     average = total / len(input_list)
#
#     return average, total
#
#
# x,y=(Average_height_students(input_list=[180, 124, 165, 173, 189, 169, 146]))
# print(y)
#
#
# my_dict = {'a': 10, 'b': 5, 'c': 15, 'd': 3}
#
# # Initialize variables to keep track of the minimum value and key
# min_value = None
# min_key = None
#
# # Iterate through the dictionary
# for key, value in my_dict.items():
#     # Check if the current value is smaller than the current minimum value
#     if min_value is None or value < min_value:
#         min_value = value
#         min_key = key
#
# print("Minimum value:", min_value)
# print("Key with minimum value:", min_key)


# Original dictionary
# my_dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
#
# # Sort by keys using a for loop
# sorted_dict_by_keys = {}
# for key, value in sorted(my_dict.items()):
#     print(key)
#     sorted_dict_by_keys[value] = key
#
# print(sorted_dict_by_keys)
#
#
# my_dict={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# def sorted_dict(my_dict):
#     new_sorted_dict={}
#     for keys,value in sorted(my_dict.items()):
#         new_sorted_dict[value]=keys
#     return new_sorted_dict
# print(sorted_dict(sorted_dict(my_dict)))
#

 # dict = {
#   'name': 'Ram',
#   'age': 23,
#   'city': 'Salem'
# }
#
# Keys = {'age', 'name'}#to check
# print(dict.keys() >= {'age', 'name'})
#
#
# import numpy as np
#
# # Your list
# my_list = [1, 2, 3, 4, 5]
#
# # Convert the list to a numpy array
# my_array = np.array(my_list)
#
# # Now, my_array is a numpy array
# print(my_array)
#
#
#
#
# import random
#
# my_list = [1, 5, 4, 2, 36, 5, 8, 7]
#
# def a(lst):
#     ran = random.choice(lst)
#     return ran
#
# # random_element = a(my_list)
# # print("Random Element:", random_element)
#
#
# # Import necessary libraries
# import numpy as np
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score
#
#
# iris = datasets.load_iris()
# X = iris.data
# y = iris.target
#
# # Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
#
# # Standardize features (mean=0, variance=1)
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)
#
# # Create a K-Nearest Neighbors classifier
# k = 3  # You can adjust the number of neighbors as needed
# knn_classifier = KNeighborsClassifier(n_neighbors=k)
#
# # Train the model on the training data
# knn_classifier.fit(X_train, y_train)
#
# # Make predictions on the test data
# y_pred = knn_classifier.predict(X_test)
#
# # Calculate and print the accuracy of the model
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy * 100:.2f}%")
#

# def count_duplicates(student_data):
#     # Create an empty dictionary to store counts of each set of values
#     count_dict = {}
#
#     # Iterate through the values in the student_data dictionary
#     for values in student_data.values():
#         # Convert the list of values to a tuple to make it hashable
#         values_tuple = tuple(values['name'] + values['class'] + values['subject_integration'])
#
#         # Update the count for this set of values in the count_dict
#         count_dict[values_tuple] = count_dict.get(values_tuple, 0) + 1
#
#     # Filter the count_dict to get only the duplicates
#     # Create an empty dictionary to store duplicates
#     duplicates = {}
#
#     # Iterate through the items (key-value pairs) in the count_dict
#     for key, count in count_dict.items():
#         # Check if the count is greater than 1, indicating a duplicate
#         if count > 1:
#             # If it's a duplicate, add it to the 'duplicates' dictionary
#             duplicates[key] = count
#
#     # 'duplicates' now contains the duplicates found in the 'count_dict'
#
#     return duplicates
#
#
# student_data = {
#     'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id5':{'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']},
#     'id6':{'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']}
# }
#
# duplicates = count_duplicates(student_data)
# print(duplicates)
# # for values, count in duplicates.items():
# #     print(f"{values}: {count} times")
#
#

# my_dict = {
#     'outer_key1': {
#         'inner_key1': 'value1',
#         'inner_key2': 'value2'
#     },
#     'outer_key2': {
#         'inner_key3': 'value3',
#         'inner_key4': 'value4'
#     }
# }
# outer_key = 'outer_key1'
# inner_key = 'new_inner_key'
# new_value = 'new_value'

# if outer_key in my_dict:
#     my_dict[outer_key][inner_key] = new_value
#     print(my_dict)
# else:
#     my_dict[outer_key] = {inner_key: new_value}
#     print(my_dict)


#
#
# my_dict = {
#     'outer_key1': {
#         'inner_key1': 'value1',
#         'inner_key2': 'value2'
#     },
#     'outer_key2': {
#         'inner_key3': 'value3',
#         'inner_key4': 'value4'
#     }
# }


# new_inner_key = 'new_key'
# new_value = 1
#
#
# outer_keys_to_update = ['outer_key1', 'outer_key2']
#
# for outer_key in outer_keys_to_update:
#
#     if outer_key in my_dict:
#         my_dict[outer_key][new_inner_key] = new_value
#
#     else:
#         my_dict[outer_key] = {new_inner_key: new_value}
# print(my_dict)

# result ={}
# duplicate = {}
#
# for key, value in student_data.items():
#     if value not in result.values():
#         result[key]=value
#     else:
#         duplicate[key]=value
# print(result,'\n',duplicate)


student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
    'id4':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
'id6':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },'id7':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   }
}


def duplicate_count(input_dictionary):
    duplicate_count = 0
    # to check the dictionary
    check_dictionary= []
    duplicates = []
    for key, value in input_dictionary.items():
        value_list = list(value.items())
        if value_list in check_dictionary:
            duplicates.append(value)
            # duplicate_count += 1
            # if value_list == 2:
            #     duplicate_count.append(value_list)

        else:
            check_dictionary.append(value_list)
    return duplicates

duplicates = duplicate_count(input_dictionary=student_data)
print(f"number of duplicates in student_data {duplicates}")
print(len(duplicates))

def find_duplicate_students(data):
    student_counts = {}
    duplicates = []

    for student_id, student_info in data.items():
        # Convert the student_info to a hashable tuple for easy comparison
        student_info_tuple = (tuple(student_info['name']), tuple(student_info['class']), tuple(student_info['subject_integration']))

        if student_info_tuple in student_counts:
            student_counts[student_info_tuple] += 1
        else:
            student_counts[student_info_tuple] = 1

    for student_id, student_info in data.items():
        student_info_tuple = (tuple(student_info['name']), tuple(student_info['class']), tuple(student_info['subject_integration']))
        if student_counts[student_info_tuple] > 1:
            duplicates.append((student_id, student_counts[student_info_tuple]))

    return duplicates

# Example usage:
student_data = {'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
                'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']},
                'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
                'id4': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
                'id6': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']},
                'id7': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']}}

duplicate_students = find_duplicate_students(student_data)
print("Duplicate students:", duplicate_students)


l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))


