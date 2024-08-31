# Python Lists

myList = ["apple", "banana", "cherry"]

# Lits are used to store multiple items in a singular variable

# Lists are one of 4 built in data types in python to store collections of data, the other 3 are tuple, set, and dictionary, all with different qualities and usage

thislist = ["apple","banana","cherry"]
print(thislist)

# List items
# List items are ordered, changeable, and allow duplicate values

# List items are indexed, the first item has index [0]

# Ordered
# When we say that lists are order it means that the item had a defined order and that order will not change

# if you add new ites to a list, the new ites will be palced at the end of the list

# changeable
# The list is changable meaning we can change, add, and remove items in the list after it has been created

# Sinces are indexed we have have items with the same value

# For example
thislist = ["apple","banana","cherry","apple","cherry"]
print(thislist)

# List Lenfth
# To determine how many items a list has the len() function returns the length of a list

thislist = ["apple","banana","cherry"]
print(len(thislist)) # 3

# List Items - data types
# Lists can be of any data type

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# The list can also contain different data types

list1 = ["abc", 34, True, 40, "male"]

# type()
# From python perspective, lists are defined as object with the date type 'list'
mylist = ["apple","banana","cherry"]
print(type(mylist))

# The list() constructor

# It is possible to use the list() constructor when creating a new list
thislist = list(("Apple","Banana","Cherry"))
print(thislist)

# Python Collections (Arrays)
# There are four collection data types in the Python programming languages
# List - collection which is ordered and changeable. Allows duplicate members
# Truple - is a collection which is ordered and unchangeable.
# Set - collection which is unordered unchange and unindexed
# Dictionary - is a collection which is ordered

# When choosing the collection type it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, ir could mean an increses in efficienct or security

# Access List items

# Items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
# Negative indexing means start from the end

# -1 refers to the last item
# -2 refers to the second last item

# Range of indexes
# You can specify a range of indexes by specifying where to start and where to end the range
# When specifying a range, the return value will be a new list with the specified items.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# By leaving out the start value the range will start at the first and then at the second position of the index
print(thislist[:4])

# By leaving out the end value the range will then continue from the specified index to the last position.
print(thislist[2:])

# Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if items exists

# To determine if an specified item is present in a list use the in keyword
if "apple" in thislist:
    print("yes, 'apple' is in the fruits list.")

# Python - Change List Items

# Change Item Value
# To change then value of a specific item, refer to the index number
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" # specifying a specific position we can change the value
print (thislist)

# change a range of item values
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] # positions 1 and 2 will be replaced with the array
print(thislist)

# if the length of values being replaced is different then the remaining values will be removed from the original list and the additional values of the new list will be added
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method

# The insert() method inserts an item at the specified index
# This insert method pushes values within a specific index

thislist = ["apple", "banana", "cherry"]
thislist.insert(2,"watermelon")
print(thislist)

# Python - Add List Items

# Append Items
# To add an item to the end of the list use the append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# insert items
# To insert an list item at a specified index, use the insert method
# The insert() method inserts an item at the specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1,"orange")
print(thislist)

# extend list
# To append elements from another list to the current list, user the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) # extend thislist array by adding the elements from tropical to thislist
print(thislist)

# Add any iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange") # adding a tuple to a list
thislist.extend(thistuple)
print(thislist)

# Python - remove list items
# Remove specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# If there are more than one item with the specified value, the remove() method removes the first occurrence
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") # remove will only remove the first occurrence
print(thislist)

# Remove specified index
# The pop() method removes the specified index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # remove item at specific index 
print(thislist)

# if you do not specify the index, the pop() method removes the last items
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# if no index is provided it pop will just remove the last item

# The del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# this del keyword can also delete the list completely
thislist = ["apple", "banana", "cherry"]
del thislist # if no index is provided just deletes the whole list

# clear the list
# the clear() method empties the list
# The list still remains but has no content

thislist = ["apple", "banana", "cherry"]
thislist.clear() # ["apple", "banana", "cherry"] => []
print(thislist)

# Python Loop lists
# You can loop through the list items by using a for loop
thislist=["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop through the index numbers
# You can also loop through the list items by referring to their index number
# use the range() and len() functions to create a suitable iterable
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)): # mew array created based on length
    print(thislist[i])

# Using a while loop
# You can loop through the list items by using a while loop

# Using the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes
# remember to increase the index by 1 after each iteration
thislist = ["apple", "banana", "cherry"]
i = 0
while i< len(thislist):
    print(thislist[i])
    i = i + 1

# Looping using list comprehension
# List comprehension offers the shortest syntax for looping through lists
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] # short hand for loop