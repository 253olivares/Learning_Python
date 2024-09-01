# Python update Tuples

# Tuples are unchangeable, meaning you cannot change, add, or remove items once the tuple is created

# change tuple calues

# onece a tuple is create you cannot change its values

# Tuples are unchangeable or immutable

# but there is a work around
# this being turing a tuple into a list and then from list back into a tuple

x = ("apple", "banana", "cherry")
y = list(x) # Tuple -> list
y[1] = "kiwi" # list-> Tuple
x = tuple(y)

print(x)

# Add items

# since tuples are immutable they do not have a built in append() method, but there are other ways to add items to a tuple

# 1. convert into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange") # add orange to the new list created from a tuple
thistuple = tuple(y) 


# Add tuple to a tuple 
# We are allowed to add tuples to tuples so if we want to add one or many we can add those values
thistuple = ("apple", "banana", "cherry")
y=("orange",)
thistuple += y # Add our y tuple to the end of thistuple

# Remove Items

# Tuples are unchangeable so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items

# Convert Tuple into a list and remove apple and then convert it back into a tuple

thistuple = ("apple", "banana", "cherry")
y = list([x for x in thistuple if x != "apple"])
print (tuple(y))

# Or you can delete the tuple completely

# The del keyword can delete the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) This will return an error since this tuple no longer exists 