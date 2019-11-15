

def open_file(filename):
    file_object = open(filename, "r")
    return file_object

def read_file(file_object,line_number):
    counter = 1
    for line in file_object:
        line = line.strip()
        if line_number == counter:
            print(line)
            break
        counter += 1

def get_line_number():
    try:
        line_num = int(input("Enter a line number: "))
        return line_num
    except ValueError:
        return 0

def main():
    filename =input("Enter filename: ")
    line_num = get_line_number()

    file_object = open_file(filename)
    read_file(file_object, line_num)
    file_object.close



main()