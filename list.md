# List in python

## what is list?

- list is sequence of data and used to store collection of data
- list is used to store multiple items in a variable
- lists are sepeated by commas and enclosed with []
- list are mutable means lists are changeable, ordered, and allow dulplicate values and we modify the list values after creation
### list index
- each element in list have its own unique index
- index is used to access any particular item from list

- fist item of list has index[0] and second is index[1] and so on

- eg:- list1 = [3,4,5,"jd","hiyu"]
- positvie indexing in list
- print(marks)
- print(list1[0])
- print(list1[1])
- print(list1[2])
- print(list1[3])

-negative indexing in list
- print(list1[-1])
- print(list1[-2])
- print(list1[-3])
- print(list1[-4])


#### converting negative index into positive 
- print(list1[-3]) --> negative index
- print(list1len(list1)[-3]) --> positive  index
- print(list1[5-3])
- print(lsit1[2])



 
- List are created by using square brackets
-    l =[]
  - eg:- this_list = ["kuldeep","kanishka","hiyu"]
  - print(this_list)
  -  list can have any data type like string,int,boolean
  - list can contain different data types
  - eg :- list1 = ["abc", 34, True, 40, "male"]
## list length
- to check the length of list we use len() fucntion.
- eg:- this_list = ["kuldeep","kanishka","hiyu"]
  - print(this_list)


## check item is present in list
### using in key word

- if 7 in list1:
-        print("yes")
- else:
-        print("no")


## list slicing 
- it is used to solve the problem easily
- helps to find the data from particular point
- it is used for both positive and negative indexes
- modifying list and delete elemnts
#### slicing with positive indexes

- eg:- List1 = [50, 70, 30, 20, 90, 10, 50]
- print(Lst[::])

#### negative indexes for slicing
- eg:- List1 = [1,2,3,4,5,6,7]
- print(Lst[-7::1])
- output : [1,2,3,4,5,6,7]


- eg :- 
- List1 = [1,2,3,4,5,6,7]
- print(List1[1:5])
- output : [2,3,4,5
- 
- eg:- list1=[1,2,3,4,5,6,7]
- print(list1[3:7:2]) # [4,6]
- print(list1[::2]) # [1,3,5]
- print(list1[::]) #[1,2,3,4,5,6,7]



## type()
- according to python list defined as object with data type list
- <class 'list'>
- eg:- this_list = ["kuldeep","kanishka","hiyu"]
- print(type(this_list))

## Insert items in list 
### use insert() method to add insert new item without replacing the existing value 
- used to insert item at specified index
- eg:- thislist = ["apple", "banana", "cherry"]
- thislist.insert(2, "watermelon")
- print(thislist) # ["apple", "banana", "watermelon", "cherry"]


## Add items in list

### use the append() method to add the value to the end of list
- eg:- thislist = ["apple", "banana", "cherry"]
- thislist.append("watermelon")
- print(thislist) # ["apple", "banana", "cherry", "watermelon"]


### Extend list
#### append elements from another list to current list use extend() method
- eg:- thislist = ["apple", "banana", "cherry"]
- this_list1=["mango", "pineapple", "papaya"]
- thislist.extend(this_list1)
- print(thislist) # ["apple", "banana", "cherry", "mango", "pineapple", "papaya"]

- fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
- newlist = []

- for x in fruits:
-   if "a" in x:
-     newlist.append(x)

print(newlist)
## remove items form list
### to remove specified item used remove() method
- thislist = ["apple", "banana", "cherry"]
- thislist.remove("banana")
- print(thislist) # ["apple", "cherry"]

### pop() method
- it is used when you d'ont have specified index
- it remove element form last

- thislist = ["apple", "banana", "cherry"]
- thislist.pop()
- print(thislist) # ["apple", "banana"]


### del()method 
- it is also used to remove specified index
- it is also delete the complete list
#### delete a specific index
- thislist = ["apple", "banana", "cherry"]
- del thislist[0]
- print(thislist) # ["banana", "cherry"]

#### delete complete list
- thislist = ["apple", "banana", "cherry"]
- del thislist

### clear() method
- this is the method used to empties the list
- thislist = ["apple", "banana", "cherry"]
- thislist.clear()
- print(thislist) # []

### loop a list 
#### using for loop 
- thislist = ["apple", "banana", "cherry"]
- for x in thislist:
-   print(x)

#### use loop thorugh index number
- thislist = ["apple", "banana", "cherry"]
- for x in range(len(thislist)):
-   print(x)


## sort list Aplphanumerically
### sort() method. it is sorted list alphanumerically ,asscending, by default
#### eg:- sort list alphabatically
- thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
- thislist.sort()
- print(thislist) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#### eg:- sort list numerically
- thislist = [100, 50, 65, 82, 23]
- thislist.sort()
- print(thislist) # [23, 50,65, 82,100]

### sort list in descending order
####  use the keyword argument reverse = True:

- thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
- thislist.sort(reverse = True)
- print(thislist) # 
['pineapple', 'orange', 'mango', 'kiwi', 'banana']

- thislist = [100, 50, 65, 82, 23]
- thislist.sort(reverse = True)
- print(thislist)  # [100, 82,65,50,23]

## Case Insensitive Sort
### sort() method is case senstive
- it solves capital letters first 

- thislist = ["banana", "Orange", "Kiwi", "cherry"]
- thislist.sort()
- print(thislist) # ['Kiwi', 'Orange', 'banana', 'cherry']


- for this we have solution
- we use built in function as key function when sorting list
- so we make it case insensitive fucntion, 
####  use str.lower

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


## reverse order of list 
- use to reverse the list 
#### reverse() method

- thislist = ["banana", "Orange", "Kiwi", "cherry"]
- thislist.reverse()
- print(thislist)

## copy a list 
### use copy() method
- thislist = ["apple", "banana", "cherry"]
- mylist = thislist.copy()
- print(mylist)

### another way to copy 
#### the built in function list()
- thislist = ["apple", "banana", "cherry"]
- mylist = list(thislist)
- print(mylist)


## join lists
- many ways to join or concatenate two lists in python
- one of the easiest way is using + operator

- list1 = ["a", "b", "c"]
- list2 = [1, 2, 3]

- list3 = list1 + list2
- print(list3)


- Another way to join two lists is by appending all the items from list2 into list1, one by one:
- list1 = ["a", "b" , "c"]
- list2 = [1, 2, 3]

- for x in list2:
-   list1.append(x)

- print(list1)

- extend() method is also used to join two list



### append()	Adds an element at the end of the list
### clear()	Removes all the elements from the list
### copy()	Returns a copy of the list
### count()	Returns the number of elements with the specified value
### extend()	Add the elements of a list (or any iterable), to the end of the current list
### index()	Returns the index of the first element with the specified value
### insert()	Adds an element at the specified position
### pop()	Removes the element at the specified position
### remove()	Removes the item with the specified value
### reverse()	Reverses the order of the list
### sort()	Sorts the list


