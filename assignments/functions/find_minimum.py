
# Find minimum
# Write a function named find_min that takes two numbers as arguments and returns the minimum of the two.
# Also write a statement that calls the function using the given input as arguments.
# find_min function definition goes here
def find_min(num1,num2):
    if num1 <= num2:
        result = num1
    else:
        result =num2
    return result 


first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
# Call the function here
minimum = find_min(first,second)
print("Minimum: ", minimum)