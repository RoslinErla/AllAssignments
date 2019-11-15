# Write a class MyString() 
# such that it has a method that gives the difference between the size of strings when the '-' 
# (subtraction) operator is used between the two objects of the class 
# (the difference should always be positive). 
# Additionally, implement a method that returns True if object 1 is greater than object 2 
# and False otherwise when the (>) (greater than) operator is used. 
# Object 1 is greater than object 2 if the string it stores 
# is longer than the string stored in object 2.

# For example:

# obj1 = MyString('this is a string')
# obj2 = MyString('this is another one')
# print(obj1 > obj2)
# False
# print(obj1-obj2)
# 3
 

# You should only hand in the class code.

class MyString():
    def __init__(self,a_string):
        self.string = a_string


    def __gt__(self,other):
        return len(self.string) > len(other.string)

    def __sub__(self, other):
        return abs((len(self.string) - (len(other.string))))

obj1 = MyString('enbody')
obj2 = MyString('alireza')
print(obj1>obj2) 
assert str(obj1>obj2) 
