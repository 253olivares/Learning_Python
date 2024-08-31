# Python Booleans

# Boolean values in programming you often need to know if an expression is true or false

# You can evaluate any expression in python and  get one or two answers

# When you comparing values Python will return a boolean answer

print(10 > 9)
print(10 == 9)
print(10<9)

# Booleans are most commonly used when working with if and else statements
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Evaluate values and variables
# The bool() function allows you to evaluate any value, and give you true or false in return
print(bool("Hello"))
print(bool(15))

# Most values are true

# Almost any value is evaluated to true if it has some sort of content
# Any string is true except empty strings
# Any number is true, except 0

# Any list, tuple, set and dictionary are true, except empty ones

bool("abc") #true
bool(123) #true
bool(["apple", "cherry", "banana"]) #true

# Some values are false
# In fact there are not many values that evaluate to false, exept empty values such as (), [], {}, "" and the number 0

# One more value or object in this case evaluates to false, and that is if you ahve an object that is made from a class with a __len__ function

# Functions can return boolean
def myFunction():
  return True

print(myFunction())

# Can you execute code based on the boolean answer of a function

if myFunction():
  print("YES!")
else:
  print("NO!")

# Python also has built in functions that return a boolean value like isinstance() function which can be used to determine if an object is a certain type of data type
x = 200
print(isinstance(x,int)) # should return true