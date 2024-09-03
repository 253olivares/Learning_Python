# Python Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties of another class

# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class

# Create a Parent Class

# Any class can be a parent class, so the syntax is the same as creating any other class

# Create a class named Person, with firstname and lastname properties, and a printname method

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

x = Person ("John", "Doe")
x.printname()

# Create a child class

# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class

class Student(Person):
    pass

# Now student has same properties and methods as Person

# Add the __init__() function

# So far we have created a child that inherits the properties and methods from its parents
# Add the __init__() function to the Student class:

class Student(Person):
    def __init__(self,fname,lname):
        pass

# Doing this will cause the init from the parent class to be over written
# To avoid this we need to call the parents instance of the __init__ function and pass its properties

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(fname, lname) #calling the parent class and passing its properties

# Use the super() Function

# Python also has a super function that will make the child class inherit all the methods and properties from its parent

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

# By using the super() function, you do not have to use the name of the parent element, 
# it will automatically inherit the methods and properties from its parents

# Add Properties

# Add a property calss called graduationyear to the Student class:

class Student(Person):
    def __init__(self, fname, lname, graduationYear):
        super().__init__(fname, lname)
        self.graduationYear = graduationYear

x = Student("Mike", "Olsen", 2019)

# Add Methods

# as a method called welcome to teh Student Class

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationYear)

# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden