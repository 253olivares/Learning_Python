# Python Unpack Tuples

# When we create a tuple, we normally assign values to it, this is called packing a tuple

# packing
fruits= ("apples", "bananas", "cherry")

# But in python we are also allowed to extract the values back into variables this is called unpacking

(x,y,z)= fruits

print(x)
print(y)
print(z)

# When unpacking we have to provide the same amount of values as the tuple
# if not we need to use a Asterisk


fruits = ("apples", "banana", "cherry", "strawberry", "mango")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# If teh asterisk is added to another variables name than the last, Python will assign values to teh variable until the number of values left matches the number of variables left