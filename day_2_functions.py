def find_even_numbers(num):
    print(f"finding even numbers in list {num}")
    evens = []
    for i in range(num + 1):
        if i % 2 == 0:
            evens.append(i)

    return evens


def even_number(list):
    new_list=[]
    for i in list:
        if i % 2 == 0:
            new_list.append(i)

    return new_list



def length_ages(ages):
    return len(ages)



def average_num(input_dictionary):
    print("input is this", input_dictionary)
    input_dictionary['xx'] = 11
    total = 0
    for i in input_dictionary.values():
        total += i

    avg_val = total / len(input_dictionary)
    return avg_val


#
def total_students(students):
    total_length = len(students)

    return total_length
#
#
def average_age_students(students):
    sum = 0
    for key, value in students.items():
        for x, y in value.items():
            if y and 'age' in y.items():
                print()
                sum += y['age']
            return sum

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}


def oldest_person(ages):
    max_age = 0
    for x, y in ages.items():

        if y > max_age:
            max_age = y
            x = max_age
    #         max_age=10 ,new_dict={'peter' :10}
    #         max_age=11 ,new_dict={'isabel' :11}
    return x

#


def function(ages, n):
    new_ages = {}
    for name, age in ages.items():
        # print(x, y)
        if age == n:
            new_ages[name] = age
    return new_ages



def function_2(students, x):
    new_dict = {}
    for p, q in students.items():
        # print(x, y)
        for a, b in q.items():
            # print(a, b)
            if x == b:
                new_dict[p] = b
    return new_dict
