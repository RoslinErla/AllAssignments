n= int(input("Input an int: "))
count= 0

while count <= n:
    count +=1
    if n % count == 0:
        print (count)