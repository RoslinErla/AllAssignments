# Write a program that prompts the user for a name.  The program then splits the name into first and last name (case insensitive).

# Then it:

# calls a function that returns a list of the common letters in first and last. The data structures used in this implementation can only be lists.
# calls a function that returns a set containing the common letters in first and last.  The data structures used in this implementation can only be sets.
# prints out a sorted list version of the results from 1) and 2)
# Example input/output:
import string

def first_and_last(name):
    first,last = name.split()
    return first,last

def list_of_common_letters(first,last):
    common_list = []
    for letters in first:
        letters = letters.lower()
        if letters not in common_list:
            if letters in last:
                common_list.append(letters)

    return common_list

def set_of_common(first,last):
    first_set = set(first.lower())
    last_set = set(last.lower())
    common_set = first_set & last_set
    return common_set

def main():
    name = input("Enter name: ")
    first,last = first_and_last(name)
    print(sorted(list_of_common_letters(first,last)))
    print(sorted(set_of_common(first,last)))

main()
