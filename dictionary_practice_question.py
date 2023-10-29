# Write a Python script to check whether a given key already exists in a dictionary
def already_access(x, dict):
    if x in dict:
        print("key is present in dictionary")
    else:
        print(":key is not present in dictionary")


y = already_access(x=9, dict={1: 23, 7: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})
print(y)


#  Write a Python script to merge two Python dictionaries

def merge_Dict(dict_1, dict_2):
    x = dict_1.copy()
    x.update(dict_2)
    return x

print(merge_Dict(dict_1={'a': 10, 'b': 8}, dict_2={'c': 6, 'd': 4}))


def itreate(dict):
    for key, value in dict.items():
        print(key, value)


x = itreate(dict={'Red': 1, 'Green': 2, 'Blue': 3})


# Write a Python program to remove a key from a dictionary.

def remove(dict):
    if 2 in dict:
        del dict[2]

    return dict


print(remove(dict={1: 3, 2: 4, 5: 6}))


def merge_two(dict_1, dict_2):
    x = dict_1.copy()
    x.update(dict_2)


print(merge_Dict(dict_1={'a': 2, 'b': 3}, dict_2={'c': 3, 'd': 4}))

# Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

# Print the value of key ‘history’ from the below
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# understand how to located the nested key
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}

# solution
print(sampleDict['class']['student']['marks']['history'])


# Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["Kelly"])

# Create a dictionary by extracting the keys from a given dictionary

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york" }

keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)

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

# Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in a dict')

# Rename key of a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)


# Get the key of a minimum value from the following dictionary
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(sample_dict, key=sample_dict.get))

# convert list into dict
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)

