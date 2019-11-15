# A prime number is a whole number greater than 1 whose only factors are 1 and itself.

# Write a program using a while statement,
#  that given an int as the input, prints out "Prime" if the int is a prime number, 
# otherwise it prints "Not prime".

n = int(input("Input a natural number: ")) # Do not change this line
count = 2
prime = True
# Fill in the missing code below
while count < n:
    
    if n%count == 0:
        prime = False
     
    count +=1   

# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("Not prime")