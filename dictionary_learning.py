# dictionary

# stores data in key and value form
# matable data structure but keys are immuatable every key should be unique

# dict = {1: "kuldeep", 2 :" singh"}

# 1 --> Key
# 2_--> value
# key --> known
# key--> number, string ,tuple
# value ---> any data type

# it is the collection of data used to store information in the from of key and value
# defined order not changed, do not allows duplicates
# changeble after creation



# dict()  --> built in function
# dict= {} --->user
# dict = dict({1:' kuldeep',2:'singh'})

# dict = {1: "kuldeep", 2 :{3 : "kuldeep"}}
# empty dict = dict ={}


# create a dictionary with each item as a Pair
# Dict = dict([(1, 'Geeks'), (2, 'For')])
# print("\nDictionary with each item as a pair: ")
# print(Dict)

#
# Dict = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}} ----> nested dictionary
# print(Dict)


dict_1 = {1: 'Geeks', 2: 'For'}
dict_1[3]= "xyz"
print(dict_1)


Dict = {1: 'kuldeep', 'name': 'singh', 3: 'naruka'}
print(Dict.get('kuldeep'))


#
#
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dict4 = {}
# for i in (dic1, dic2, dic3):
#     dict4.update(i)
#
# print(dict4)
#
#
# dict1= {1:'kuldeep',' age':20}
# dict2= {'class':4,'college':'riet'}
# dict3={}
# for i in (dict1,dict2):
#     dict3.update(i)
# print(dict3)

student = {'first_name': 'kuldeep', 'last_name': 'singh', 'gender': 'male', 'age': 19, 'marital_status': 'none',
           'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
           'address': 'lal_mandir', 'city': 'Jaipur', 'country': 'India'}


print(student)
print(student['skills'])
# skills = 'html'
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

# Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)



# iterate over dictionaries using for loops.
d = {'x': 10, 'y': 20, 'z': 30}
for dict_key, dict_value in d.items():
    print(dict_key, '->', dict_value)

# merge two dict
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)

# multiply items of dict
my_dict = {'data1':100,'data2':-54,'data3':247}
result=1
for key in my_dict:
    result=result * my_dict[key]

print(result)


# remove item from dict
myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict:
    del myDict['a']
print(myDict)



# map two list into dict
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)


# Write a Python program to remove duplicates from the dictionary.
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
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)
