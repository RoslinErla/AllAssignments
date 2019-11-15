#Write a program that makes a list of the unique letters in an input sentence.  That is, if the letter "x" is used twice in a sentence, it shouild only appear once in your list.  Neither punctuation nor white space should appear in your list.  The letters should appear in your list in the order they appear in the input sentence.
import string

# Implement a function here
def unique_letters(sentence):
    unique = []
    punctuation = string.punctuation
    sentence = sentence.replace(" ", "")
    sentence = sentence.replace(punctuation, "")
    for letters in sentence:
        if letters in punctuation:
            letters.replace(punctuation,"")
        elif letters not in unique:
            unique.append(letters)
    return unique


# Main starts here
sentence = input("Input a sentence: ")
# Call the function here
unique_letters = unique_letters(sentence)
print("Unique letters:", unique_letters)