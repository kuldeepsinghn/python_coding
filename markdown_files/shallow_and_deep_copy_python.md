- num = 100
- num1 = num (incorrect way of copying)
- my_list = [1,2,3,4]
- new_list= my_list  # new_list is copy

- my_list=[[1,2,3],[4,5],[6,'a']]
- figure 1
- memory allocation of nested list 
- ![Alt text](D:\git_hub\sql\memory_allocation_of_nested_list.png)

## There are two ways to create copies:
### 1. Deep Copy
### 2. Shallow copy


### shallow copy :-
- A shallow copy creates a new object
- but instead of copying the elements recursively, it copies only the references to the objects
- means the outer container is duplicate but the inner objects are still prefrences as same as original
- 
- first import copy module
- for shallow copy we just use copy fucntion
- in actual shallow copy make affect on our orginal

- mylist =[[1,2,3],[4,5],[6,'a]] 
- changes in one is affecting the other one
-  ![Alt text](D:\git_hub\sql\shallow_copy.png)
-  

- so basically shallow copy is not the best option of copying 
- Use shallow copy when you want a new object but don't need complete independence for nested objects



- eg:
- import copy

- original_list = [[1, 2, 3], [4, 5, 6]]
- shallow_copied_list = copy.copy(original_list)

- original_list[0][0] = 'X'

- print(original_list)       # Output: [['X', 2, 3], [4, 5, 6]]
- print(shallow_copied_list) # Output: [['X', 2, 3], [4, 5, 6]]



## Deep Copy
- A deep copy creates a completely independent copy of the original object 
-  It recursively copies all objects found in the original, creating a new object structure.
- in deep each and every nested element create a copy 
- in this memory address are differnt to each other
- it creates completely new copies

#### Module: In Python, you can create a deep copy using the copy module's deepcopy() function

- import copy

- original_list = [[1, 2, 3], [4, 5, 6]]
- deep_copied_list = copy.deepcopy(original_list)

- original_list[0][0] = 'X'

- print(original_list)      # Output: [['X', 2, 3], [4, 5, 6]]
- print(deep_copied_list)   # Output: [[1, 2, 3], [4, 5, 6]]

- Use deep copy when you want a completely independent copy of both the outer and inner objects.


#### Key Differences:

##### Behavior on Nested Objects:
- Shallow copy only creates copies of the outermost container, leaving inner objects as references.
- Deep copy creates copies of both the outermost container and all nested objects, creating a fully independent copy

