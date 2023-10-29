# creating an empty dictionary
dog = {}
print(dog)
# enter items in dictionary
dog['name'] = 'jd'
dog['breed'] = 'labrador'
dog['color'] = 'golden'
dog['age'] = 10
dog['legs'] = 'four'
print(dog)

# deleting a dictionary 
del dog
# print(dog)
# creating a new dictionay student and in dictionary i create a list also
student = {'first_name': 'kuldeep', 'last_name': 'singh', 'gender': 'male', 'age': 19, 'marital_status': 'none',
           'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
           'address': 'lal_mandir', 'city': 'Jaipur', 'country': 'India'}
print(student)

# find length of dictionary using len() function
print(len(student))

# find value of key
print(student['skills'])

# check type
print(type(student['skills']))

#  addd element in dictionary using append() function
student['skills'].append('HTML')
print(student['skills'])
student['skills'].append('JAVA')
print(student['skills'])

# data of key is in list form
keys = student.keys()
print(keys)

# data of value in list form
values = student.values()
print(values)

print(student.items())
del student['first_name']
print(student)
c

def new_one():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    dict4 = {}
    for i in (dic1, dic2, dic3):
        dict4.update(i)

    return dict4


print(new_one())

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')


is_key_present(5)
is_key_present(9)


def square_of_keys_value(n):
    d = dict()
    for x in range(1, n + 1):
        d[x] = x ** 2
    return d


print(square_of_keys_value(100))

myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(myDict)

if 'a' in myDict:
    del myDict['a']
print(myDict)

keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)


def remove_duplicates(student_data):
    result = {}

    for key, value in student_data.items():
        if value not in result.values():
            result[key] = value

    return result


print(remove_duplicates(student_data={'id1':
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
                                          {'name': ['Surya'],
                                           'class': ['V'],
                                           'subject_integration': ['english, math, science']
                                           },
                                      }))
