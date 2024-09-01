# Python Tuples

mytuple = ("apple", "banana", "cherry")

# Tuples are used to store mulitple items in a single variable

# Tuple is one of 4 built in data types in Python used toi store collections of data, the other 3 are list, set, Dictonary
# all with different qualities and usage

# A tuple is a collection which is order and unchangeable

# Tuples are written with rounded brackets

thistuple = ("apple", "banana", "cherry")

print(thistuple)

# Tuple Items

# Tuples items are ordered, unchangeable, and allow duplicate values

# Tuple items are indexed, the first item has index [0], the second item has index [1] etx


# Ordered
# Tuples have defined order that can not be changes

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length
# To determine how many items tuple have, use the len() like with a list

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# create tuple with one item

# To create a tuple with only one item you have to add a comma after the item, otherwise python will no recognize it as a tuple
thisTuple = ("apple",) # without the comma creating a tuple with only one variable does not work
print(type(thisTuple))

# Tuple items - Data Types
# Tuple items can be of any data type

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1,2,3,5,7)
tuple3 = (True, False, False)

# A tuple can contain different data types

tuple1 = ("abc", 34, True, "male", 40)

type()

# From pythons perspective, Tuples are defined as objects with the data type "tuple"

# What is the data type of a tuple
mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) # Tuple has its own data type

# The Tuple Constructor

# It is also poissible to use the tuple() constructor to make a tuple

# Using the tuple() method to make a tuple

thistuple = tuple (("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Python Collections (Arrays)

# There are four collection data types in the Python Programming language

# List is a collection which is order and changeable
# Tuple is a collection which is ordered and unchangeable
# set is a collection which is unorder, unchangable na dunindexed
# dictonary: Is a collection which is ordered and changable

# Python Access Tuple Items

# We can access tuple items by referring to the index number, inside square brackets

# Print the second item in the tuple

thistuple = ("apple", "banana", "cherry")

# Negative Indexing
# Negative indexing means starting from the end

thisTuple = ("apple", "banana", "cherry")
print(thisTuple[-1]) #This will get cherry since -1 starts with the very last item

# Tange of indexes
# You can specify where to start and where to end the range
# This is the same method as when working with lists

thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# By leaving out the start value, the range will start at the first item

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:5])

# By leaving out the end value, the range will go on to the end of the tuple
# same as with a list
print(thisTuple[2:])

# negative indexes work in the same way

# Check if item exists
# to determine if a specified item is preset in a tuple use the in keyword
thisTuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")