import string

def scramble_file_content(filename):
    data_file = open(filename, "r")
    for word in data_file:
        word = word.strip() # remove the carriage return
        scrambled_word = scramble(word)
        print(scrambled_word, end=' ')
    print()
    data_file.close()

def swap_adjacent(sequence):
    odd = False
    length = len(sequence)
    if length % 2 != 0:     # odd number of characters in sequence
        length -= 1
        odd = True

    scrambled_sequence = ''
    for i in range(0,length,2):
        scrambled_sequence += sequence[i+1] + sequence[i]
    if odd:
        scrambled_sequence += sequence[-1]  # Add the last letter of the sequence

    return scrambled_sequence


def scramble(word):
    
    if len(word) <= 3:
        return word

    last_index = -1
    last_letter = word[-1]
    if last_letter in string.punctuation:
        last_index -= 1

    sequence = word[1:last_index]   # excluding the first and last letters
    scrambled_sequence = swap_adjacent(sequence)
    scrambled_word = word[0] + scrambled_sequence + word[last_index:]
    
    return scrambled_word

def main():
    filename = input("Enter name of file: ")
    try:
        scramble_file_content(filename)
    except FileNotFoundError:
        print("File {} not found!".format(filename))

main()