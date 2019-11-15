# Write a function named safe_input(prompt, a_type) 
# that works like the Python input function, 
# except that it only accepts the specified type of input. 
#  The function accepts two arguments:
# prompt: of type string
# a_type: either the type int, float or str
# The function should keep prompting the user for input until the user inputs the correct type. 
#  At the end, the function should return the converted value.


# Here is the definition of safe_input. It should contain this exception:
def safe_input(prompt, a_type):
    while True: 
        try:
            i = a_type(input(prompt))
            return i
        except ValueError:
            print("Error: please enter a value of", a_type)

    
# Do not change the lines below
print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))