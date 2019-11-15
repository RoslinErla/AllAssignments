def open_file(filename):
    file_object = open(filename, "r")
    return file_object

def read_file(filename):
    """reads the file and makes a list of all the lines"""
    population_list = []
    line_counter = 0
    number_of_columns = 0
    for line in filename:
        line = line.split()
        if line_counter == 0:
            number_of_columns = len(line) #Seeing how long the original line is so if there are more than one words in the state name I can put them together when the time comes
            line_counter += 1
            population_list.append(line)
        else:
            length_check = len(line) - number_of_columns #Checking the length of the other lines 
            # If the next line is the same length as the previous one nothing happens but if it's longer you put the first two together
            us_state = " ".join(line[0:1 + length_check])
            state = [us_state] #creates a list with just the state
#makes a list of all elements in the line other than the state so if the state has two names we can account for it
            population = [int(elements) for elements in line[length_check + 1:]] 
            state.extend(population) # puts together the state and all other elements into one list 
            population_list.append(state) #here is the list of all the other lists we made
    return population_list

def find_year(population_list):
    """Checks if the year is valid and if it is it outputs in which column it is"""
    year = input("Enter year: ")
    while year not in population_list[0]:
        print("Invalid year!")
        year = input("Enter year: ")
    else: 
        location_in_columns = population_list[0].index(year)
        return location_in_columns

def minimum_population(population_list,location):
    """Finds the minimum population and state"""
    minimum = population_list[1][location]
    state = population_list[0][0]
    for lists in population_list[1:]:
        if lists[location] < minimum:
            minimum = lists[location]
            state = lists[0]
    return minimum, state

def maximum_population(population_list, location):
    """Finds the maximum population and state"""
    maximum = population_list[1][location]
    state = population_list[0][0]
    for lists in population_list[1:]:
        if lists[location] > maximum:
            maximum = lists[location]
            state = lists[0]
    return maximum,state

def main():
    filename = input("Enter filename: ")
    try:
        file_object = open_file(filename)
        population_list = read_file(file_object)
        location_of_year = find_year(population_list)
        print("Minimum: " ,minimum_population(population_list, location_of_year))
        print("Maximum: " ,maximum_population(population_list, location_of_year))
        file_object.close

    except FileNotFoundError:
        print("Filename {} not found!".format(filename))
    
main()
