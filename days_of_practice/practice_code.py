"""Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list
and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98
Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

Hints: In case of input data being supplied to the question, it should be assumed to be a console input. tuple()
 method can convert list to tuple"""

# input_numbers = input("Enter a sequence of comma-separated numbers: ")
# numbers_list = input_numbers.split(',')
# numbers_tuple = tuple(numbers_list)
# print(numbers_list)
# print(numbers_tuple)

"""
 Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
 such that is an integral number between 1 and n (both included). and then the program should print the dictionary. 
 Suppose the following input is supplied to the program: 8 Then, the output should be: 
 {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict()
"""


def sqaure_root(n):
    result_dict = {i: i * i for i in range(1, n + 1)}
    return result_dict


print(sqaure_root(n=7))

"""Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: Consider use range(#begin, #end) method"""


def number_divisible_by_n(n, n1):
    result_list = []
    for num in range(2000, 3201):
        if num % n == 0 and num % n1 != 0:
            result_list.append(num)
    return result_list


print(number_divisible_by_n(n=7, n1=5))


def get_second_largest(nums):
    largest = nums[0]
    second_largest = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest


my_nums = [44, 11, 83, 29, 25, 76, 88]
second_largest = get_second_largest(my_nums)
print("Second highest number is : ", second_largest)


def get_second_smallest(nums):
    smallest = nums[0]
    second_smallest = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]
        elif nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest


my_nums = [44, 11, 83, 29, 25, 76, 88]
second_smallest = get_second_smallest(my_nums)
print("Second smallest number is : ", second_smallest)


def square_sum(num):
    sum = 0
    for i in range(num + 1):
        square = (i ** 2)
        sum = sum + square

    return sum


num = int(input('Enter a number: '))
sum = square_sum(num)

print('sum of square numbers is ', sum)

# palindrome numbers

my_str = input('String to check: ')
rev_str = my_str[::-1]

if my_str == rev_str:
    print("It is palindrome")
else:
    print("It is not palindrome")


# cubes in dictionary

def cube_sum(num):
    sum = 0
    for n in range(num + 1):
        sum = sum + n ** 3
    return sum


user_num = int(input('Enter a number: '))
result = cube_sum(user_num)
print('Your sum of cubes are: ', result)


# count vowels of given word

def count_vowels(word):

    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in word:
        if i in vowel:
            count += 1
    return count

user_word= input("Enter any word")
number_of_vowels=count_vowels(user_word)
print(f"there are {number_of_vowels} in word")


# count constants in word

def count_constant(word):

    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in word:
        if i not in vowel:
            count += 1
    return count

user_define = input("eneter a word")
print(count_constant(user_define))

print("hello")