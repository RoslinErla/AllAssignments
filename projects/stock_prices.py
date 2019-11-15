def open_file(filename):
    #Opens and reads the file but if the file does not exist it returns none
    try:
        file_object = open(filename, "r")
        return file_object

    except FileNotFoundError:
        return None

def get_data_list(file_object):
    """Goes through the lines and splits it and adds it to a list"""
    data_list = []
    for line in file_object:
        line = line.strip().split(",")
        data_list.append(line)

    return data_list

def my_constants(file_list):
    """The constants that I need""" 
    #It finds the location of the date,the adj close, and the volume
    #Because those locations will be used a lot further on
    DATE = file_list[0].index("Date")
    ADJ_CLOSE = file_list[0].index("Adj Close")
    VOLUME = file_list[0].index("Volume")

    return DATE,ADJ_CLOSE,VOLUME

def monthly_averages_list(file_list,date,adj_close,volume):
    """finds the average for each month and adds it into a list with the date"""
    #average formula = (adj close * volume) / volume
    product = 0
    the_sum_of_volume = 0
    average = 0
    average_list = []
    first_date = file_list[1][0][0:7] #Something to compare the rest of the dates to

    for lists in file_list[1:]: #Start on the first line
        if lists[0][0:7] == first_date:
            product += float(lists[adj_close]) * float(lists[volume]) #Making it a float so I can multiply them together
            the_sum_of_volume += float(lists[volume])

        else: 
            average += product / the_sum_of_volume 
            date_and_average_list = [first_date,average] #A list with the date and the average
            average_list.append(date_and_average_list) #A list of all the dates and averages
            first_date = lists[0][0:7] #now make the list the next month
#I reset them so it doesnt just keep adding numbers to what is already in the list
            product = 0
            the_sum_of_volume = 0
            average = 0
#And then start with the new lines here. Finding the average
            product += float(lists[adj_close]) * float(lists[volume]) 
            the_sum_of_volume += float(lists[volume])

    else: 
        average += product / the_sum_of_volume
        date_and_average_list = [first_date,average]
        average_list.append(date_and_average_list)

    return average_list

def find_highest_price(file_list,date,adj_close):
    """Finds the maximum and the date"""
    date_of_maximum = file_list[1][date] #Have to start somewhere so I just start in the first line
    maximum = float(file_list[1][adj_close]) #Make the maximum into a float and then compare it with the rest of the adj close columnn

    for lists in file_list[1:]: #Skip the first line because that only has the header
        if float(lists[adj_close]) > maximum: 
            maximum = float(lists[adj_close])
            date_of_maximum = lists[date]

    return maximum, date_of_maximum

#The column "Month" should have the width 10 (left justified) 
# and the column "Price" the width 7 (right justified).  
# All numbers should be printed with two digits after the decimal point. 
# Use format strings to obtain the correct layout.
def print_info(monthly_averages_list,maximum,date_of_maximum):
    """Prints the average and maximum in the special format"""

    print("{:<10s}{:>7s}".format("Month","Price"))

    for lists in monthly_averages_list:
        print("{:<10s}{:>7.2f}".format(lists[0],lists[1]))

    print("Highest price {:>5.2f} on day {}".format(maximum,date_of_maximum))

def main():
    filename = input("Enter filename: ")
    file_object = open_file(filename)

    if file_object == None:
        print("Filename",filename,"not found!")

    else:
        file_list= get_data_list(file_object)
        DATE, ADJ_CLOSE, VOLUME = my_constants(file_list)
        monthly_average = monthly_averages_list(file_list, DATE,ADJ_CLOSE, VOLUME)
        highest,date = find_highest_price(file_list,DATE,ADJ_CLOSE)
        print_info(monthly_average,highest,date)

main()