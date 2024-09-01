#  List Comprehension
#  List comprehension offers a shorter syntax when you want to create a new list 
#  base on the values of an existing list

# Based on a list of fruits you want a new list, containing only yhe fruits with the letter "a" in the name
# without list comprehension you will have to write for statement in a conditional test inside

# Created a new list of fruits with the letter a without using list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", 'mango']
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x) # append any variable that as an a in it

print(newlist)

fruits = ["apple", "banana", "Cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# The Syntax
# newlist= [expression for item in iterable if condition == True]
# The return value is a new list leaving the old list unchanged

# The condition is like a filter that only accepts the times that valuate to True


# list comprehension that only accepts items that are not "apple"

newlist = [x for x in fruits if x != "apple"]

# The condition if x != "apple" will return TRue for all elements other than "apple", making the new list contain all fruits except "apple"

# The condition is optional and can be omitted 
newlist= [x for x in fruits]

# Iterable
# The iterable can be any iterable object, like a list, tuple, set 

# You can use the range() function to create a iterable
newlist = [x for x in range(10)]

# using the same list above creating a list comprehension that only accepts numbers below 5
newlist = [x for x in range(10) if x < 5]

# Expression the expression is the current item in the iteration but it is also the outcome, which you can manipulate before it ends up like a list item
# set the values in the new list to uppercase
newlist = [x.upper() for x in fruits]

# You can set the outcome to whatever you like
# loop through fruits and replace each value with hello
newlist = ['hello' for x in fruits]

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
newlist = [x if x!= "banana" else 'orange' for x in fruits]
