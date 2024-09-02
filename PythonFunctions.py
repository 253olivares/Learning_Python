# Python Functions

# A function is a block of code which only runs when it is called
# You can pass data, known as parameters, into a function

# A function return data as a result


# Creating a function

# In Python a function is defined using the def keyword

def my_function():
    print("Hello from a function!")

# Calling a function

# To call a function, use the function name followed by parenthesis:

def my_function():
    print("Hello from a function")

my_function()

# Arguments

# Information can be passed into functions as arguments

# Arguments are specified after the function name, inside the parentheses. You can add
# as many arguments as you want, just separate them with a comma.

# THe following example has a function with one argument (fname). when the function is called, we pass
# along a first name, which is used inside the function to print the full:

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Arguments are often shortened to args in Python documentations

# Parameters or Arguments
# The terms parameter and argument can be used for the same thing: 
# information that are passed into a function

# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if you function expects 2 arguments you have the call the function with 2 arguments, not more, and not less

# This function expects 2 arguments and get 2 arguments

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")

# If you try to call the function with 1 or 3 arguments, you will get an error

# my_function("Emil") Will throw an error if we provide less arguments than parameters

# Arbitrary Arguments, *args

# If you do not know how many arguments that will be passed into your function, add a * 
# before the parameter name in the function definition.

# This way the function will receive a tuple of  arguments, and can access the items accordingly:

def my_function(*kids):
    print("THe youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Arbitrary Arguments are often shortened *args in Python Documents

# Keyword Arguments

# You can also send arguments with the key = value syntax
# This way the order of the arguments does not matter

def my_function(child1, child2, child3):
    print("The youngest child is" + child3)

# if we have set values we an decide in which order they can be added
my_function(child1="Emil", child2="Tobias", child3="Linus")

# The phrase Keyword Arguments are often shortened to kwargs in Python documentations

# Arbitrary Keyword Arguments, **kwargs

# If you do not know how many keywords that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.

# This way the function will recieve a dictionary of arguments, and can acces the items accordingly

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "tobias", lname = "Refsnes")

# Default Parameter Value

# The following example shows how to use a default parameter value

# If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument

# You can send a data types of argument to a function (string, number, list, dictionary)
# It will be treated as the same data type inside the function

# If you send a list as an argument, it will be a list when it reaches the function:

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values

# To let a function return a value, use the return statement:

def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement

# function definitions cannot be empty, but if you for some reason have a 
# function definition with no content, put in the pass statement to 
# avoid getting an error

def my_function():
    pass

# Positional-Only Arguments

# You can specify that a function can have ONLY 
# positional arguments, or ONLY keyword arguments 

# To specify that a function can have only positional arguments, add ,/ after the arguments

def my_function(x,/):
    print(x)

my_function(3)
# This means specifying a value for a value will throw an error

# my_function(x = 3) // throw error

# Keyword-Only Arguments

# To specify that a function can have only keyword arguments, add *, before the arguments

def my_function(*,x):
    print(x)

my_function(x=3)

# my_function(3) This will now throw an error


# Combine Positional-Only and Keyword-Only

# You can combine the two arguments types in the same function

# Any argument before the /, are positional-only and any arguments after the *, are keyword only

# Combining both will look like

def my_function(a,b, /, *,c,d):
    print(a + b + c + d)

my_function(5,6,c = 7, d = 8)

# Recursion

# Python also accepts function recursion, which means a defined 
# function can call itself.

# Recursion is a common mathematical and programming concept. It means that a function calls itself.
# This has the benefits of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be quite easy to 
# slip into writing a function which never terminates, or one that uses excess 
# amounts of memory or processor power. However, when written correctly recursion 
# can be very efficient and mathematically-elegant approach to programming.

# Om this example, tri_recursion() is a function that we have defined to call 
# itself ("recurse"). We use the k variable as the data, which decrements (-1)
# every time we recurse. The recursion ends when the condition is not greater than 0.

# To a new developer it can take some time to work out how exactly this works, best way 
# to find out is by testing and modifying it.

def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
    
print("\n\nRecursion Example Results")
tri_recursion(6)
