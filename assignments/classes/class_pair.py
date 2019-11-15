# Write a class 'Pair' that initializes two values 'v1' and 'v2' to '0' by default. It should print the values in this form: "Value 1: 20, Value 2: 30". When two objects of this class are added together using the '+' operator, the result is 'v1' of object 1 gets added to 'v1' of object 2 and 'v2' of object 1 gets added to 'v2' of object 2.

# For example:

# a = Pair(20,30)
# print(a)
# Value 1: 20, Value 2: 30
# b = Pair(40,50)
# c = a + b
# print(c)
# Value 1: 60, Value 2: 80

class Pair():
    def __init__(self, value1 = 0, value2 = 0):
        self.__value1 = value1
        self.__value2 = value2
    
    def __str__(self):
        return "Value 1: {}, Value 2: {}".format(self.__value1, self.__value2)

    def __add__(self, other):
        self.__value1 += other.__value1
        self.__value2 += other.__value2
        return self

a = Pair()
print(a)
b = Pair(40,50)
c = a+b
print(c)