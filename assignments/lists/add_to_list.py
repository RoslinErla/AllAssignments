#Write a program that keeps asking the user for new values to be added to a list
#  until the user enters 'exit' ('exit' should NOT be added to the list). 
# After that, the program creates a new list with 3 copies of every value in the initial list. 
# Finally, the program prints out all of the values in the new list.


def stop(final_list):
    the_final_list = final_list * 3
    for char in the_final_list:
        print(char)


def main():
    the_list = []
    input_str = input("Enter value to be added to list: ")
    while input_str != "exit":
        the_list.append(input_str)
        input_str = input("Enter value to be added to list: ")
    else: 
        stop(the_list)

main()