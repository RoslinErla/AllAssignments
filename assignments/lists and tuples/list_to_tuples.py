# Write a function that takes a list as a parameter, 
# converts every element in the list to an integer and then returns a tuple 
# comprising of these integer elements.
# If the function encounters a character such as 'p' that cannot be converted to an integer,
#  it throws this error message on the screen: "Error. Please enter only integers."
# and returns an empty tuple
# The main program is given - DO NOT change it.

#list_to_tuple function goes here
def list_to_tuple (lists):
    try:
        empty_list = ()
        empty_list = list(map(int, lists))
        return tuple(i for i in empty_list)
    except:
        print("Error. Please enter only integers. ")
        return empty_list


# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)