# Functions in Python
## what is function
- it is a reusable code that is used to perform single or specified task
- it runs when we call the function
-passes data in a function is called parameter
- functions returns data as output or result
## uses
- divide problems into small problems and make program easy.
- avoid rewriting of code
- make reusabilty of code 
- call function anywhere in python
- program divided into multiple function
## types of functions

### built in function
- those functions that are already built and available to use
- len(), str(), int(), float(), range(), max(), min(), sum(), open(), sorted(), and type()
### user defined
- those functions which we can create our own fucntion based on our requirement


### creating a function

- def - (keyword )
- function_name - (any name given to the function)
- arguments - (any value passed to function)
- return - (returns value from a function)


-eg:-  def my_function():
- print("Hello from a function")


### calling function
-  after the creation we call the fucntion by its name "my_function()" with parenthesis that contain parameter of function
- 
- def my_function():
-  print("Hello from a function")

- my_function()


- call function with no parameters
-  call function with 1 parameter
- def greetings(name):
-    message = name + ', welcome to Python for Everyone!'
-    return message


- print(greetings('Asabeneh'))

-
- call function with many parameter
- def sum_two_numbers(num_one, num_two):
-    sum = num_one + num_two
-    return sum


- print('Sum of two numbers: ', sum_two_numbers(1, 9))
- 
- 


### parameter
- name of data
- 
### arguments
- data or information passed inside the parenthesis
#### default arguments
- it is a parameter that assumes a default value if value is not provided
- def my_function(country = "Norway"):
-   print("I am from " + country)

- my_function("Sweden")
- my_function("India")
- my_function()
- my_function("Brazil")
- 
- 
#### keyword arguments
- it is a arguments that is used to call the specific argument name with value
-def print_fullname(firstname, lastname):
-   space = ' '
-    full_name = firstname + space + lastname
-   print(full_name)


- print(print_fullname(firstname='Asabeneh', lastname='Yetayeh'))



- def add_two_numbers(num1, num2):
-     total = num1 + num2
-     print(total)


- 
- print(add_two_numbers(num2=3, num1=2))
 
-
-
#### postional argument
- it is used to check the position of argument 



 

### return value
- it is always use to exit from a function
- it return the specified value or data of fucntion
- return many value

- def my_function(x):
-   return 5 * x

- print(my_function(3))
- print(my_function(5))
- print(my_function(9))

### doc string
- the first written in function after the function and it describe the fucntionality of function
- syntax - print(function_name.__doc__)
- the above syntax to print the doc string of function
- 
### assign function name into variable 


- def remove_items(lst, item):
-     lst.remove(item)
-     return lst


- lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
- x =(remove_items(lst, item=7))
- print(x)




- def unique_list(lst):
-     new_lst = []
-    for a in lst:
-        if a not in new_lst:
-           new_lst.append(a)
-    return new_lst


- print(unique_list(lst = [1, 2, 3, 3, 3, 3, 4, 5]))




### pass statement
- if fucntion have no content then we use pass fucntion to avoid error

- def myfunction():
-   pass