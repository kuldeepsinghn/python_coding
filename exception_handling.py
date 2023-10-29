num = int(input("enter the number"))
print(f"Multiplication of {num}")
try:

    for i in range (1,11):
        print(f"{int(num)}x{i}= {int(num)*i}")
except:
    print('invalid input')


print("this is very important line ")
print("End of program ")


try:
    number = int(input("enter a number"))
    a =[2,3]
    print(a[num])
except ValueError:
    print("the value you entered is not integer ")
except IndexError:
    print("Index Error")

numbers_list= [1,2,33,3,4,5,6,8,9,9]
even_count = 0
odd_count = 0

for num in numbers_list:
    if num % 2 == 0:
        even_count += 1
    if num %2 !=0:
        odd_count += 1
print(odd_count)
print(even_count)

# return even_count, odd_count