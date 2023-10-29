"""Question: Write a program which will find all such numbers which are divisible by 7 but are not a
 multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
  comma-separated sequence on a single line."""


def find_num_divisible_by_7():
    # list and , seperated values [1,2,3,4]
    l = []
    for i in range(2000, 3201):
        if (i % 7 == 0) and (i % 5 != 0):
            # 5000 check 5 multiple ?
            l.append(i)
    return l


output = find_num_divisible_by_7()
print(output)

"""Write a program which can compute the factorial of a given numbers. The results should be 
printed in a comma-separated sequence on a single line. Suppose the following input is supplied
 to the program: 8 Then, the output should be: 40320"""

# def factorial_of_8(x):
#     if x ==0:


"""Question: With a given integral number n, write a program to generate a dictionary that contains 
(i, i*i) such that is an integral number between 1 and n (both included). and then the program should
 print the dictionary. Suppose the following input is supplied to the program: 8 Then, the output should be: 
 {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints: In case of input data being supplied to the question, it should be assumed to be a console
 input. Consider use dict()"""

def generate_square_of_keys(x):
    generated_dictionary={}
    for i in range(x+1):
        # print(i)
        generated_dictionary[i]=i*i
    return generated_dictionary

print(generate_square_of_keys(x=100))


""" Write a program which accepts a sequence of comma-separated numbers from console and generate a list
 and a tuple which contains every number. Suppose the following input is supplied to the program: 
 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] 
 ('34', '67', '55', '33', '12', '98')

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
 tuple() method can convert list to tuple"""

# def lsit_into_tuple(*input):
#     x= input()
#     l = x.split(",")
#     t = tuple(l)
#     return l,t
#
# print(lsit_into_tuple(x =32,43,45,76))