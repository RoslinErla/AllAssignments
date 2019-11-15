# Write a program that reads a file called 'test.txt' 
# and prints out the contents on the screen after removing all spaces and newlines. Punctuations will be preserved.
# For example, if 'test.txt' contains:

# This is a test file, for chapter 06.
# This a new line in the file!

# Then, your program's output will show:
# Thisisatestfile,forchapter06.Thisanewlineinthefile!
# Hint:  Consider using the strip() and replace() functions.





def open_file(filename):
    file_object = open(filename, "r")
    return file_object

def read_file(file_object):
    for line in file_object:
        line = line.strip().replace(" ","")
        print(line, end="")

def main():
    filename = "test.txt"
    file_object = open_file(filename)
    read_file(file_object)
    file_object.close


main()