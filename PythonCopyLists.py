# Pyhton Copy Lists

# Copy a list

# You cannot copy a list simply by typing list2 = list1, because list2 will only be a reference to list1 and changes made in list1 will automatically also be made in list 2
# THe way coding works variables only reference a location to where the value is stored in memory 

# Use the copy() method

# You can use a built in list method copy() to copy a list

thislist = ["apple", "banana", "cherry"]
thislist = thislist.copy()
print(thislist)

# use the list() mehtod

# Another way to create a copy is by using a built in method list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# use the slice operator 
# You can also make a copy of a list by using the : slice operator

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:] # this just copies the entire list from beginning to end
print(mylist)