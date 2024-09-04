# Python RegEx

# A RegEx, or regular expression, is a sequence of characters that forms a search pattern.
# Regex can be used to check if a string contains the specified search pattern

# RegEx Module

# Python has a built-in package called re, which can be used to work with Regular Expressions
# Import the re module:

import re

# RegEx in Python

# When you have imported the re module, you can start using regular expressions:

import re
text = "The rain in Spain"
x = re.search("^The.*Spain$", text) #It is case sensitive

if x:
  print("YES! We have a match!")
else:
  print("No match")

# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match:

# findall : Returns a list containing all matches
# search : Returns a Match Object if there is a match anywhere in the string
# split : Returns a list where the string has been split at each match
# sub : Replaces one or many matches with a string

# Metacharacters
# Metacharacters are characters with a special meaning

# [] a set of characters     [a-m]
# \ Signals a special sequence (can also be used to escape special characters)     \d
# . Any character (except newline character)      he..o
# ^ Starts with      ^hello
# $ Ends with      planet$
# * Zero or more occurrences   he.*o
# + one or more occurrences    he.+o
# ? Zero or more occurrences       he.?o
# {} Exactly the specified number of occurrences     he.{2}o
# | Either or          "falls|stays
# () capture and group

# The findall() Function

# The findall() function returns a list containing all matches

import re
text = "The rain in Spain"
x = re.findall("ai",text)

print(x)

# The list contains the matches in order they are found
# IF no matches are found, an empty list is returned

# The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned

# Search for the first white-space character in the string

import re

text = "The rain in Spain" 
x=re.search("\s", text)

print("The first white-space character is located in position:", x.start())

# If no matches are found, the value None is returned:

import re 

text = "The rain in Spain"
x = re.search("Portugal", text)
print(x)

# The split() Function
# The split() function returns a list where the string has been split at each match:

import re
text= "The rain in Spain"
x.re.split("\s", text)
print(x)

# We can tell teh code how many times we want to split the string for example if we want to stop at the first occurance

import re
text = "The rain in Spain"
x = re.split("\s",text,1)

# The sub() function

# The sub() function replaces the matches with the text of your choice:
import re
text = "The rain in Spain"
x = re.sub("\s", "9", text)

# Control the number of replacements by specifying the count parameter

import re
text = "The rain in Spain"
x = re.sub("\s", "9", text, 2)
print(x)

# Match Object
# A Match object is an object containing information about the search and the result.

# Note: If there is not match, thje value none will be returned, instead of the Match Object.

import re
text= "The rain in Spain"

x = re.search("ai",text)

print(x)

# The Match object has and methods used to retrieve information about the search, and the result:
# .span()  returns the tuple containing that start, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

# Print the position (state- and end-position) of the first match occurrences. 
# The regular expression looks for any words that start with an upper case "S":

import re 
text = "The rain in Spain"
x = re.search(r"\b5\w+", text)
print(x.span())

# Print the string passed into the function

import re

text = "The rain in Spain"
x = re.search(r"\bS\w+", text)

print(x.string)

# Print the part of the string where there was a match

# The regular expression looks for any words that start with an upper case "S"

import re

text = "The rain in Spain"
x = re.search(r"\bS\w+", text)

print(x.group())