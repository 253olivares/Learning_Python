# Convert Tuple into a list and remove apple and then convert it back into a tuple

thistuple = ("apple", "banana", "cherry")
y = list([x for x in thistuple != "apple"])
print (tuple(y))