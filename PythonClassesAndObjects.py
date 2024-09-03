# Python Classes and Objects

# Python is an object oriented programming language

# Almost everything in Python is an object, with its properties and methods

# A class is like an object constructor, or a blueprint for creating objects


# Create a Class

# Te create a class use the keyword class

class MyClass:
    x = 5

# Create Object 

# No we can use the class named MyClass create objects:

# Create an object named p1, and print the value of x

p1 = MyClass()
print(p1.x)

# The _init_() function

# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

# TO understand the meaning of classes we have to understand the built-in _init_() function

# All classes have a function called __init__() which is always initiated when the class is being called

# Use the _init_() function to assign values to object properties, or other operations that are necessary to do when the object is being created. 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person(name=36, age="John")

# The __init__() function is called automatically every time the class is being used to create a new object


# The __str__() function

# The __str__() function controls what should be returned when the class object is represented as a string
# If the __str__() function is not set, the string representation of the object is returned

# Without __str__()

class Person:
    def __init__(self,name,age):
        self.name= name
        self.age = age

p1 = Person("John", 36)

print("Without",p1) #Points to memory address where data is stored

# With __str__()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("John", 36) #displays our information in __str__

print("With",p1)

# Object Methods

# Objects can also contain methods. Methods in objects are function that belong to the object

# Let us create a method in the person calss

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.myfunc()

# The self parameter is a reference to the current instance of the class and is used to access variable that belong to the class

# The self Parameter

# The self parameter is a reference tot he current instance of the class and us used to access variables that belong to the class

# It does not have to be name self, you can call it whatever we want, but it has to be the first parameter of any function within the class

class Person:
    def __init__(test,name,age):
        test.name = name
        test.age = age

    def myfunc(abc):
        print("Hello my name is "+ abc.name)

p1 = Person("John", 36)

p1.myfunc()

# Modify Object Properties

# When we modify properties on objects as follows
# Set the age of p1 to 40

p1.age = 40

# Delete Object Properties
# We can also delete properties on objects by using the del keyword


del p1.age

# Delete Objects

del p1

# Something we have to keep in mind is that we cannot have classes empty when creating them
# If we do we need to call the pass keyword to avoid errors

class Person:
    pass
