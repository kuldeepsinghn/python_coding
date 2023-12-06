# Memory Mangement
- In python memory management is totally automatic.

## two scripts
- 1. Python Memory Manager:- allocation of memory
- 2. Python Garbage Collector :- de-allocation


## Two parts :-

### 1. Memory Allocation
### 2. Memory De-allocation
- When an object is no longer needed, its memory is deallocated. This process is typically automatic due to the combination of reference counting and garbage collection.

### 1. Memory Allocation
-Memory allocation is the process of reserving a block of memory for a specified purpose, typically to store data during the execution of a computer program.
- When you create objects in Python (e.g., variables, lists, objects of custom classes), memory is allocated to store the data associated with those objects
- The Python memory manager handles this allocation process.
#### There are two types of memory:-

##### 1. Stack Memory or static memory
- stack memory is slow compare to dynamic memory 
- directly accessed
- memory allocation for global references and  for function call and names 
- in stack memory there is no memory allocation for objects and values
- In static memory allocation, memory is allocated at compile time.
- The size of memory required is known at the time of program compilation.
- Memory is assigned to variables and data structures before the program starts executing.
- This type of allocation is common in languages like C, where you declare variables with fixed sizes.

- eg:-
- ![Alt text](D:\git_hub\sql\stack_memory.png)

- 
##### 2. Heap or Dyanmic Memory
- dynamic or heap memory is fast as compare to stack memory
- it is not directly accessed to accessed dynamic we use references and variables 
- in this heap memory, memory allocation is done for all values and objects
- it is allocated by interpreter, and it is managed by the interpreter.
- The size of memory required may not be known until the program runs.
- It allows for flexibility in managing memory based on the program's needs.
- In dynamic memory allocation, memory is allocated at runtime during program execution
- ![Alt text](D:\git_hub\sql\heap_memory.png)


### python garbage collector 
- it means removing objects which having no references.
- it is just a script which is used to remove the following type of object
- x= 7 # it removes for python garbage collector
- x=9
- print(x) # 9

#### it uses below two algorithm
- 1. Reference counting algo
- 2. Tracing


## 1.Reference counting 
- Python uses a reference counting mechanism to keep track of how many references (pointers) exist to an object
- Each object has a reference count
- when this count drops to zero, the memory occupied by the object is deallocated
- number of names pointing to an object
- ref-count -->used to track 
- if new reference created count Increment
- reference removed count Decrement
  - x -> 10
  - y ->10 this object having two tags # ref-count = 2
  - z -> 10 ref-count =2+1

- if reference count is zero then it calls to garbage collecter then garbage collecter delete that object


### what make references
#### 1.creating a object
#### 2.giving new name to object
#### 3.adding object in data structure
#### 4.passing in function



### what remove references
- assignment of new object to name like x=10, x=20
- when variables goes out of scope 



#### advantages
- easy to implement
- clear memory immediately when ref-count =0

#### disadvantages
- space require to store count
- if execution is overhead then it needs everytime to update it internally 
- cascading effect



### Traces Algorithm:-

- it comes in picture when memory is full 
- mark and sweep principle
  - mark:- mark reachable references
  - sweep:- remove marked object