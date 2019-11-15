# Write a program that accepts a list of numbers as an argument 
# and then prints 'True' if two consecutive eights are found in the list. 
# The program prints out an error message saying 
# 'Error - please enter only integers.' if the list is found to contain any non-numeric characters. 

# Examples:

# Enter elements of list separated by commas: 2,3,8,8,5
# True
# Enter elements of list separated by commas: 3,4,5,8
# False
# Enter elements of list separated by commas: 2,3,5,8,8,x
# Error - please enter only integers.

def consecutive_eights(a_list):
    if 8 in a_list:
        index_of_eight = a_list.index(8) #Checking where the 8 is
        if len(a_list) >= (index_of_eight + 2): #if the 8 is the last element in the list then it can not be consecutive
            if a_list[index_of_eight + 1]== 8: #If there is an 8 next to the other 8 its consecutive so it prints True
                print(True)
            else:
                print(False) #Else it always prints False
        else: 
            print(False)
    else:
        print(False)

def main():
    numbers = input("Enter elements of list separated by commas: ").split(",")
    try: 
        numbers = list(map(int, numbers))
        consecutive_eights(numbers)
        
    except ValueError:
        print("Error - please enter only integers.")

main()
