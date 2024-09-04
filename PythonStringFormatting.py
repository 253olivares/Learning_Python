# Python String Formatting

# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings
# Before Python 3.6 we had to use the format() method


# F-Strings

# F-string allows you to format selected parts of a string
# To specify a string as an f-string, simply put a f in front of the string literal, like this:

text = f"The price is 49 dollars"

print(text)

# Placeholders and Modifiers
# TO format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.

price = 59
text = f"The price is {price} dollars"
print(text)

# A placeholder can also include a modifier to format the value
# A modifier is include bt adding a colon : followed bt a legal formatting type, like .2f which means fixed point number with 2 decimals

price = 59
text = f"The price is {price: .2f} dollars"

# We can also format a value directly

text = f"The price is {95: .2f} dollars"
print(text)

# Perform Operations in F-string

# You can perform Python operations inside the placeholders
# You can do math operations
text = f"The price is {20*50: .2f} dollars"
print(text)

# You can perform math operations on variables

price = 59
tax = 0.25

text = f"The price is {price * (tax +1):.2f} dollars"

# You can perform if...else statements inside teh placeholders
price = 49
text = f"It is very{'expensive' if price >= 50 else 'cheap'}!"

# Execute Functions in F-strings

fruit = "apples"
text = f"I love{fruit.upper()}"
print(text)

# The function does not have a built-in Python method, you can create your own functions and use them:

def myconverter(x):
    return x * 0.348

text = f"The plane is flying at my {myconverter(40000)} meter altitude"

print(text)

# More Modifiers
# At the beginning of this chapter we explained how to use the .2f modifier to format a number into a fixed point number with 2 decimals
# There are several other modifiers that can be used to format values:

price = 59000
text = f"The price is {price:,.2f} dollars"
print(text)

# String Format()

# Before Pythion 3.6 we used the format() method to format strings.

# The format() method can still be used, but f-strings and the preferred way to format strings.
# The next examples in this page demonstrates how to format strings with the format() method
# The format() method also uses curly brackets as placeholder {}, but the syntax is slightly different

price = 49
text = "The price is {} dollars"
print(text.format(price))

# you can add parameters inside the curly brackets to specify how to convert the values
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Multiple Values
# If you want to use more values, just add more values to the format() method

# print(text.format(price,itemno,count))
# and add more placeholders

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity,itemno,price))

# Index Numbers
# You can use index numbers (a number inside the curly brackets {0}) to be sure teh values are places in the correct placeholders:

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} price of item number{1} for {2:.2f} dollars"
print(myorder.format(quantity, itemno, price))

# Named Indexes
# We can also use named indexes by entering a name inside teh curly brackets {carname}, but then you must use the names when you pass the parameters values

myorder = "I have a {carname}, it is a {model}"
print(myorder.format(carname = "Ford", model ="Mustang"))
