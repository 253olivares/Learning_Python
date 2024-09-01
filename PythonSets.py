# Python Set

myset = {"apple", "banana", "cherry"}

# Sets are used to store multiple items in a single variable

# Set is one of the 4 built in data types in Python used to store collections of data,
# The other 3 are lists, tuples, dictionary

# Set is a collections which is unordered, unchangeable, unindexed

# Sets are defined by being written in curly brackets

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Set Items

# Set items are unordered, unchangeable, and do not allow duplicate values

# unordered
# Unordered means that the items in a set do not have a defined order

# Set items can appear ina  different order every time you use them, and cannot be referred to by index or key


# Unchangeable

# Set items are unchangable, meaning that we cannot change the items after the set has been created

# Duplicates not allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Duplicates not allowed

# Sets cannot have two items with the same value

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) # Despite not allowing duplicates this will not throw an error. What it will do is just not show the duplicate values

# Both true and false are the same value
thisset = {"apple", "banana", "cherry", False, True, 0}

# In sets
#  True = 1,
#  False = 0

# Get the length of a set

# To determine how many items a set has use the len() function

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set Items - Data Types
# Set items can be of any data type and do not have a restriction
set1 = {"apple", "banana", "cherry"}
set2 = {1,5,7,9,3}
set3 = {True, False, False}

set1 = {"abc", 34,  True, 40, "male", ("check", "Yernk", "Sperny")}

for x in set1:
    print("test",x)

# From a Python perspective, sets are defined as objets with the data type set

# What is the data type of a set
myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = set(("apple", "banana", "cherry")) #Just like with list and tuples you can call the constructor to create a set
print(thisset)

# Python Access set Items

# Access Items

# You cannot access Items in a set by referring to an index or a key

# But you can loop through set items using a for loop, or ask if a specified value is preset in a set, by using the in keyword

thiset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

print("banana" in thiset)

# Check if banana is not present in the set
print("banana" not in thiset)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items

# Python Add Set Ites

# Once a set is created you cannot change its items but you can add new items

# To add one item toa  set use the add method

thisset = {"apple", "banana", "cherry"}
thiset.add("Orange")


print(thiset)

# Add sets
# To combine sets from one to another use the update() method

thiset = {"apple", "banana", "cherry"}

tropical = {"pineapple", "mango", "papaya"}

thiset.update(tropical)

print(thiset)

# Add any interable

# The object in the update() method does not have to be a set, It can be any iterable object (tuples, list, dictionaries)

# Add elements of a list to a set

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thiset.update(mylist)

print(thiset)

# Python remove set items

# To remove an item in a set, use the remove() or the discard() method

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
print(thiset)

# If the item remove does not exist it will raise an error


# thisset = {"apple", "banana", "cherry"}

thiset.discard("banana")
# when using discard if the item doesnt exist it will not raise an error

# If you can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that get removed.

# The return the value of the pop() method is the removed item

thisset = {"apple", "banana", "cherry"}

x = thisset.pop() # returns an item when popped

print(x) # displays popped item

print(thisset)


# Sets are unordered, so when using the pop() method, you do not know which item that gets removed

# The clear() method empties the set

thisset= {"apple", "banana", "cherry"}

thisset.clear()

print(thiset)

# delete does the same thing but will return an error as the variable no longer exists

thiset = {"apple", "banana", "cherry"}

del thiset

print(thiset)

# Python Loop sets

# You can loop through the set items by using a for loop

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


# Python Join Sets

# There are several ways to join two or more sets in Python

# The union() and update() method joins all items from both sets

# The intersection() method keeps only the duplications
# The difference () method only keeps the items from the first set that are not in the other sets

# The symetric_difference() method keeps all the items except the duplicates

# Union
# Returns a new set with all items from both

set1 = {"a", "b", "c"}
set2 = {1,2,3}

set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of a union method will get the same result

set3 = set1 | set2

# Join Multiple Sets

# All the joining methods and operators can be used to join multiple sets

# When using a method, just add more sets in the parentheses, separated by commas

set3 ={"John", "Elena"}

set4 = {"apple", "banana", "cherry"}

myset = set1.union(set2,set3,set4)

# OR

myset = set1 | set2 | set3 | set4

print(myset)

# Join a set and a Tuple

# THe union method allows us to join sets with other data types and it will result in being a union

# Update

# The update() method inserts all items from one set into another.
# When this is done update modifies the original set and does not return a new set

set1.update(set2)
print(set1)

# Intersection

# KEEPS ONLY THE DUPLICATES

# The intersection() method will return a new set, that only contains the items that are present in both sets

set3 = set1.intersection(set2)
print(set3) # Combine both sets but only keep dupes

# WE can slo use the & operator instead of intersection() metho

set3 = set1 & set2
print(set3)

# intersection_update does the same thing but instead of creating a new array it will update the original array

# The value True and 1 are considered the same value. The same goes for False and 0
# Something to keep in mind when using methods like intersection and update

# Difference() 
# The method will return a new set that contains only the items from the first set that are not present in the other set

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

# You can use the - operator instead of the difference () method to get the same result

set3 = set1 - set2
print(set3)

# Something to keep in mind with using operators you can cannot user them with varied data types

# Difference_update() exists to the same as intersection_update
# Modify the original set to only include items in first set not in second set

# Symmetric Differences

# Will return items that are not present in both

set3 = set1.symmetric_difference(set2)

# For an operator we can use ^ instead

set3 = set1 ^ set2
# Just like other operators variables must be the same data type

# Symetric_difference_update() does the same as other update methods that changes the original array

set1.symmetric_difference_update(set2)

print(set1)

