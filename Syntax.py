import sys

print(sys.version)

# Indenting signifies blocks of code so a if else block
if 15>2:
    print("Five is greater than two!")

# When indenting you have to use
if 15>2 :
    print("print 1")
    print("This will work cuz its the same indent line as the previous!")
        # print("This will not work on a different indent as now it is a new block of code")
    if 5<2:
        # to indent on a new line we need to precede code with a new if statement to signal we are writing a new block
        print("5 is not less than 2")

# Python Variables
# To create a variable in python we just need to type the variable name and assign it.
x =5
y = "Hello World"

# Something to note about python compared to other coding languages is that is has no comment for declaring variables