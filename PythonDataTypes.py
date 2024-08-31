# Python data types
# Built in data types

# The following data types are built in my default
# Text type: str
# Numeric type: int, float, complex
# Sequence type: list, tuple, range
# Mapping type: dict
# Set type: set, frozenset
# Boolean, type: bool
# Binary type: bytes, bytearray, memoryview
# None type: nontype

# Getting the data type
# You can get the data type of any object bt using the type() function

x = 5
print(type(x))

# Setting the Data Type
# In Python the data type is set when you assign a value to a variable

x = "Hello World" # str
x = 20 # int
x = 20.5 # float
x = 1j #complex
x = ["apple","banana","cherry"] # list
x = ("apple","banana","cherry") # tuple
x = range(6) # range
x = {"name": "John", "age":36} # dict
x = {"apple", "banana", "cherry"} # set
x = frozenset({"apple", "banana", "cherry"}) # frozenset
x = True # bool
x = b"Hello" # btyes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview
x = None # NoneType

# Setting the specific data type

# If you want to specify a specific data type we have to follow constructor functions

# specify variable as string
x = str("Hello World")

x = float(20.5) 

x = list(("apple","banana","cherry"))