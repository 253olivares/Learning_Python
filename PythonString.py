# Python Strings

# Strings in python are surrounded by either single quotation marks or double quotation marks
# 'hello' is the same as "hello"
# you can display a string literal with the print()
# 
print("Hello") 
print('hello')

# Quotes inside quotes
# You can use quotes inside a string, as long as they dont match the quotes surrounding the string
print("It's alright")
print("He is called 'Johnny'")
print('He is called"Johnny"')

# Assign string to a variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string
a = "Hello"
print(a)

# Multiline strings
# You can assign a multiline string to a variable by using three quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
# Like many other popular programming languages, strings in Pythin are arrays of bytes representing unicode characters
#  Python does not have a character data type a single character is simply a string with a length of 1

a = "Hello, World!"
print(a[1])

# Looping through a string
# Since strings are arrays, we can loop through the characters in a string with a for loop
for x in "banana":
    print(x)

# String Length
# to get the length of a string to use len() function
a = "Hello, World!"
print(len(a))

# Check String
# check if a certain phrase or character is present in a string, we can use the keyword in
txt = "The best things in life are free!"
print("free" in txt)

# use it in a if statment to check if conditions are meet
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if NOT
# To check if a certain phrase or character is not present in a string, we can use the keyword not in
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# Python - slicing strings
# Slicing
# We can return a range of characters by using slicing syntax

# get characters from 2 to 5
b = "Hello, World!"
print(b[2:5])

# Slice from the start
# By leaving out the start index the range will start at the first character
b = "Hello, World!"
print(b[:5])

# Slice to the end
# By leaving out the end index the range will go the end
b = "Hello, World!"
print(b[2:])

# Negative Indexing
# using negative indexes to start the slice from the end of the string

b = "Hello, World!"
print(b[-5:-2])

# Modify Strings
# Python has a set of built in methods that you can use on strings

# Upper Case
# The upper() method return the string in upper case
a = "Hello, World!"
print(a.upper())

# Lower Case
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# This is the same of trim in javascript
a = " Hello, World! "
print(a.strip())

# Replace String
# The replace() method replaces a string with another string
a = "Hello, World!"
print(a.replace("H","J"))

# Split String
# The split() method return a list where the text between the specified separator becomes the list items
# This is like the javascript JSON.parse
a = "Hello, World!"
print(a.split(",")) # returns ["Hello","World!"]

# Python string concatenation
# String Concatenation 

a = "Hello"
b = "World"
c = a + b

a = "Hello"
b = "World"
c = a + " " + b

# Python Format Strings

# String Format
# As we learned in the Python variables chapters we cannot combine string and numbers using +

# If we wanted too or needed to we can combine strings and number types using F-strings

age = 36
txt = f"My name is John and my age is {age}"
print(txt)

# Placeholders and modifiers
# Placeholders can contain variables, operations, function, and modifiers to format the value

price = 59
txt = f"The price is {price} dollars"

print(txt)
# A placeholder can include modifiers to format the value
# A modifier is included by adding a colon followed by a legal formatting type, like .2f which means fixed point number with 2 decimals
# displace price with 2 decimals

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) # The price is 59.00 dollars

# A placeholder can contain python code like a math operation

txt = f"The price is {20 * 50} dollars"
print(txt)

# The f strings is the equivalent as using ` to directly call javascript functions to be used inside strings`

# Python - escape character
# To insert characters that are illegal in a string, us an escape character

# An escape character is a backslash \ followed bt the character you want to insert

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes
txt = "We are the so-called \"Vikings\" from the north."

# Escape Characters
# \' Single quote
# \\ Backslash
# \n New Line
# \r Carriage Return
# \t Tab
# \b Backspace
# \f Form Feed
# \ooo Octal value
# \xhh Hex value

# Python String Method
# Python has a set of built in methods that you can use on strings

# Some of the functions built in to help manipulate strings
# capitalize() Converts the first character to uppercase
# casefold() Converts string into lower case
# center() returns the centered string
# count() returns the number of times of specified value occurs in a string
# encode() returns an encoded version of the string
# endswith() returns true if the string ends with the specified value
# expandtabs() sets the tab size of the string
# find() searches the string for a specified value and returns the position of where it was found
# format() Formats the specified values in a string
# format_map() formats specified values in a string
# index() searches the string for a specified value and returns the position of where it was found
# isalnum() returns true if all characters in the string are alphanumeric
# isalpha() returns true if all characters in the string are in the alphabet
