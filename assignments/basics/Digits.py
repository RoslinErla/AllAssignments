#Input a six-digit integer.
# Assign first_three (int) to be the first three digits.
# Assign last_two (int) to be the last two digits.
# Assign middle_two (int) to be the middle two digits.
# Print out the three values.
# Hint: use quotient (//) and remainder (%)
# For example, if the input is 123456
# The first three digits: 123
# The last two digits: 56
# The middle two digits: 34

x= int(input("Enter an 6 digit number: "))
first_three = x // 1000
last_two = x % 100
middle_two = x//100%100

print(first_three)
print (last_two)
print(middle_two)