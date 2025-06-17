# Why python for Data Engineering?
Python is extensively used in data engineering for various tasks like data ingestion, transformation, and loading, as well as for building and orchestrating data pipelines. Its rich ecosystem of libraries like Pandas and NumPy, combined with its readability and ease of use, make it a popular choice for data engineers. 

# Data types

Python has the following data types built-in by default, in these categories:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

# Numbers 
There are three numeric types in Python:
**int** - Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
**float** -Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
Float can also be scientific numbers with an "e" to indicate the power of 10. Like 35e10
**complex** - Complex numbers are written with a "j" as the imaginary part:
Example
x = 3+5j


# Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.



# Lists
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
List items are **ordered, changeable, and allow duplicate** values.

It is also possible to use the list() constructor when creating a new list.
List methods
**Method	Description**
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

# Dictionaries
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

It is also possible to use the dict() constructor to make a dictionary.
items() returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.