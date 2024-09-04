# Python Ty Except

# THe try block lets us test a block of code for error
# The except block lets you handle the error
# The else block lets you execute coe when there is no error
# The finally block lets you execute code, regardless of the result of the try- and except blocks

# Exception Handeling

# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:

# The try block will generate an exception, becuase x is not defined

try:
    print(x)
except:
    print("an exception occurred")

# Since the try block raises an error, the except block will be executed
# Without the try block, the program will crash and raise an error:

# Many Exceptions
# You can define exception blocks as you want, e.g. If you want to execute a special block of code for a special kind of error:

# Print one message if the try block raises a NameError and another for other errors:

try:
    print(x)
except NameError:
    print("Variable x is not defined!")
except:
    print("Something else went wrong!")

# Else

# You can use the else keyword to define a block of code to be executed if no errors were raised:
# In this example, the try block does not generate any error:

try:
    print("Hello!")
except:
    print("Something went wrong!")
else:
    print("NOthing went wrong!")

# Finally
# The finally block, is specified, will be executed regardless if the try block raises an error or not

try:
    print(x)
except:
    print("Something went wrong!")
finally:
    print("The 'try except' is finished!")

# The can be useful to close objects and clean up resources
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file!")

# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs. 
# To throw (or raise) an exception, use the raise keyword.

# Raise an erro and stop the program if x is lower than 0:

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero!")

# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.

# Raise a TypeError is not an integer:

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed!")

