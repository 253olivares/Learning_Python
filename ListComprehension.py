#  List Comprehension
#  List comprehension offers a shorter syntax when you want to create a new list 
#  base on the values of an existing list

# Based on a list of fruits you want a new list, containing only yhe fruits with the letter "a" in the name
# without list comprehension you will have to write for statement in a conditional test inside

fruits = ["apple", "banana", "cherry", "kiwi", 'mango']
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x) # append any variable that as an a in it

print(newlist)