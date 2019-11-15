# Write functions get_list() and sort_list().  
# get_list() reads numbers from the user, until a non-digit string is entered 
# (you could use try-except for this), and stores them in a list.  
# sort_list() accepts a list of integers and sorts it. 
# The function should not explicitly return this list 
# and yet the list will be sorted when printed within main() 
# after being passed to sort_list() as a parameter.
# Example input/output:
# 2
# 32
# 43
# 12
# 24
# 32
# x
# [2, 32, 43, 12, 24, 32]
# None
# [2, 12, 24, 32, 32, 43]

def sort_list(a_list):
    a_list = a_list.sort()
# sort_list() function goes here


def get_list():
    empty_list = []
    while True:
        try:
            number = int(input("Please"))
            empty_list.append(number)
            continue
        except:
            return empty_list
# get_list() function goes here


# Do not modify this part
def main():
    a_list = get_list()
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    
main()