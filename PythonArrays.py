# Python Arrays

# Python does not have a built in support for arrays but python lits can be used instead

# For this module we are going to us lists and arrays to work with arrays we need to import a library like NumPy

# Arrys are use to store multiple values in one single variable

cars = ["Ford", "Volve", "BMW"]

# What is an Array

# An array is a special variable which can hold more than one value at a time

# if if you have a list of items (a list of car names for example) storing the cars in a single variable woul look liek this

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

# However what if you want to loop through the cars and find a specific one? and what if you have not 3 cars but 300

# The solution is an array!

# An array can hold many values under a single name, and you can access those values by using index numbers

# Access the elemnt of an array

x = cars[0]

# Change the value at index

x = cars[0] = "Toyota"

# The length of an array

# Use the len method

x = len(cars)

# Loop through an array

for x in cars:
    print(x)

# Adding array elements
cars.append("Honda")

# Remove elements
cars.pop(1) #specify index you want to remove other wise it removes last element

# remove element by name
cars.remove("Volve") # only deletes first occurance


