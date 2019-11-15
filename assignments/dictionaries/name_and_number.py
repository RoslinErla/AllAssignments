# Write a program that asks for name from the user 
# and then asks for a number and stores the two in a dictionary as key-value pair.
# The program then asks if the user wants to enter more data (More data (y/n)? ) 
# and depending on user choice, either asks for another name-number pair or exits.  
# Finally, it stores the dictionary key, values 
# in a list of tuples and prints a sorted version of the list.

# Note: If a name is already in the dictionary, the old value should be overwritten.

# Example:
# Name: pranshu
# Number: 517-244-2426
# More data (y/n)? y
# Name: rich
# Number: 517-842-5425
# More data (y/n)? y
# Name: alireza
# Number: 517-432-5224
# More data (y/n)? n
# [('alireza', '517-432-5224'), ('pranshu', '517-244-2426'), ('rich', '517-842-5425')]

more_input = True
contact_dict = {}
while more_input:
    name = input("Name: ")
    number = input("Number: ")
    contact_dict[name] = number
    more_inp = input("More data (y/n)? ")
    if more_inp == "y":
        next
    else: 
        more_input = False

print(list(sorted(contact_dict.items())))


