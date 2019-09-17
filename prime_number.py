# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
# Write a function named is_prime that takes an integer argument and returns True if the number is prime and False otherwise. (Assume that the argument is an integer greater than 1, i.e. no need to check for erroneous input.)
# Also write code that calls the function and prints out a message saying that the given number is a prime or not.
# Example input/output:
# Input an integer greater than 1: 7
# 7 is a prime
# Input an integer greater than 1: 6
# 6 is not a prime

def is_prime(number):
    prime=True
    count=2
    while count < number:
        if number%count == 0:
            prime = False
        count +=1   
    if prime==True:
        result= "is a prime"
    else: 
        result= "is not a prime"
    return result


num = int(input("Input an integer greater than 1: "))
is_it_prime = is_prime(num)

print(num,is_it_prime)

