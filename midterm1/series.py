first= int(input("First: "))
step= int(input("Step: "))

sum_of_series=0

while sum_of_series < 100:
    print(first, end= " ")
    sum_of_series += first
    first += step

print()
print(sum_of_series)

