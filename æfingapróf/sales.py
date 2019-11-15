# Gögn í hverri línu eiga við ákveðna deild í tilteknu fyrirtæki.
#  Sérhver lína inniheldur runu af N sölutölum með einu bili á milli allra talna. 
#  T.d. inniheldur þriðja línan (sem á við deild nr. þrjú) runu af átta sölutölum.

# Skrifið Python forrit sem les skrá eins og þessa hér að ofan, 
# reiknar út meðalsölu fyrir sérhverja deild og skrifar niðurstöðuna (með einum aukastaf) út á skjá. 
# Forritið skal spyrja notandann um nafn á inntaksskránni 
# og skrifa út villuboð og hætta keyrslu ef ekki er hægt að opna inntaksskrána. 
#  Athugið að fallið sem les gögnin úr skránni má hvorki reikna neitt út né skrifa á skjáinn.

def open_file():
    filename = input("Enter file name: ")
    try:
        file_object = open(filename,"r")
        return file_object
    except FileNotFoundError:
        return None

def read_file_and_make_list(file_object):
    line_list = list()
    for line in file_object:
        line = line.strip().split()
        line_list.append(line)
    return line_list

def find_average(line_list):
    ave_list = list()
    for lists in line_list:
        sum_of_sale_num = 0
        for elements in lists:
            elements = float(elements)
            sum_of_sale_num += elements
        average = sum_of_sale_num / len(lists)
        ave_list.append(average)
    return ave_list

def print_average(ave_list):
    print("Average sales:")
    for i in range(len(ave_list)):
        format_string = "Department no. {}: {:.1f}".format(i + 1,ave_list[i])
        print(format_string)



def main():
    file_stream = open_file()
    if file_stream:
        sales_list = read_file_and_make_list(file_stream)
        average = find_average(sales_list)
        print_average(average)
    else: 
        print("File not found!")

main()