first= int(input("First: "))
step= int(input("Step: "))
sum_of_series=0

if step == 0:
    while sum_of_series < 100:
        print(first, end= " ")
        sum_of_series += first
        if sum_of_series >=100:
            break
else:
    while sum_of_series < 100:
        for i in range (first , 100, step):
            print(i, end= " ")
            sum_of_series += i
            if sum_of_series >= 100:
                break

print()
print(sum_of_series)

