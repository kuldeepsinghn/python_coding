# def multiply(numbers):
#     total = 1
#     for x in numbers:
#         total *= x
#     return total
#
#
# print(multiply((8, 2, 3, -1, 7)))
#


# check how many times duplicates value occur
def count_duplicates(my_list):
    duplicates = []# empty list

    for item in my_list:
        if my_list.count(item) > 1 and item not in duplicates:
            duplicates.append(item)

    for item in duplicates:
        count = my_list.count(item)
        print(f"{item} occurs {count} times in the list.")
        # print()

    return duplicates


print(count_duplicates(my_list=[1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 10, 11, 11, 11, 11, 11]))
