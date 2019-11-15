def open_file(filename):
    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError:
        return None

def read_file_and_make_dict(file_object):
    fly_dict = dict()
    for line in file_object:
        name, country = line.split()
        if name not in fly_dict:
            fly_dict[name] = {country}
        else:
            fly_dict[name].add(country)
    return fly_dict

def print_from_dict(file_dict):
    for name in sorted(file_dict.keys()):
        print("{}:".format(name))
        for country in sorted(file_dict[name]):
            print("\t{}".format(country))

def find_max(file_dict):
    max_countries = 0
    max_flier = ""
    for names,country in file_dict.items():
        if len(country) > max_countries:
            max_countries = len(country)
            max_flier = names
    return max_flier,max_countries

def print_max(name,count):
    format_line = "{} has been to {} countries".format(name,count)
    print(format_line)






def main():
    filename = "flights.txt"
    file_stream = open_file(filename)
    flyers_dict = read_file_and_make_dict(file_stream)
    print_from_dict(flyers_dict)
    name,count = find_max(flyers_dict)
    print_max(name,count)

main()
