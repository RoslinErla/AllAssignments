# Write a function named count_case that takes a string as an argument 
# and returns the count of upper case and lower case characters in the string (in that order). 

def count_case(sentence):
    upper=0
    lower=0
    for letter in sentence:
        if letter.isupper():
            upper +=1
        if letter.islower():
            lower+=1
    return upper, lower



user_input = input("Enter a string: ")

# Call the function here
upper,lower= count_case(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)