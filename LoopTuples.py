# Python Loop Tuples

# Loop through a tuple

# You can loop through the tuple items by using a for loop

thistuple = ("apple", "banana", "cherry")

for x in thistuple:
    print(x)

# This functions in the same way as a list

# Loop through the index numbers

thistuple = ("Chiecken", "red", "soda")

for x in range(len(thistuple)):
    print(thistuple[x])

# Using a while loop

# You can loop through the tuple item by using a while loop

# Use the len() function to determine the length of a tuple, thens tart 0 of your loop

thistuple = ("this",  "is", "a", "new", "tuple")
x  = 0 

while x < len(thistuple):
    print("test",thistuple[x])
    x += 1