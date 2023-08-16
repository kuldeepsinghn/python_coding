"""Write a Python program to count the number of strings from a given list of strings.
The string length is 2 or more and the first and last characters are the same."""

list = ['abc', 'xyz', 'aba', '1221']


def number_of_string(input_list):
    count_num = 0
    for i in input_list:
        if len(input_list) > 1 and i[0] == i[-1]:
            count_num += 1
    return count_num


x = number_of_string(input_list=list)
print(x)

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]


def check_common_number(input_list, input_list2):
    result = False
    for i in input_list:
        for j in input_list:
            if i == j:
                result = True

    return result


x = check_common_number(input_list=a, input_list2=b)
print(x)


def removing_even_num(input_list):
    new_list = []
    for i in input_list:
        if i % 2 != 0:
            new_list.append(i)
    return new_list


x = removing_even_num(input_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(x)

num = [1, 2, 3, 4, 5]
print(*num)

num = [1, 2, 3]
color = ['red', 'white', 'black']
for (a, b) in zip(num, color):
    print(a, b)

import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ', d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ', sorted_d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print('Dictionary in descending order by value : ', sorted_d)

# to add a key
d = {0: 10, 1: 20}
print(d)
d.update({2: 30})
print(d)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
d = dic1.copy()
d.update(dic2)
d.update(dic3)

print(d)

d = {'x': 10, 'y': 20, 'z': 30}
for dict_key, dict_value in d.items():
    print(dict_key, '->', dict_value)


#  generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

def making_dicct_contain_n_num():
    n = int(input("Enter the number "))
    d = dict()
    for x in range(1, n + 1):
        d[x] = x * x
    return d


print(making_dicct_contain_n_num())


# Write a Python script to print a dictionary
# where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

def Making_square():
    d = dict()
    for x in range(1, 16):
        d[x] = x * x
    return d


print(Making_square())

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)

d = {'Red': 1, 'Green': 2, 'Blue': 3}
for color_key, value in d.items():
    print(color_key, 'corresponds to ', d[color_key])

num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)
