# Write a Python program that allows the user to perform three operations on a dictionary:

# add_to_dict(): takes a dictionary, a key, a value and adds the key,value pair to the dictionary.
#  If key is already in dictionary then it displays the error message: "Error. Key already exists.".
 
# remove_from_dict(): takes a dictionary and key and removes the key from the dictionary.  
# If no such key is found in the dictionary then it prints: "Key not found."

# find_key(): takes dictionary and key 
# and prints the value corresponding to the key from the dictionary:
#  print("Value: ", value). If key is not found, then prints: "Key not found." 
 
# The user is presented with a menu and repeatedly offered to perform an operation 
# until he/she quits.

# Finally, a list of the key-value pairs in the dictionary is printed out.

# The main program is given - do not change it.
# Menu: 
# add(a), remove(r), find(f): a
# Key: rich
# Value: 1
# More (y/n)? y
# Menu: 
# add(a), remove(r), find(f): a
# Key: alireza
# Value: 2
# More (y/n)? n
# [('alireza', '2'), ('rich', '1')]

# Menu: 
# add(a), remove(r), find(f): a
# Key: pranshu
# Value: 1
# More (y/n)? y
# Menu: 
# add(a), remove(r), find(f): r
# key to remove: enbody
# Key not found.
# More (y/n)? y
# Menu: 
# add(a), remove(r), find(f): a
# Key: mary 
# Value: 2
# More (y/n)? y
# Menu: 
# add(a), remove(r), find(f): f
# Key to locate: mary
# Value:  2
# More (y/n)? y
# Menu: 
# add(a), remove(r), find(f): f
# Key to locate: bla
# Key not found.
# More (y/n)? n
# [('mary', '2'), ('pranshu', '1')]

def menu_selection():
    print("Menu: ")
    operation = input("add(a), remove(r), find(f): ")
    return operation

def add_to_dict(a_dict,a_key,a_value):
    if a_key in a_dict:
        print("Error. Key already exists.")
    else:
        a_dict[a_key] = a_value

def remove_from_dict(a_dict, a_key):
    if a_key in a_dict:
        a_dict.pop(a_key)
    else: 
        print("Key not found.")

def find_key(a_dict, a_key):
    if a_key in a_dict:
        print("Value: ", a_dict[a_key])
    else: 
        print("Key not found.")



def execute_selection(choice,a_dict):
    if choice == "a":
        key = input("Key: ")
        value = input("Value: ")
        add_to_dict(a_dict,key,value)

    elif choice == "r":
        key = input("key to remove: ")
        remove_from_dict(a_dict,key)

    elif choice == "f":
        key = input("Key to locate: ")
        find_key(a_dict,key)



def dict_to_tuples(a_dict):
    a_dict = tuple(a_dict.items())
    return a_dict



# Do not change this main function
def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()