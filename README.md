# 8months-for-AI
I am starting the journey of AI for 8 months



contents of itertools 
Product:
product is a function from the itertools module that computes the Cartesian product of input iterables. It generates all possible combinations of elements from the input iterables, optionally repeating elements.

permutations:(it is in file itertools.py)
is a function from the itertools module that generates all possible ordered arrangements of a given iterable's elements. It is used to create permutations of a specific length.

Combinations:
combinations is a function from the itertools module that generates all possible combinations of a specified length from the elements of an iterable. Unlike permutations, the order of elements in combinations does not matter.

Accumulate:
is a function from the itertools module that is used to perform cumulative operations on an iterable. By default, it performs cumulative summation, but you can specify a custom function (e.g., multiplication, maximum, etc.) using the func parameter.

infinite iterators in python
infinite iterators are provided by the itertools module. These iterators generate values indefinitely, and you can use them with a for loop or other iteration tools. They are particularly useful when you need to generate an infinite sequence of values.Its types are 

count: Useful for generating infinite sequences of numbers, such as indices or timestamps.
cycle: Useful for cycling through a fixed set of values, such as alternating between two states.
repeat: Useful for repeating a constant value, such as a default parameter.



_______________________________________________________
lambda.py

lambda:
lambda is an anonymous function (a function without a name) that is defined using the lambda keyword. It is typically used for short, simple operations where defining a full function is unnecessary. syntax: 
                                lambda arguments: expression

map function
reduce function 
filter function and
sorted 

i covered above 
________________________________________________________

logging.py
Logging:
The logging module in Python is used to log messages that provide information about the execution of a program. It is a powerful tool for debugging, monitoring, and tracking the behavior of your application.


What Does Each Logging Level Mean?
The logging module provides several levels of severity for log messages:
DEBUG:
Used for detailed diagnostic information, typically useful for debugging.
Example: Variable values, function calls, etc.

INFO:
Used to confirm that things are working as expected.
Example: Application startup, configuration details, etc.

WARNING:
Indicates something unexpected happened or a potential problem.
Example: Deprecated features, missing files, etc.

ERROR:
Indicates a more serious problem that prevents part of the program from functioning.
Example: Exceptions, failed operations, etc.

CRITICAL:
Indicates a very serious error that may prevent the program from continuing.
Example: System crashes, database unavailability, etc.
