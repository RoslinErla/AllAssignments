import math

class Vector():
    def __init__(self, a_list):
        
        self.__elements = a_list

    def __str__(self):
        return str(self.__elements)

    def __len__(self):
        return len(self.__elements)

    def scaling(self, scalar):
        for i in range(0, len(self)):
            self.__elements[i] = self.__elements[i] * scalar

    def length(self):
        square_sum = 0
        for i in range(len(self)):
            square_sum += self.__elements[i]**2
        return math.sqrt(square_sum)

    def __add__(self,other):
        """Return a new vector which is the result of adding self and other"""



#main program starts here
vec1 = Vector([3,4])
print(vec1)

print(vec1)
print(len(vec1))
print(vec1.length())


vec2 = Vector([1,2,3,4])
print(vec2)
vec2.scaling(3)
print(vec2)
print(len(vec2))

vec3= vec1 + vec2
#vec3 = vec1.__add__(vec2)

class Pet(object):

   def __init__(self, name):
       self.__name = name

   def get_name(self):
       return self.__name

   def __str__(self):
       return "My pet {}".format(self.get_name())


class Dog(Pet):

   def __str__(self):
       return "My dog {}".format(self.get_name())

# Main starts here
d = Dog("Fido")
print(d)
