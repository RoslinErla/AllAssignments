# Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …


n = int(input("Enter the length of the sequence: ")) # Do not change this line
first=1
second =2
third =3 


for i in range (n+1):
    if i==0:
        print(1)
    if i==1:
        print(2)
    if i == 3:
        print(3)
    if i > 3:
        fourth= first+second+third
        first=second
        second=third
        third=fourth
        print(fourth)