# Python packages
Packages are way to organize code in a reusable and clean manner by grouping modules into directories.

*Components of a package*
1. Module: A single Python file containing reusable code (e.g., math.py).
2. Package: A directory containing modules and a special __init__.py file.
3. Sub-Packages: Packages nested within other packages for deeper organization.

*How to create a package*
1. Create a directory
2. Create modules in this directory with each module with specific functionality.
3. Include __init__.py to mark the directory as package
4. You can add sub-packages as well with seperate __init__.py files.
5. Import package using dot notation, e.g., from mypackage.module1 import greet

*Some useful defs*
A module is a single file containing code (functions, classes, variables) that can be imported and reused in other programs.

A library is a collection of related modules, often providing a larger set of functionalities.

# List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Exception handling

Exception handling handles errors during the execution of a python program. 
**try** block runs the code which performs your operations
**except** blocks handle errors.
**else** block runs if no exception occurs, displaying the result.
**finally** block runs regardless of the outcome, indicating the completion of execution.

# File Handling
File handling refers to the process of performing operations on a file such as creating, opening, reading, writing and closing it, through a programming interface. 

# Functions
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.

# Lambda function
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.