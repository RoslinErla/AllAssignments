# Write a program that reads a text file (you don't have to error check the filename), 
# keeps a count of the individual words in the file using a dictionary 
# and finally converts the dictionary to a list of tuples 
# and prints out a sorted version of the list.  
# The main program is given, do not change it.
 
# Note that the counts are not case-sensitive, that is, 'Word' is the same as 'word' or 'wORd'.

# Also, note that your program should account for if a punctuation (like a comma) 
# appears at the end of a word. 

# I do not think there is any thrill that can go through the human heart,
# like that felt by the inventor as he sees some creation of the brain
# unfolding to success.
# Such emotions make a man forget food, sleep, friends, love, everything.
# Nikola Tesla
# [('a', 1), ('any', 1), ('as', 1), 
# ('brain', 1), ('by', 1), ('can', 1), 
# ('creation', 1), ('do', 1), ('emotions', 1), 
# ('everything', 1), ('felt', 1), ('food', 1), 
# ('forget', 1), ('friends', 1), ('go', 1), ('he', 1), 
# ('heart', 1), ('human', 1), ('i', 1), ('inventor', 1),
#  ('is', 1), ('like', 1), ('love', 1), 
#  ('make', 1), ('man', 1), ('nikola', 1), 
#  ('not', 1), ('of', 1), ('sees', 1), ('sleep', 1),
#   ('some', 1), ('success', 1), ('such', 1), ('tesla', 1), 
#   ('that', 2), ('the', 3), ('there', 1), ('think', 1), 
#   ('thrill', 1),('through', 1), ('to', 1), ('unfolding', 1)]

import string

def get_word_list(file_stream):
    file_list=[]

    for line in file_stream:
        line = line.strip()
        line = line.split()
        for elements in line:
            elements = elements.strip(string.punctuation)
            file_list.append(elements)

    return file_list

def word_list_to_counts(file_list):
    word_count_dict = {}
    for elements in file_list:
        if elements.lower() not in word_count_dict:
            word_count_dict[elements.lower()] = 1
        else:
            word_count_dict[elements.lower()] += 1
    return word_count_dict


def dict_to_tuple(word_dict):
    word_dict = tuple(word_dict.items())
    return word_dict

def main():
    filename = input("Name of file: ")
    # Get a file stream
    fstream = open(filename)
    # Get a list of words from the stream
    word_list = get_word_list(fstream) 
    fstream.close()
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))
    
main()