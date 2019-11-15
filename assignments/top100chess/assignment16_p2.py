COUNTRY = 1
RATING = 2
BYEAR = 3

def open_file():
    """Open the given file name and returns the file stream, or None if the file cannot be opened"""
    filename = input("Enter filename: ")
    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError:
        return None

def create_players_dict(file_object):
    """ Reads the given file stream and returns a dictionary in which 
    the name of a chess player is the key, the value is a tuple:
    (rank,country, rating, b-year)"""
    player_dict = dict()

    for line in file_object:
        rank, name, country, rating, birth = line.split(";")
        last_name, first_name = name.split(",")
        first_name = first_name.strip()
        last_name = last_name.strip()
        country = country.strip()

        key = "{} {}".format(first_name, last_name)
        value_tuple = (int(rank), country, int(rating), int(birth) )
        player_dict[key] = value_tuple

    return player_dict

def create_country_dict(player_dict):
    """Uses a players dictionary to create a countries dictionary 
       in which countries are key and a list of player names are values"""
    country_dict = dict()

    for chess_player, chess_player_data in player_dict.items():
        country = chess_player_data[COUNTRY]

        if country in country_dict:
            name_list = country_dict[country]
            name_list.append(chess_player)

        else: 
            name_list = [chess_player]
            country_dict[country] = name_list

    return country_dict

def create_birth_dict(player_dict):
    """Uses the players dictionary to create a birth year dictinary
       in which birth year is the key and a list of players name are values"""
    birth_year_dict = dict()

    for chess_player, chess_player_data in player_dict.items():
        birth_year = chess_player_data[BYEAR]

        if birth_year in birth_year_dict:
            name_list = birth_year_dict[birth_year]
            name_list.append(chess_player)
        else:
            name_list = [chess_player]
            birth_year_dict[birth_year] = name_list
    return birth_year_dict

def get_average_rating(players, player_dict):
    """Returns the average ratings for the given players"""

    ratings = [player_dict[player][RATING] for player in players]
    average = sum(ratings)/len(ratings)

    return average

def header_print(header_string):
    print(header_string)
    dashes = "-" * len(header_string)
    print(dashes)

def print_sorted(a_dict, player_dict):
    """Prints information sorted on the key of a_dict"""
    sorted_dict = sorted(a_dict.items())
    for key, players in sorted_dict:
        average_rating = get_average_rating(players, player_dict)
        print("{} ({}) ({:.1f}):".format(key, len(players), average_rating))
        for player in players:
            rating = player_dict[player][RATING]
            print("{:>40}{:>10d}".format(player, rating))

def main():
    file_object = open_file() 
    if file_object:
        player_dict = create_players_dict(file_object)
        country_dict = create_country_dict(player_dict)
        header_print("Players by country:")
        print_sorted(country_dict, player_dict)
        birth_dict = create_birth_dict(player_dict)
        header_print("Players by birth year:")
        print_sorted(birth_dict, player_dict)
        file_object.close()

main()