
class IntList():
    def __init__(self,length):
        self.__length = length
        self.__elements = []
    
    def add(self,element):
        if len(self.__elements) < self.__length:
            self.__elements.append(element)
        return self.__elements

    def __str__(self):
        return str(self.__elements)
    
    def __len__(self):
        return len(self.__elements)
    
    def full(self):
        return len(self.__elements) == self.__length
    
    def __add__(self,other):
        shorter = min(len(self),len(other))
        result = IntList(shorter)
        for i in range(shorter):
            result.add(self.__elements[i] + other.__elements[i])
        return result






list1 = IntList(5)  # Constructs an IntList that can hold 5 integers
list2 = IntList(12) # Constructs and IntList that can hold 12 integers

for i in range(10):
    list1.add(i)
    list2.add(i)

print(list1)
print(list2)

print("Length of list1 is: {}".format(len(list1)))
print("Length of list2 is: {}".format(len(list2)))

if list1.full():
    print("list1 is full")
if list2.full():
    print("list2 is full")

list3 = list1 + list2
print(list3)

list4 = list2 + list1
print(list4)