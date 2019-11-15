#Write a Python program that reads a file, input by the user,
#  containing one word/token per line with an empty line between sentences. 
#  The program prints out the longest word found in the file along with its length.

def open_file(filename):
    file_object = open(filename, "r")
    return file_object

def read_file_and_find_longest_word(file_object):
    counter = 0
    longest = "innflutningstolla"
    for line in file_object:
        line = line.strip().replace(" ", "\n")
        if len(line) > len(longest):
            longest = line
    for char in longest:
        counter += 1
    print("Longest word is", longest, "of length", counter)


def main():
    filename =input("Enter filename: ")

    file_object = open_file(filename)
    read_file_and_find_longest_word(file_object)
    file_object.close



main()