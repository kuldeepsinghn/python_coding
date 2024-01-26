# Exception Handling in Python


## Exceptions: 
- In Python, exceptions are events that occur during the execution of a program that disrupts the normal flow of instructions.
## Error Handling:
- Exception handling is a mechanism to handle errors or exceptions gracefully, preventing them from causing the program to terminate abruptly.

- try:
    # Code block where exception may occur
-     <code>
- except <ExceptionType> as <alias>:
-     # Code block to handle the exception
-     <exception handling code>


- try Block: Contains the code where an exception may occur.

- except Block: Handles the exception raised in the try block. Multiple except blocks can be used to handle different types of exceptions.

- <ExceptionType>: Specifies the type of exception to handle. If omitted, it catches all exceptions.

- as <alias>: Assigns the exception instance to a variable for further processing


- example

- try:
-     x = int(input("Enter a number: "))
-     result = 10 / x
-     print("Result:", result)
- except ZeroDivisionError as e:
-     print("Error:", e)
- except ValueError as e:
-     print("Invalid input:", e)
- except Exception as e:
-     print("An error occurred:", e)
- else:
-     print("No exceptions occurred.")
- finally:
-     print("Execution completed.")


# Common Exception Types:

### ZeroDivisionError: Raised when division or modulo by zero occurs.

### ValueError: Raised when an operation or function receives an argument of the right type but an inappropriate value

### TypeError: Raised when an operation or function is applied to an object of an inappropriate type.

### FileNotFoundError: Raised when a file or directory is requested but cannot be found.

### IOError: Raised when an input/output operation fails (Python 2), or when there is an input/output error (Python 3).

### IndexError: Raised when a sequence subscript is out of range.

## Raising Exceptions in Python:-

- Raising Exceptions: In Python, developers can raise exceptions to indicate that an error or unexpected condition has occurred during the execution of a program.

- Explicit Error Signaling: Raising exceptions allows developers to explicitly signal errors or exceptional conditions, which can be caught and handled by the calling code or higher-level components.


- raise Statement: Used to raise an exception.
- <ExceptionType>: Specifies the type of exception to raise. This can be a built-in exception class or a custom exception class derived from the Exception class


- <optional_message>: Optional message providing additional information about the error.

### Using with for Resource Management in Python

## Context Managers:-
-  The with statement in Python is used for resource management, providing a convenient way to ensure that resources are properly acquired and released.

## Automatic Cleanup:-
- Using with ensures that resources are automatically released when they are no longer needed, even if an exception occurs within the with block.

### Benefits:
- Automatic Cleanup: Resources are automatically released when they go out of scope, even if an exception occurs.

- Readability: with statement improves code readability by clearly defining the scope in which resources are used.

- Error Handling: Provides built-in error handling capabilities, ensuring proper cleanup even in the presence of exceptions.


