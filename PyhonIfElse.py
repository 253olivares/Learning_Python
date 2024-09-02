# Python If ... Else 

# Python supports the usual logical conditions from mathematics

# equals a == b
# not equals a != b
# less than a < b
# less than or equal to a <= b
# greater than a > b
# greater than or equal to a >= b

# These conditions can be used in several ways, most commonly in "if statements" and loops

# an "if statement" is written using the if keyword
a = 33
b = 200
if b > a:
  print("b is greater than a")

# as previously discussed python relies on indentation to create code blocks

# Elif

# the elif keyword is pythons way of saying "if the previous conditions were not true then try this"

if b > a : 
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal"

# Else

# The else keyword catches anything which isnt caught by the preceding conditions

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else: 
  print("a is greater than b")

#   We can also have a else without the elif statment

if a>b:
  print("a is greater than b")
else: 
  print("a is not greater than b")

# Short hand if

# If you have only one statement to execute, you can put it on the same line as the if statement

if a > b: print("a is greater than b")

# Short hand if else

# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line

a = 2
b = 330
print("a") if a > b else print("b")
# action if condition else action 2

# This technique is known as a Ternary Operators, or Conditional Expression 

# We can also have multiple else statements on the same line

# one if else statement, with 3 conditions

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# action 1 if condition else action 2 if condition ... (keep adding actions and conditions for each addition action) else final action


# And
# The and keyword is a logical operator, and is used to combine conditional statements will run the block is both statements are true

# Test if a is greater than b, AND if x is greater than a

a = 200
b = 33
c = 500

if a > b and c > a:
  print("Both conditions are True")

# Or 
# The or keyword is a logical operator, and is used to combine conditional statements will run the block if either statement is true

x = 41

if x >  10:
  print("Above ten,")
  if x  > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Test if a is greater than b or if a is greater than x

if a > b or a > c:
  print("At least one of the conditions is True")

# NOT
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

# Test if a is Not greater than b:

a = 33
b = 200
if not a > b: # will reverse the result of the conditional statement
  print("a is NOT greater than b")

# Nested if

# You can have if statements inside if statements, this is called nested if statements


# Pass statement
# If statements cannot be empty but if for some reason if you have an if statment with no content put the pass statment to avoid getting an error

a = 33
b = 200
if b > a:
  pass


