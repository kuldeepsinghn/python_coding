# creating an empty dictionary
dog = {}
print(dog)
# enter items in dictionary
dog['name'] = 'jd'
dog['breed'] = 'labra'
dog['color'] = 'golden'
dog['age'] = 10
dog['legs'] = 'four'
print(dog)

# deleting a dictionary
del dog
# print(dog)
# creating a new dictionay student and in dictionary i create a list also
student = {'first_name': 'kuldeep', 'last_name' : 'singh', 'gender' : 'male', 'age' : 19, 'marital_status' : 'none', 'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
           'address' : 'lal_mandir', 'city' :'Jaipur', 'country'  : 'India' }
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
keys=student.keys()
print(keys)

# data of value in list form
values=student.values()
print(values)

print(student.items())
del student['first_name']
print(student)

