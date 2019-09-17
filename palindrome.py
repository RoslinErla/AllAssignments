def is_palindrome(Sentence):
    Sentence = str(Sentence.lower())
    new_sentence=""
    for char in Sentence:
        if char.isalpha():
            new_sentence += char

    if new_sentence[::1] == new_sentence[::-1]:
        result = "is a palindrome."
    else:
        result = "is not a palindrome."
    return result
    

in_str=input("Enter a string: ")
is_it_palindrome = is_palindrome(in_str)

print('"'+in_str+'"', is_it_palindrome)

