START = 1
END= 10

def starting_point(number):
    empty_string= ""
    for numbers in range (START,END+1):
        if number == numbers:
            empty_string += "o"
        else:
            empty_string += "x"
    return empty_string

def instructions():
    return print("l - for moving left"), print("r - for moving right"), print("Any other letter for quitting")
    
def move(left_or_right):
    new_location = location
    empty_string=""
    location_of_o= new_location.find("o")
    #If you try to leave the range you end up in the last place you.
    if location_of_o == 0 and left_or_right=="l":
        empty_string = "oxxxxxxxxx"
        result=empty_string
    elif location_of_o ==9 and left_or_right =="r":
        empty_string = "xxxxxxxxxo"
        result= empty_string
    elif left_or_right=="r":
        location_of_o +=1
        for number in range (START-1,END):
            if number ==location_of_o:
                empty_string += "o"
            else:
                empty_string += "x"
        result = empty_string
    elif left_or_right == "l":
        location_of_o=new_location.find("o")
        location_of_o -=1
        for number in range(START-1,END):
            if number == location_of_o:
                empty_string += "o"
            else:
                empty_string += "x"
        result=empty_string
    elif left_or_right != "l" and left_or_right !="r":
        result= location
    return result


start=int(input("Input a position between 1 and 10: "))
location= starting_point(start)
print(location)

instructions=instructions()

where_to_next= (input("Input your choice: "))
location=move(where_to_next)
print(location)
while where_to_next == "l" or where_to_next =="r":
    where_to_next = (input("Input your choice: "))
    location = move(where_to_next)
    print(location)

