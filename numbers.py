first_digit=0
second_digit=0 
number_of_divisors=0

for i in range(10,100):
    first_digit = i//10
    second_digit = i%10
    if (first_digit + second_digit)**2 == i:
        print(i)

for i in range (1,100):
    number_of_divisors=0
    for j in range(1,i+1):
        if i % j == 0:
            number_of_divisors +=1
    if number_of_divisors == 10:
        print (i)
