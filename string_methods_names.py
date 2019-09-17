# Given a name in the format

# lastname, firstname

# where there is exactly one comma and exactly one space, transform the name into the format

 

# first_initial. lastname

# where

# * first_inital and lastname are both capitalized

# * there is exactly one period and space following the first_initial

 

# For example, given s='ghandi, mahatma'

# the output will be

# M. Ghandi


name = input("Input a name: ")

first, last = name.split( ", ")
print(last[0].upper()+ ". " + first.capitalize())