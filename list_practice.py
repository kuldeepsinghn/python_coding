# list practice

lst = list()
print(lst)

empty_list = list()
print(empty_list)

lst = []
print(lst)
print(len(lst))

fruits = ['banana', 'orange', 'mango', 'lemon']
print(len(fruits))

vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
print(len(vegetables))

lst = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]  # list containing different data types
print(type(lst))

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]  # we are accessing the first item using its index
print(first_fruit)  # banana
second_fruit = fruits[1]
print(second_fruit)  # orange
last_fruit = fruits[3]
print(last_fruit)  # lemon
# Last index
# last_index = len(fruits) - 1
# last_fruit = fruits[last_index]

last = fruits[-1]
print(last)

lst = ['item1', 'item2']
lst.insert(2, 'item')
print(lst)

lst = []
print(lst)

lst = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6']
print(lst)
print(len(lst))
print(lst[0])
mid = (len(lst) - 1) / 2
print(mid)
# print(lst[mid])?///////////////////////////////

lst = ['kuldeep', 19, 174, {'country': 'India', 'city': 'Jaipur'}]
print(lst)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
# find first element of companies
print(it_companies[0])
# find last element of companies
print(it_companies[-1])

# Print the list after modifying one of the companies
it_companies[0] = 'youtube'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('Microsoft')
print(it_companies)

# Insert an IT company in the middle of the companies list
midpoint = len(it_companies) // 2
it_companies = it_companies[0:midpoint] + ['Vi pro'] + it_companies[midpoint:]
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
companies = [x.upper() for x in it_companies]
print(companies)

# Join the it_companies with a string '#;
print(' '.join(it_companies))

# Check if a certain company exists in the it_companies list.
print(it_companies.index('youtube'))

# Sort the list using sort() method
print(sorted(it_companies))

# Reverse the list in descending order using reverse() method
print(sorted(it_companies, reverse=True))

# Slice out the first 3 companies from the list
first_third_company = it_companies[:3]
print(first_third_company)

# Slice out the last 3 companies from the list
last_third_company = it_companies[-3:]
print(last_third_company)

lst = [1, 2, 3, 4, 5, 6, 7]
last = lst[-3:]
print(last)
#  sliceing middle item


# Remove the first IT company from the list
del it_companies[0]
print(it_companies)

del it_companies[-1]
print(it_companies)

# del full it_companies
# del it_companies
# print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
print(front_end)
back_end = ['Node', 'Express', 'MongoDB']
print(back_end)
front_end.extend(back_end)
print("front_end and back_end", front_end)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)
# sort the list and find min and max age

ages.sort()
print(ages)

print(max(ages))

print(min(ages))

ages.insert(0, 10)
ages.insert(-1, 30)
ages.sort()
print(ages)

# average of ages in list

x=sum(ages)
print("sum of ages", x)

y=len(ages)
print("length of ages", y)

print(sum(ages) / len(ages))

