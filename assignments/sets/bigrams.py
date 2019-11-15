# Write a program that reads in a file and prints out the 10 most frequent bigrams in the file. 
#  A bigram is a sequence of two adjacent words.

# Note that you should use a dictionary (not a set) in this project, 
# because you need to keep track of the counts of each bigram (thus a key-value pair).

# Further instructions:

# all words need to be converted to lower case
# all words need to be stripped of punctuations
# The keys in the bigram dictionary should be tuples (word1, word2)
# The values are the occurences of the given bigram in the text
# Dictonaries are unordered collections. You can however, transform a dictionary to a list of tuples (using the items() method) and then sort it.  Look at itemgetter on pages 355-356 in the textbook.
import string

def open_file():
    filename = input("Enter name of file: ")
    file_object = open(filename,"r")
    return file_object

def read_file_and_strip(file_object):
    word_list= []
    for line in file_object:
        line= line.strip()
        line = line.split()
        for word in line:
            word = word.strip(string.punctuation)
            word_list.append(word.lower())
    return word_list

def bigrams(file_object_list):
    tuple_list = []
    i = 0
    while i < len(file_object_list)-1:
        bigram_list = [file_object_list[i]]
        bigram_list.append(file_object_list[i+1])
        tuple_list.append(tuple(bigram_list))
        i += 1
    return tuple_list

def bigram_dict(list_of_tuples):
    bigram_dict = dict()
    for tuples in list_of_tuples:
        if tuples in bigram_dict:
            bigram_dict[tuples] += 1
        else:
            bigram_dict[tuples] = 1

    return bigram_dict

def top_10(dictionary):
    print(sorted(dictionary.items(), reverse = True, key = lambda item: item[1])[:10])


def main():
    file_object = open_file()
    word_list = read_file_and_strip(file_object)
    tuple_list = bigrams(word_list)
    bigram_dictionary = bigram_dict(tuple_list)
    top_10(bigram_dictionary)
    



    file_object.close()

main()