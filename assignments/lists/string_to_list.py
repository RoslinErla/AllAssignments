# Write a function called 'to_list' that takes a string as a parameter and returns a list of words in the string.

# "Words" are entities that are seperated by either commas (',') or spaces (' '). In case the string contains neither commas nor spaces, a list should be returned containing a single element.

# Note: We are not testing for the case where both commas and spaces are present in the string so feel free to ignore that.

# Example input/output:

# Enter the string: this is a string

# ['this', 'is', 'a', 'string']

 

# Enter the string: Pranshu,Enbody,Alireza

# ['Pranshu', 'Enbody', 'Alireza']

def to_list(string):
    if " " in string:
        new_string = string.split(" ")
    else:
        new_string =string.split(",")
    return new_string

the_string = input("Enter the string: ")
print(to_list(the_string))


