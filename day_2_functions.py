# def find_even_numbers(num):
#     print(f"finding even numbers in list {num}")
#     evens = []
#     for i in range(num + 1):
#         if i % 2 == 0:
#             evens.append(i)
#
#     return evens


# def even_number(list):
#     new_list=[]
#     for i in list:
#         if i % 2 == 0:
#             new_list.append(i)
#
#     return new_list
#


# def length_ages(ages):
#     return len(ages)
#
#
def average_num(ages):
    total = 0
    for i in ages.values():
        total += i

    total_val = total / len(ages)
    return total_val


def total_students(students):
    total_length = len(students)

    return total_length


def average_age_students(students):
    total = 0
    for i in students:
        total += i

    average_ = total / len(students)

    return average_
