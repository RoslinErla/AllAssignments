# Write a Python program that reads an integer from the user and prints out the binary equivalent number.


# How do we get a binary string from an integer? The easiest method uses integer division by 2 on successive quotients and then collects the remainders. It is best illustrated by an example. Consider the integer 156:

# 156 divided by 2 gives the quotient 78 and remainder 0.

# 78 divided by 2 gives the quotient 39 and remainder 0.

# 39 divided by 2 gives the quotient 19 and remainder 1.

# 19 divided by 2 gives the quotient 9 and remainder 1.

# 9 divided by 2 gives the quotient 4 and remainder 1.

# 4 divided by 2 gives the quotient 2 and remainder 0.

# 2 divided by 2 gives the quotient 1 and remainder 0.

# 1 divided by 2 gives the quotient 0 and remainder 1.

# Stop at reaching a quotient of 0. The binary equivalent is given by concatenating the remainders, in reverse (so the last remainder is the most significant bit and the first is the least). In this example: 10011100

# Note: You should implement the above algorithm using a loop and string methods.  Don't use format in this exercise!

my_int = int(input('Give me an int >= 0: '))
my_int1 = my_int
bin_str = ""
# Fill in the missing code
if my_int == 0:
    bin_str += "0"
while my_int1 > 0:
    if my_int1 % 2 == 0:
        my_int1 = my_int1//2
        bin_str += "0"
    elif my_int1 % 2 != 0:
        bin_str += "1"
        my_int1 = my_int1//2

print("The binary of", my_int, "is", bin_str[::-1])