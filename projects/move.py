START= 1
END= 10

#Getting the user to pick a starting point
def starting_point(number):
    empty_string= ""
    for numbers in range (START,END+1):
        if number == numbers:
            empty_string += "o"
        else:
            empty_string += "x"
    return empty_string

#Printing out instructions for the user
def instructions():
    print("l - for moving left") 
    print("r - for moving right")
    print("Any other letter for quitting")

#What we want the program to do if the input is "l"
def move_left(left):
    empty_string=""
    location_of_o = location.find("o") + 1
    if location_of_o > START :
        location_of_o -= 1
    empty_string = starting_point(location_of_o)
    return empty_string

#What we want the program to do if the input is "r"
def move_right(right):
    empty_string=""
    location_of_o = location.find("o") + 1
    if location_of_o < END:
        location_of_o += 1
    empty_string = starting_point(location_of_o)

    return empty_string
#What we want to happen if the input is something other than "r" or "l"
def quit(location):
    new_location = location 
    return print(new_location)

start= int(input("Input a position between 1 and 10: "))

location = starting_point(start)
print(location)

#Printing out instructions for the program
instructions()

#Getting the next location. Do you want to go right or left.
where_to_next = input("Input your choice: ")
#Now we show the location and if they want to keep on moving on the x-axis they can by inputting "r" or "l"
while where_to_next == "r" or where_to_next == "l":
    if where_to_next == "r":
        location = move_right(where_to_next)
    elif where_to_next == "l":
        location = move_left(where_to_next)
    print(location)
    where_to_next = input("Input your choice: ")

else: 
    quit(location)