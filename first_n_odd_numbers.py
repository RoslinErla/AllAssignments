#Write a program using a while statement, that given the number n as input, prints the first n odd numbers starting from 1.

#For example if the input is

#4

#The output will be:

#1
#3
#5
#7
num = int(input("Input an int: ")) # Do not change this line
counter = 0
odd= 1
# Fill in the missing code below
while counter < num:
    print(odd)
    counter += 1
    odd += 2