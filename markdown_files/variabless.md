# Variable in python 
## what is variable 
- variable is the name attached to a value which can be changed and is used later in code
- no need to declare before use it
- x= 10 # 10 assign in variable 
- y=20
- x + y = 30
- value of variable can be changed later in the code
-
x = 40

  x+y = 60
- in  python the type of variable is no need to specify in advance because python automaticelly known the type of variable by seeing variable store in variable at it runtime is called dynamic typing  
- the variable can be store any type of value its lifetime duration
- in python variable are dynamic


## Variable  naming convention
- variable name can contain only letter, number and underscores.
- not allow special character
- eg :- x_1 = 10 --> correct
- x@12 = 10 --> show error
- 
- variable can be start with _, name but not with number
- _x=10
- 1x = 10 --> invalid 

- not use of space
- variable name should be short or descriptive
- they are case-sensitive
- X =10
- x = 10  # these two variables are different
- multi-word word variable can be any of the following convention
- 1- camel case convention --> means second word should be captiallised
- eg:- studentName
- 2- pascal case convention --> same as camel case but first letter of first word is also capitalised
- eg:- StudentName
- 3- snake case convention --> words are seperated with underscore
- eg:-student_name


## Chained assignment of variable 
- it helps us assign same value to multiple variables in same line
- x=y=z = 10
- x+y+z = 30 


## variable scope
- meaning of scope of variable is its lifetime in program.
- The scope of a variable in python is that part of the code where it is visible.
- scope of variable is block of code in entire program where we declare , used and can be modified variable

- eg:-
- b=8 --> global variable
- def func():
-     a=7 --> local variable
-     print(a) 
-     print(b)             
- func() # here i am calling the function and output is >> 7 , 8
### there are four types of scope in python 
- 1- Local Scope
- 2- Global Scope
- 3- Enclosed scope
- 4- built-in scope


- 1- Local Scope :-
- variable created inside the function and belongs to local scope of that function.
- the local variable can be accessed from a function within the function
- eg:- 
- def myfunc():
-   x = 300
-   def myinnerfunc():
-     print(x)
- myinnerfunc()

- myfunc()
- in above code  i am define "a" inside the function so  variable "a" is local scope of function hence we can read write the variable inside the function, but not outside.
- a=0
- def func():
-     print(a) --> it gives error because we trying to access the local scope a before assign it  
-     a=7 --> local variable
-     print(a)  
- func()

- 2- Global Scope:- 
- It is a variable which is created in main body of code is a global variable and belongs to global scope
- A variable created outside a function is global and can be used by anyone
- eg:-
- x = 300

- def myfunc():
-     print(x)

- myfunc()

- print(x)                                

#### global keyword:-
- it is keyword it is used when we need to create global variable, but we stuck in local so use global key word.
- it is make variable global.
- if you use global keyword the variable belongs to global scope.
- eg:- def myfunc():
-         global x
-         x = 300

- myfunc()

- print(x) # x= 300

- use the global keyword if you want to make a change to a global variable inside a function
- x = 300

- def myfunc():
-   global x
-   x = 200

- myfunc()

- print(x) # x =200

- 3- Enclosing scope :-
- def red():
-               a=1
-               def blue():
-                              b=2
-                               print(a)
-                               print(b)
-               blue()
-               print(a)
-  red()
- In this code, ‘b’ has local scope in Python function ‘blue’, and ‘a’ has nonlocal scope in ‘blue’.
- a python variable scope that isn’t global or local is nonlocal. This is also called the enclosing scope.


- 4- Built-in scope :-
- it is the widest scope 
- it has all the names that are loaded into python
- eg:- global keyword
- non-local keyword


