# Implement the class WholeNumber.  
# The whole numbers are the nonnegative integers 0,1,2,...  
# The class must handle addition, subtraction, and multiplication of whole numbers, 
# as well as printing. 

# The class should have one instance variable, __num.  
# The constructor should accept one whole number parameter (with default value 0). 
# If something other than a whole number is passed to the constructor, 
# the __num instance variable should be set to None.

# All operations on an illegal whole number should be handled and result in None.

# Example run:


class WholeNumber:
    def __init__(self,number = 0):
        if type(number) == int and number >= 0: 
            self.__num = number
        else: 
            self.__num = None

    def __str__(self):
            return str(self.__num)

    def __add__(self,other):
        try: 
            return self.__num + other.__num
        except:
            return None

    def __sub__(self,other):
        try:
            sub = self.__num - other.__num
            if sub > 0:
                return sub
            else:
                return None
        except:
            return None

    def __mul__(self,other):
        try:
            return self.__num * other.__num
        except:
            return None


num1 = WholeNumber("bla")


