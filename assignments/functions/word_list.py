# This program builds a wordlist out of all of the words found in an input file 
# and prints all of the unique words found in the file in alphabetical order. 
# Remove punctuations using 'string.punctuation' and 'strip()' before adding words to the wordlist.
# Make your program readable!
# Example input file test.txt:
# the test file!
# another line in the test file.
# third, is this a good test?
# Input/Output:
# Enter filename: test.txt
# ['a', 'another', 'file', 'good', 'in', 'is', 'line', 'test', 'the', 'third', 'this']
import string

def open_file(filename):
    file_object = open(filename, "r")
    return file_object

def read_file_and_remove_punct(file_object):
    empty_list = []
    punct = string.punctuation
    for word in file_object:	# process each line/word
        word = word.strip() # strip leading and trailing white space
        word = word.split(" ")
        for elements in word:
            if elements[-1] in punct or elements[0] in punct:
                elements = elements.strip(punct)
            if elements not in empty_list:
                empty_list.append(elements)
    return empty_list

def sorted_list(a_list):
    a_list.sort()
    print(a_list)

def main():
    filename = input("Enter filename: ")
    file_object = open_file(filename)
    word_list = read_file_and_remove_punct(file_object)
    sorted_list(word_list)

main()