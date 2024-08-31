# Variable Names

# Variables names
# must start with a letter or the underscoreCharacter
# cannot start with a number
# can only contain alpha-numeric characters and underscores
# are case-sensitive
# cannot be Python keywords

# Legal names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal Names
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Variable names with more than one word can be difficult to read
# Some comment coding practices to help read long variables is to use camel case
# Pascal Case?
# Snake Case

# Many values to multiple variables

x,y,z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One values to multiple Variables
# You can assign the same value to multiple variables in one line

x = y = z = "Orange"

# Unpack a Collection

# if you have a collection of values or tuples python allows us to extract the values into variables
fruits = ["apples","banana","cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables

x = "Python is awesome"
print(x)

# We can print multiple variables when they are separated by ,
x = "Python "
y = "is "
z = "awesome "
print(x,y,z)

# You can use the + operator to output multiple variables
x = "Python "
y = "is "
z = "awesome "
print(x+y+z)

# For numbers the + character will work as a mathematical operator
x = 5
y = 10
print(x+y)

# When trying to combine a string and number python will return an error
x=5
y="John"
# print(x+y)

# The best way to output multiple variables in print is to seperate with commas which ever supports different data types
x = 5
y = "John"
print(x,y)

print('Hello' , 'World')

# Global Variables  
# Variables created outside a coding block/scope are global variables
# These global variables like other languages can be used by any functions that proceed it
# 

x="awesome"

def myfunc() :
    print("Python is " + x)

myfunc()

# If you create a variable with the same name inside a function this variable will be local and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the orignal value

x = "awesome"

# overwrite our previous function
def myfunc() :
    # overwrite x 
    x = "fantastic"
    print("Python is "+ x)

myfunc()
print("Python is "+ x)

# The global keyword

# Normally when you create a variable inside a function, that variable is local and can only be used within

# To create a global variable we use the global keyword

def myfunc():
    global y
    y = "fantastic"

myfunc()

print("Python is " + y)
