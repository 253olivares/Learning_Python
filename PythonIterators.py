# Python Iterators

# An iterator is an object that contains a countable number of values
# An iterator is an object that can be iterated upon meaning that you can traverse through all the values
# Technically in python an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__()

# Iterator vs Iterable

# Lists, Tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which can be used to get an iterator:

# Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# This works even on strings

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator

# We can also use a for loop to iterate through an iterable object

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)


# Iterate the characters of a string

mystr = "banana"

for x in mystr:
    print(x)

# The for loop actually creates an iterator object and executes the next method for each loop 


# Create an Iterator

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object

# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__() which allows 
# you to do some initializing when the object is being created 

# The __iter__() method acts similar, you can do operations (initializing ect.)

# The __next__() method also allows you to do operations, and must return the next item in the sequence

# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myClass = MyNumbers()
myiter = iter(myClass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# Stop Iteration

# The example above would continue forever if you had enough next() statement, or if it was used in a for loop.
# To prevent iteration from going on forever we can use the StopIteration statement.
# In the __next__() method, we can add a termination condition to raise an error if the iteration is done a specified number of times

# Stop after 20 iterations

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
myClass = MyNumbers()
myiter = iter(myClass)

for x in myiter:
    print(x)