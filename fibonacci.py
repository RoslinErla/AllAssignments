# The Fibonacci sequence is: 1, 1, 2, 3, 5, 8, 13, ...
# Write a function, fibo, to print the first N numbers of the Fibonacci sequence.  There should be one space between the elements.
# Also write a statement to call fibo.
# Example input/output:
# Input the length of Fibonacci sequence (n>=1): 7
# 1 1 2 3 5 8 13

def fibonacci(number):
    first=1
    second=1
    for num in range (number):
        if num == 0:
            print(first,end=" ")
        if num ==1:
            print(second,end=" ")
        if num >=2:
            third=first+second
            first=second
            second =third
            print(third,end=" ")
n = int(input("Input the length of Fibonacci sequence (n>=1): "))

the_fibonacci_sequence= fibonacci(n)



