"""Set is a collection of items,
Set is a collection of unordered and un-indexed distinct elements
In Python set is used to store unique items
it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
"""

# Exercises: Level 1

# Q1 Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

# Q2 Add 'Twitter' to it_companies
print('Twitter' in it_companies)

# Q3 Insert multiple IT companies at once to the set it_companies
it_companies.update(['apier','rpas','tp'])
print(it_companies)

# Q4 Remove one of the companies from the set it_companies
it_companies.remove('tp')
print(it_companies)

# Q5 What is the difference between remove and discard
# it_companies.remove('tp')
# print(it_companies)

it_companies.discard('xyz')
print(it_companies) #xyz not in it companies but it not raise any error

#Q 6 Join A and B
#union()
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.union(B))


# Q 7 Find A intersection B
print(A.intersection(B))

# Q 8 Is A subset of B
print(A.issubset(B))
print(A.issuperset(B))

# Q9 Are A and B disjoint sets

print(A.isdisjoint(B))

# Q 10 Join A with B and B with A
A.update(B)
print(A)
# print(B.update(A))

#Q11 What is the symmetric difference between A and B
x = B.symmetric_difference(A)
print(x)


# Q12 Delete the sets completely
del A
del B


# Q13 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(age))
age_set = set(age)
print(len(age_set))

print(len(age)==len(age_set))

# Q14   Explain the difference between the following data types: string, list, tuple and set

print("""string :- Any type of text is a string. any data type written as text is string
any data type under single and double and tripe quote is string 

list :- list is sequence of data which is use  to store data 
list stores all types of data in its container and give it a name as variable
list are mutable 
we can change, update, insert the list after creation 
lsit =[]

tuple :- tuple is collection of data
 tuples are immutable
 we can not change tuple after creation 
 tuples are unchanged and unordered and it creates using ()
 
 sets :- set is a collection of items
 set store unique value 
 it is unordered and unindexed
 in tuples we can find union, symmetric differnce, difference, intersections,etc
 set ={} """)




#Q 15 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words
