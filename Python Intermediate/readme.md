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

# OOPS
**Classes** - A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.
**Objects** - An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.
*self* - self parameter is a reference to the current instance of the class. It allows us to access the attributes and methods of the object.
*__init__* - __init__ method is the constructor in Python, automatically called when a new object is created. It initializes the attributes of the class.

**Inheritance**
Inheritance allows a class (child class) to acquire properties and methods of another class (parent class). It supports hierarchical classification and promotes code reuse.

*Types of Inheritance:*

Single Inheritance: A child class inherits from a single parent class.
Multiple Inheritance: A child class inherits from more than one parent class.
Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
Hybrid Inheritance: A combination of two or more types of inheritance.

**Polymorphism** allows methods to have the same name but behave differently based on the object's context. It can be achieved through method overriding or overloading.

*Types of Polymorphism*

Compile-Time Polymorphism: This type of polymorphism is determined during the compilation of the program. It allows methods or operators with the same name to behave differently based on their input parameters or usage. It is commonly referred to as method or operator overloading.
Run-Time Polymorphism: This type of polymorphism is determined during the execution of the program. It occurs when a subclass provides a specific implementation for a method already defined in its parent class, commonly known as method overriding.

**Python Encapsulation**
Encapsulation is the bundling of data (attributes) and methods (functions) within a class, restricting access to some components to control interactions.

Types of Encapsulation:
*Public Members:* Accessible from anywhere.
*Protected Members:* Accessible within the class and its subclasses. e.g - _breed
*Private Members:* Accessible only within the class. e.g - __color

**Abstraction** hides the internal implementation details while exposing only the necessary functionality. It helps focus on "what to do" rather than "how to do it."

*Types of Abstraction:*

Partial Abstraction: Abstract class contains both abstract and concrete methods.
Full Abstraction: Abstract class contains only abstract methods (like interfaces).