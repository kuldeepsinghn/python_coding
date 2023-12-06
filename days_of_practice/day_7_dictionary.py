"""A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type"""

# Q1. Create an empty dictionary called dog
empty_dict = {}

# Q2 Add name, color, breed, legs, age to the dog dictionary

dog_dictionary = {}
dog_dictionary['name'] = 'Jd'
dog_dictionary['breed'] = 'labra'
dog_dictionary['legs'] = 4
dog_dictionary['age'] = 11
print(dog_dictionary)

# Q3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

students_dictionary = {}

students_dictionary['first_name'] = 'kuldeep singh'
students_dictionary['last_name'] = 'naruka'
students_dictionary['gender'] = 'male'
students_dictionary['age'] = 20
students_dictionary['marital_status'] = 'no'
students_dictionary['skills'] = ['python', 'sql']
students_dictionary['country'] = "India"
students_dictionary['city'] = 'Jaipur'
students_dictionary['address'] = ('khatipura')
print(students_dictionary)

# Q4 Get the length of the student dictionary
length = len(students_dictionary)
print(length)

# Q5 Get the value of skills and check the data type, it should be a list
print(students_dictionary['skills'])
print(type(students_dictionary['skills']))

# Q6 Modify the skills values by adding one or two skills
skill = ['c', 'c++']
students_dictionary['skills'].extend(skill)
print(students_dictionary)

# Q7 Get the dictionary keys as a list
students_dictionary_keys = list(students_dictionary.keys())
print(students_dictionary_keys)

# Q8 Get the dictionary values as a list
students_dictionary_values_list = list(students_dictionary.values())
print(students_dictionary_values_list)

# Q9 Change the dictionary to a list of tuples using items() method
new_list = students_dictionary.items()
print(new_list)

# Q10 Delete one of the items in the dictionary
x = students_dictionary.popitem()
print(x)

# Q11 Delete one of the dictionaries
del students_dictionary
