# Python Datetime

# A date in python is not a data type of its own, but we can import a module named datetime to work with dates as date objects

# Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()
print(x)

# Date Output

# When we execute the code fro the example above the result will be
# 2024-09-03 10:37:58.640196

# The date contains year, month, day, hour, minute, second, and microsecond

# Te datetime module has many methods to return information about the date object

# here are a few examples, you will learn more about them later in the chapter.

import datetime

x = datetime.datetime.now()

print(x.year)
print*x.strftime("%A")

# Create Date Objects
# To create a date, we can use the datetime() class(constructor) of the datetime module.

# The datetime() class requires three parameters to create a date: year, month, day

import datetime

x = datetime.datetime(2020, 5, 17)

# The datetime() class also takes parameters for time and timezone (Hour, Minute, Second, Microsecond, Tzone) 
# but they are optional, and has a default value of 0, (one for timezone)

# The strftime() Method

# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


# %a Weekday, Short version
# %A Weekday, Full version

# %w Weekday as a number 0-6, 0 is sunday
# %d Day of month 01-31

# %b Month name, Short version
# %B Month ame, Full version
# %m Month as a number 01-12
# %y Year, short version, without century
# %Y Year, full version
# %H Hour 00-23
# %I Hour 00-12
# %p AM/PM
# %M Minute 00-59
# %S Second 00-59
# %f Microsecond 00000-99999
# %z UTC offset
# %Z Timezone
# %j Day number of year 001-366
# %U Week number of year, Sunday as the first day of week, 00-53
# %c local version of date and time
# %C Century
# %x Local version of date
# %X Local version of time
# %% a % character
# %G ISO 8601 year
# %u ISO 8601 weekday (1-7)
# %V ISO 8601 weeknumber (01-53)