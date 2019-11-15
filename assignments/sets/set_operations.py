# Write a program that:


# Reads in two lists of integers from the user and converts them to sets and prints out the sets.
# Allows the user to repeatedly perform intersection, union and difference on the two sets and prints out the result of each operation
# Example input/ouput:

 
# Input a list of integers separated with a comma: 1,2,3,4
# Input a list of integers separated with a comma: 1,1,3,3,5,6
# {1, 2, 3, 4}
# {1, 3, 5, 6}
# 1. Intersection
# 2. Union
# 3. Difference
# 4. Quit
# Set operation: 1
# {1, 3}
# 1. Intersection
# 2. Union
# 3. Difference
# 4. Quit
# Set operation: 2
# {1, 2, 3, 4, 5, 6}
# 1. Intersection
# 2. Union
# 3. Difference
# 4. Quit
# Set operation: 3
# {2, 4}
# 1. Intersection
# 2. Union
# 3. Difference
# 4. Quit
# Set operation: 4

def make_list():
    first_input = input("Input a list of integers separated with a comma: ").split(",")
    first_list = map(int,first_input)
    second_input = input("Input a list of integers separated with a comma: ").split(",")
    second_list = map(int,second_input)
    return first_list,second_list

def make_set(list1,list2):
    set_1 = set(list1)
    set_2 = set(list2)
    return set_1,set_2

def pick_operation():
    print("1. Intersection")
    print("2. Union")
    print("3. Difference")
    print("4. Quit")
    operation = input("Set operation: ")
    return operation

def intersection(set_a,set_b):
    intersection_set = set_a & set_b
    print(intersection_set)

def union(set_a,set_b):
    union_set = set_a | set_b
    print(union_set)

def difference(set_a,set_b):
    difference_set = set_a - set_b
    print(difference_set)

def what_happens(operation,set_1,set_2):
    if operation == "1":
        intersection(set_1,set_2)
    elif operation == "2":
        union(set_1,set_2)
    elif operation == "3":
        difference(set_1,set_2)

def main():
    list_a,list_b = make_list()
    set_a,set_b = make_set(list_a,list_b)
    print(set_a)
    print(set_b)
    operation = pick_operation()
    while operation != "4":
        what_happens(operation,set_a,set_b)
        operation = pick_operation()

main()