# Write a function that takes an integer as an argument and returns True if the number is within the range 1 to 555
#  (not inclusive, i.e. neither 1 nor 555 are in range).
# Also write a statement that calls the function with the given input as an argument.
num = int(input("Enter a number: "))

# You call the function here
def range(number):
    if number <= 1 or number>=555:
        result= print(number, "is outside the range! ")
    else:
        result =print(number, "is in range.")

range= range(num)
