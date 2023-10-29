# Write a Python function that takes a list of strings as input, and then
# returns the longest string in the list.
# output = [ 'banana', 'orange']
input_list = ['apple', 'banana', 'kiwi', 'orange', 'pear']


def longest_string(input_list):
    max_length_string = 0
    # str_varibale = None
    new_list = []
    for i in input_list:
        if len(i) >= max_length_string:
            max_length_string = len(i)

    for x in input_list:
        if len(x) == max_length_string:
            new_list.append(x)

    return new_list


largest_string_in_list = longest_string(input_list=input_list)
print(largest_string_in_list)

input_dict = {}
input_dict['apple'] = 5
input_dict['banana'] = 6
input_dict['kiwi'] = 4
input_dict['orange'] = 6
input_dict['peer'] = 4
print(input_dict)


def largest_string(input_dict, n):
    new_dict = {}
    for name, length in input_dict.items():
        if length == n:
            new_dict[name] = length
    return new_dict


name_of_largest_string = largest_string(input_dict=input_dict, n=6)
print(name_of_largest_string)
