# Python For Loops

# A for loop is used for iterating over a sequence (That is either a list, a tuple, a dictionary, a set, or a string)

# Thi is less like the for keyword in other programming languages, and works more like an iterator

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# The for loop does not require indexing variable set beforehand

# Looping Through a String

# Even strings are iterable objects, they contain a sequence of ahcaracters

# loop through the word banana

for x in 'banana':
    print(x)


# The break statement

# the bvreak statement can stop the look before it has finish looping through all the items

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
    if(x == 'banana'):
        break

# Exit the loop when x is banana but this time the break comes before the print
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == 'banana':
        break
    print(x)

# The Continue Statement

# With the continue statement we can stop the current iteration of the loop, and continue with the next:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue # continue skips any code that proceeds this lines and continues to next index in the loop or item since sets or not indexed and neither are tuples
    print(x)

# The range() function

# To loop through a set of code a specified number of times, we can use the range() function

# The range() function returns a sequence of numbers, start from 0 from default and increments by 1, and ends at a specified number

for x in range(6):
    print(x)

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5

# The range () function defaults to 0 as string value, however it is possible to specify the starting value by adding a parameter: range(2,6),
# which means values from 2 to 6 (but not including 6)

for x in range(2,6):
    print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify increment value by adding a third parameter

range(2, 30, 3)

# Else in for loop

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for x in range(6):
    print(x)
else:
    print("Finally finished!")

# The else block will not be executed if the loop is stopped by a break statement

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

# Nested Loops

# A nested loop is a loop inside a loop

# The "inner loop" will be executed on time for each iteration of the "outer loop"

# print each adjective for every fruit

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

# The Pass Statement

# for loops cannot be empty, but if you for some reason have a for loop 
# with no content, put in the pass statement to avoid getting an error

for x in [0,1,2]:
    pass