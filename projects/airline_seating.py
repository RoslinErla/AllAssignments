def seat_and_row_list(seat_list,alphabet):
    """ Makes a list of all the rows and seats"""
    num_of_rows = int(input("Enter number of rows: "))
    num_of_seats = int(input("Enter number of seats in each row: "))
    while len(seat_list) < num_of_rows: # while there are not enough rows you keep making lists
        row_list = [] # a list of all the seats in each row
        for num in range(num_of_seats): 
            row_list.append(alphabet[num]) #You add as many letters from the alphabet as there are supposed to be seats
        seat_list.append(row_list)

def any_seats_left(seat_list,alphabet):
    """Checks if there are any seats left on the plane"""
    seats_left_counter = 0 
    for lists in seat_list: #We are looking at all the rows and seats to check if there are any left
        for elements in lists:
            if elements != "X":
                seats_left_counter += 1 #We count how many seats are left. If they are marked x they are booked and can't be booked again
    if seats_left_counter >0: #If there are any seats left then people can keep booking them so we keep asking them. Else we stop the program.
        more_seats(seat_list,alphabet)

def making_half_list(half_list):
    half_str = ""
    for elements in half_list:
        half_str += elements  #Make it into a string so I can print it out
        half_str += " "
    return half_str


def print_seat(seat_list):
    row_number = 1
    for lists in seat_list: #Look at all the lists/rows in the seat_lists
        length = len(lists) #Check how long the list is 
        half = length//2 #I find out how many elements are supposed to be on each side of the aisle
        first_half_str = making_half_list(lists[:half])
        second_half_str = making_half_list(lists[half:])

        print("{:>2}   {:}  {:}".format(row_number, first_half_str, second_half_str)) # Printing it in the right format
        row_number += 1

def more_seats(seat_list,alphabet):
    """Function to ask if the user wants to book more seats"""
    yes_or_no = input("More seats (y/n)? ")
    if yes_or_no == "y":
        book_seats(seat_list,alphabet)

def book_seats(seat_list,alphabet):
    """books the seats"""
    n = input("Input seat number (row seat): ")
    row,seat = tuple(n.split())
    seat_index = alphabet.index(seat) #If it is the 3. letter in the alphabet then it's also going to be the 3. seat

    try:
        row = int(row) - 1
        if seat_list[row][seat_index] == "X": #If the seat is already booked it is marked with an x and then it's not available
            print("That seat is taken!")
            book_seats(seat_list,alphabet) #It repeats the function. It asks you again

        elif seat_list[row][seat_index] == seat: #If the seat is available then you book it. Now it is marked with an X 
            seat_list[row][seat_index] = "X"
            print_seat(seat_list)
            any_seats_left(seat_list, alphabet) 

    except IndexError: #If you chose a row or seat that is not there then this happens
            print("Seat number is invalid!")
            book_seats(seat_list,alphabet)

    except ValueError: #If the input "row" is something other than an integer then this happens
        print("Seat number is invalid!")
        book_seats(seat_list,alphabet)

def main():
    seat_list = []
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    seat_and_row_list(seat_list,alphabet)
    print_seat(seat_list)
    book_seats(seat_list,alphabet)

main()