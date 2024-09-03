# Python Modules

# What is a module

# We consider modules to be the same as coding libraries
# A file containing a set of functions you want to include in your application.

# Create a module

# To create a module just save the code you want in a file extension .py:

# def greeting(name):
#     print("Hello, " + name)


# Use a module

# Now we can use the module we just created, by using the import statement

import mymodule

mymodule.greeting("Johnathan")

# When using a function from a module, use the syntax: module_name.function_name


# Variables in module

# THe module can contain functions, as already describer, 
# but also variables of all types (arrays, dictionaries, objects)

# Save this code in the file mymodule.py

import mymodule

a = mymodule.person1["age"]

# Naming a Module

# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module

# You can create an alias when you import a module, by using the as keyword:

import mymodule as mx # change import module name to mx so when used we can call it using mx instead of mymodule

a = mx.person1["age"]
print(a)


# Built-in Modules

# There are several built-in modules in Python, which you can import whatever you like.

# Import and use the platform module:
import platform

x = platform.system()
print(x)

# Using the dir() function

# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

# List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)

# The dir() function ca be used on all modules

# Import From Module

# You can choose the import only parts from a module, by using the form keyword:
# The module named mymodule has one function and on dictionary

# Import only the person1 dictionary from the module

from mymodule import person1

print(person1["age"])

# When importing using the from keyword, do not use the module name when referring to elements in the module.




