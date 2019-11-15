#Write a function that takes a list L of integers as an argument
#  and uses list comprehension to return the sum of the even integers in the list L.



def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def even_sum(lists):
    the_sum = 0
    for char in lists:
        char = int(char)
        if char % 2 == 0:
            the_sum += char
    return the_sum

# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
