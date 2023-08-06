# Dictionary in Python
### what is dictionary or what do you mean by dictionary?
- dictionary is a collection of keys values
- dictionary is mutable data structure which was built in python
- the keys are immutable object dictionary and key should be unique 
- it stores data in key value pair
- it is an ordered collection of data that contains key value pairs which are seperated with colon inside the curly brackets{}
- it is optimised to retrieve value when key is known 
- same key cannot appear more than once if it repeats it retained last pair
- A number, string or tuple can be used as key.
- the value can be of any data type.
- it is collection which is ordered,changeable, do not allow duplicates.
- ordered means  that the items have a defined order, and that order will not change.
- changeable, meaning that we can change, add or remove items after the dictionary has been created.


##  creating a dictionary
- it is created by placing sequence of elements within curly brackets{}
- it holds the data in key:value form
- values in dictionary can have any data type and duplicated
- keys can't be duplicated and must be immutable
- eg :-
- Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
- print(Dict)
### Dictionary can also be created by the built-in function dict() and dict ={}
- eg:- use dict()
- Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
- print("\nDictionary with the use of dict(): ")
- print(Dict)
- An empty dictionary can be created by just placing to curly braces{}. 
- Dict = {}
- print("Empty Dictionary: ")
- print(Dict)
#### create a dictionary with each item as a Pair
- Dict = dict([(1, 'Geeks'), (2, 'For')])
- print("\nDictionary with each item as a pair: ")
- print(Dict)

## creating nested dictionary 
- it means dictionary inside a dictionary
- means a dictionary which contain a set of multiple dictionary
- nested means putting a dictionary inside a dictionary
- it contains unordered collection of various dictionary 
- eg:-
- Dict = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
- print(Dict)

## Adding elements to the dictionary
- there are many ways to add value in dictionary 
- 1 is dict[key]= 'value'
- builtin function is used to update the existing value
- note - if key - value is already exists in dict then value gets updated or otherwise a new with value is added
- eg:- creating a new dictionry 
- Dict = {}
- print("Empty Dictionary: ")
- print(Dict)
-
- eg :- adding elements at one time
- Dict[0] = 'Geeks'
- Dict[2] = 'For'
- Dict[3] = 1
- print("\nDictionary after adding 3 elements: ")
- print(Dict)
- 
- eg:- add a set of value to a single key 
- Dict['Value_set'] = 2, 3, 4
- print("\nDictionary after adding 3 elements: ")
- print(Dict)
- 
-  eg:-updating existing keys value 
- Dict[2] = 'Welcome'
- print("\nUpdated key value: ")
- print(Dict)
- 
- eg:- adding nested key and value
- Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
- print("\nAdding a Nested Key: ")
- print(Dict)


## Accessing elements of dictionary
- if you want to access the item of dictionary it refers to key name
- this key can be used inside the square backets []
- eg:-
- Dict = {1: 'kuldeep', 'name': 'singh', 3: 'naruka'}
- print("Accessing a element using key:")
- print(Dict['name'])
-
#### there is also a method call get()
- it also help as to access the elements
- it accept key as arguments and return value 
- eg:-
- Dict = {1: 'kuldeep', 'name': 'singh', 3: 'naruka'}
- print(Dict.get(3))

### accessing elements form nested dictionary 
- in this we use indexing[] syntax
-  eg:-
- Dict = {'Dict1': {1: 'kuldeep'},
        'Dict2': {'Name': 'singh'}}

- print(Dict['Dict1']) # {1: 'Geeks'}
- print(Dict['Dict1'][1]) # kuldeep
- print(Dict['Dict2']['Name'])# singh


## delete elements from dictionary 
- del ()
- Dict = {1: 'kuldeep', 'name': 'singh', 3: 'naruka'}
- del(Dict[1]) 
- print(Dict) #{ 'name': 'singh', 3: 'naruka'}



## dictionary methods
- dic.clear() = Remove all the elements from the dictionary
- dict.copy() = Returns a copy of the dictionary
- dict.get(key, default = “None”) = Returns the value of specified key
- dict.items() = Returns a list containing a tuple for each key value pair
- dict.keys() = return  keys
- dict.value() = return values
- dict.update(dict2)= Updates dictionary with specified key-value pairs
- pop() = remove the element with specified key
- popItem() = Removes the last inserted key-value pair
- dict.setdefault(key,default= “None”) = set the key to the default value if the key is not specified in the dictionary
- dict.has_key(key) = returns true if the dictionary contains the specified key.
- dict.get(key, default = “None”) = used to get the value specified for the passed key.
- 