count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:  # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)  # the numbers will be printed line by line, from 0 to 5

language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)  # this way we get both keys and values printed out

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print(
        "loop's end")  # for short hand conditions need both if and else statements
print('outside the loop')

lst = list(range(11))
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))  # 2 arguments indicate start and end of the sequence, step set to default 1
print(st)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0, 11, 2))
print(lst)  # [0, 2, 4, 6, 8, 10]
st = set(range(0, 11, 2))
print(st)  # {0, 2, 4, 6, 8, 10}

for number in range(11):
    print(number)  # prints 0 to 10, not including 11

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

for number in range(6):
    pass

count = 0
while count < 11:
    print(count)
    count = count + 1
# prints from 0 to 4


for i in range(11):
    print(i)

count = 0
while count < 4:
    print(count)
    count = count + 1
else:
    print(count)

for i in range(10, 0, -1):
    print(i)


def missing_number():
    list = [1, 2, 3, 4, 5, 6, 7, 9, 10]
    n = 10
    total = 0
    sum = 0
    sum = (n * (n + 1)) / 2
    print("sum", sum)
    for x in list:
        total += x
    print("total_sum_of_list", total)

    missing_num = sum - total
    print("missed_num in list ", missing_num)


missing_number()

number = (int(input("Enter a number")))
for i in range(11):
    print(i, "x", i, "=", i * i)


# for i in range(101):
#     if i % 2 == 0:
#         print(i)
#
# for i in range(101):
#     if i % 2 != 0:
#         print(i)
#
# sum = 0
# for i in range(101):
#     sum += i
#     print(sum)
#
# sum = 0
# for i in range(101):
#     if i % 2 == 0:
#         sum += i
#         print(sum)


def triangle(n):
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("#", end="")

        # ending line after each row
        print("\r")

    # Driver Code


n = 7
triangle(n)


def unique_list(lis):
    x = []
    for i in lis:
        if i not in x:
            x.append(i)
    return ("the new unique list is =", x)


print(unique_list(lis=[1, 2, 3, 3, 3, 3, 4, 6, 6, 5]))
