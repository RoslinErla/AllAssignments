#Write a function named is_float(s) that takes one argument that is a string. 
#  It returns True if string s represents a floating point value 
# and returns False otherwise.  You are required to use try-except.  
# The basic concept is to "try" to convert string s to a float and if it succeeds, return True,
#  but if it fails (that is, an exception is raised), return False. 
#  Note that float() raises a  ValueError exception.

def is_float(s):
    try:
        is_it_float = float(s)
        return True

    except ValueError:
        return False



print(is_float('3.45'))
print(is_float('3e4'))
print(is_float('abc'))
print(is_float('4'))
print(is_float('.5'))