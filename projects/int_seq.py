summa= 0
odd= 0
even= 0
num = int(input("Enter an integer: "))
max_value= 0

while num > 0:
    if num%2== 1:
        odd +=1
    elif num%2==0:
        even +=1
    summa += num
    if max_value < num:
        max_value = num
    print ("Cumulative total:", summa)   
    num = int(input("Enter an integer: "))
    if num <= 0:
        print ("Largest number:",max_value)
        print ("Count of even numbers:",even)
        print ("Count of odd numbers:",odd)
