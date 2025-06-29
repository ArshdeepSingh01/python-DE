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