# Python JSON

# JSON is a syntax for storing and exchanging data

# JSON is text, written with JavaScript object notation.

# JSON in Python

# Python has a built in package called json, which can be used to work with JSON data.

# Import the json module

import json

# Parse JSON - convert from JSON to Python

# If you have  JSON string, you can parse it by using the json.loads() method
# Convert from JSON to Python

import json

# some JSON:
x = '{"name":"John", "age":30, "city":"New York"}'


# Parse x
y = json.loads(x)

print(y["age"])

# Convert from Python to JSON
# If you have a Python, you can convert it into a JSON string by using the json.dumps() method

import json

# a Python object (dict)

x = {
    "name": "John",
    "age": "30",
    "city": "New York"
}

y = json.dumps(x)

print(y)

# You can convert Python objects of the following types, into JSON string

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "banana"]))
print(json.dumps("apple","bananas"))
print(json.dumps("Hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# dict
# list
# tuple
# str
# int
# float
# True
# False
# None

# Convert a Python object containing all the legal data types:

import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children" : ("Anny","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg":27.5},
        {"model": "Ford Edge", "mpg":24.1}
    ]
}

print(json.dumps(x))

# Format the Result

# The example above prints a JSON string, but it is not very east to read, with no indentations and line break

# The json.dumps() method has a parameters to make it easier to read the result:
json.dumps(x,indent=4)

# You can also define the separators, default value is (", ", ": ")

json.dumps(x,indent=4,separators=(".", "="))

# Order the Result

# The json.dumps() method has parameters to order the keys in the result

# use the sort_keys parameters to specify if the result should be sorted or not:

json.dumps(x,indent=4,sort_keys=True)



