# Write code which prints the index location of each letter 'o' in the string, one location per line of output.

# Hint: enumerate() is your friend!

 

# Given the string a_str = 'happiness is when what you think, what you say, and what you do are in harmony. - gandhi'

# the output will be:

# 24

# 40

# 58

# 62

# 75

a_str = input("Input a string: ")
for index, char in enumerate(a_str):
    if char == "o":
        print(index)