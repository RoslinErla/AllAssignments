# Write a function merge_lists that takes two lists as arguments, 
# merges them into a third list without duplicates and returns the third list sorted.
# The elements of each list are strings.

def merge_lists(list1,list2):
    list3 = []
    for element in list1:
        if element not in list3:
            list3.append(element)
    for element in list2:
        if element not in list3:
            list3.append(element)
    list3.sort()
    return list3



# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
