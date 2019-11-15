# A set is a collection of distinct elements.  
# For example, the list [1, 3, 2] is a set, 
# whereas [1, 2, 3, 2] is not (because the element 2 appears twice). 
#  A sorted set is a set whose elements are sorted. 
# If the list [1, 3, 2] denotes a set, then [1, 2, 3] is a sorted version of it. 
# Write a Python program that:
# Reads integer elements into two lists (space between elements in input), 
# converts the lists into sorted sets and prints out the sets.  
# No error checking of the input is needed.
# Constructs a sorted intersection of the two sets and prints it out.
# Constructs a sorted union of the two sets and prints it out. 
# The Intersection of two sets A and B is the set that contains all elements of A that also belong to B. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B.

# You are not allowed to use any import statement in your implementation.

def making_sets(lists):
    """Makes sure that an element is only once in a set"""
    empty_set = []
    lists =lists.split()
    for elements in lists:
        if elements == " ":
            next
        else:
            if elements not in empty_set:
                empty_set.append(elements) 
    return empty_set

def sort_sets(sets):
    sets = list(map(int, sets))
    sets.sort()
    new_sets = sets
    return new_sets

def intersection(A,B):
    """Creates the intersection for both sets"""
    set_A = A
    set_B = B
    sorted_intersection = []
    for elements in set_A:
        if elements in set_B:
            sorted_intersection.append(elements)
    return sorted_intersection 

def union(A,B):
    """Creates the union for both sets"""
    set_A = A
    set_B = B
    sorted_union = []
    for elements in set_A:
        if elements not in sorted_union:
            sorted_union.append(elements)
    for elements in set_B:
        if elements not in sorted_union:
            sorted_union.append(elements)
    return sorted_union


def main():
    A = input("Enter elements of a list separated by space: ")
    B = input("Enter elements of a list separated by space: ")

    setA = making_sets(A)
    setB = making_sets(B) 
    sorted_set_A = sort_sets(setA)
    sorted_set_B = sort_sets(setB)

    intersection_of_A_and_B = intersection(sorted_set_A, sorted_set_B)
    sorted_intersection = sort_sets(intersection_of_A_and_B)

    union_of_A_and_B = union(sorted_set_A, sorted_set_B)
    sorted_union = sort_sets(union_of_A_and_B)

    print("Set 1: ", sorted_set_A)
    print("Set 2: ", sorted_set_B)
    print("Intersection: ", sorted_intersection)
    print("Union: ", sorted_union)
main()