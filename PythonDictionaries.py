# Python Dictionaries


# Dictionaries are used to store data values in key:value pairs

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates

# Dictionaries are written with curly brackets and have keys and values

# Create and print a dictionary

thisdict = {
    "brand" : "Ford",
    "model": "Mustang",
    "year" : 1964
}

# Dictionary Items
# Dictionary items are ordered, changeable, and do not allow duplicates

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name

# we cab call these items the same way as we normally do in other langauges
print(thisdict["brand"])

# Ordered or unordered
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change

# Unordered means that the items do not have a defined order, you cannot refer to an item by using an index

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2020
}

# Dictionary Length

# To determine how many items a dictionary has, use the len() function:
print(len(thisdict))

# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:

# string, int, boolean, and list data types
thisdict = {
    "brand" : "ford",
    "electric":False,
    "year" : "1964",
    "colors" : ["red", "white", "blue"]
}

# type()

# From Pythons perspective, dictionaries are defined as objects with the data type 'dict'

# The dict() constructor

# It is also possible to use the dict() constructor to make a dictionary

thisdict = dict(name="John", age = 36, country = "Norway")
print(thisdict)

# Python - Access Dictionary Items

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
x = thisdict["model"]

# There is a modal called get() that will give us the same results

# Get the value of the model key

x = thisdict.get("model")


# get Keys

# The keys() method will return a list of all the keys in the dictionary

x = thisdict.keys()

# get Values

# The values() method will return a list of all the values in the dictionary

y = thisdict.values()

thisdict["color"] = "white"


# The list of values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

x = car.values()

print(x) # Before the change

car["year"] = 2020

print(x) # After the change


# Get Items
# The items() method will return each item in a dictionary, as tuples in a list

# Get a list of the key:values pairs

x = thisdict.items()

# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected to the items list

# Python - Change Dictionary Items

# Change Values

# You can change the values of a specific item by referring to its key name

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

thisdict["year"] = 2018


# Update Dictionary

# The update() method will update the dictionary with the items from the given argument

# The argument must be a dictionary, or an iterable object with key:value pairs

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

thisdict.update({"year" : 2020})

# Python Add Dictionary Items

# Adding an item to the dictionary is done by using a new index key and assigning a value to it

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

thisdict["color"] = "red"

print(thisdict)

# Python Remove Dictionary Items

# There are several methods to remove items from a dictionary

# The pop() method removes the item with the specified key name:

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

thisdict.pop("model")

print(thisdict)


# The popitem() method removes the last inserted item

thisdict.popitem() # removes final item

# We can use the del keyword as well to remove item of specified key name

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

del thisdict["model"] # This will return an error if not found

print(thisdict)

# The clear() method empties the dictionary

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

thisdict.clear()
print("checked",thisdict)

# Python Loop Dictionaries

# You can loop through dictionary by using a for loop

# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
for x in thisdict:
    print("checked",x)


# Print all values in teh dictionary, one by one
for x in thisdict:
    print(thisdict[x])

# We can also loop through just values
for x in thisdict.values():
    print(x)

# You can use the keys() method to return the keys of a dictionary
for x in thisdict.keys():
    print(x)

# Loop through both keys and values, using the items() method
for x,y in thisdict.items():
    print("test",x,y)

# Python Copy Dictionaries

# You cannot copy a diction simply by typing dict2 = dict1, because: dict2 will onlt be a reference to dict1, and changes made in dict1 will automatically also be made in dict 2

# There are ways to make a copy, one way is to use a built in dictionary method copy

mydict = thisdict.copy()
print(mydict)

# Another way to make a copy us to use the buily in functions

thisdict = {
    "brand": "Ford",
    "model" : "Mustang",
    "year" : 1964
}

# Use the built in constructor 
mydict = dict(thisdict)
print(mydict)

# Python Nested Dictionaries

# A dictionary can contain dictionaries, this is called nested dictionaries 
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2005
    }
}

child2 = {
    "name" : "Tobias",
    "year" : 2007
}

myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2005
    },
    "child2" : child2
}

# Access items in nested dictionaries

# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary

print(myfamily["child2"]["name"])

# Loop through nested dictionaries

# You can loop through a dictionary by using the items() method like this:

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y+ ':' , obj[y])

        