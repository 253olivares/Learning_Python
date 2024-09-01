# Python - Sort Lists

# Sort list alphanumerically

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist= [100,50,65,82,23]
thislist.sort()
print(thislist)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:

# ex:
# Sort the list descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse= True) # sort list in reverse order

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# customizing the sort function
# We can also customize our own function by using keyword arguments
# The function will return a number that will be used to sort the list (the lowest number first):

# The custom function that will sort
def myfunc(n):
    return abs(n-50) # subtract 50 from the number and return the absolute value which converts any negative numbers to positive and then whatever comes it is what is used to sort

thislist = [100,50,65,82,23]
thislist.sort(key = myfunc)
print(thislist)

# Case insensitive sort

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters

thislist = ["banana", "orange", "Kiwi", "Cherry"]
thislist.sort()
print(thislist)

# this happens because of the capital letters position from the ascll position for each letter

# To fix this we use a built in function as a key function when sorting
# we use str.lower to fix this issue


thislist.sort(key = str.lower)
print(thislist)

# Reverse order
# What if you want to reverse the order of a list, regardless of the alphabet
#  The reverse() method reverses the current sorting order of the elements

thislist = ["banana", "Orange", "Kiwi", "Cherry"]
thislist.reverse() # this will return the reverse order of our list
thislist