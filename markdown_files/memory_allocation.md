# Memory Mangement
- In python memory management is totally automatic.

- In Python, memory allocation and garbage collection are managed automatically by the Python interpreter using a combination of mechanisms

## Memory Allocation:
- Dynamic Allocation: Python dynamically allocates memory for objects as needed.
- Objects: Memory is allocated for variables, lists, objects, etc., as they are created.
- Automatic: Allocation is handled automatically by the Python interpreter

## Garbage Collection:
- Reference Counting: Python uses reference counting to track the number of references to an object.
- Increment/Decrement: Reference count is incremented when an object is referenced and decremented when a reference goes out of scope or is deleted.
- Deallocation: When the reference count reaches zero, the object is deallocated.

### Reference Counting:

- Python uses a reference counting mechanism to keep track of the number of references to an object.
- Each object has a reference count indicating how many references point to it.
- Reference counts are automatically updated as references are created or removed. Cycle Detection:

- Reference counting alone cannot handle cyclic references where objects refer to each other in a loop.
- Python's garbage collector detects and breaks such reference cycles to ensure proper deallocation of memory.

## Mechanisms:
- Automatic: Python automatically manages memory allocation and deallocation.
- Garbage Collector: Python's garbage collector periodically sweeps through memory to reclaim objects with zero reference counts.
- Efficient: Handles circular references and reference cycles.


### Garbage Collector:

- Python also employs a garbage collector to reclaim memory from objects with zero reference counts.
- The garbage collector periodically runs to identify and deallocate objects that are no longer in use.
- It traverses the object graph, starting from a set of roots (e.g., global variables, local variables, etc.), and identifies unreachable objects, which are then deallocated.




## Python:
### Dynamic Typing:

- Python: Dynamically typed language where variable types are inferred at runtime.
- C: Statically typed language where variable types must be declared at compile time.
- Automatic Memory Management:
