# ATH það má ekki nota innbyggða Set klasann í þessu dæmi


# Skrifið klasann StringSet sem heldur utan um mengi af strengjum 
# (mengi geymir aðeins eitt tilvik af sérhverju staki).  
# Þessi útgáfa af mengi viðheldur röð, þ.e. hægt er að vísa í stök þess með "index". 
# Aðalforrit sem prófar klasann er gefið. 

# Aðalforritið byrjar á því að búa til tvö strengjamengi og skrifa þau út ásamt stærð þeirra. 
#  Forritið býr síðan til sammengi mengjanna tveggja og skrifar það út. 
# Síðan býr forritið til mengi úr fyrirspurn skrifar það út ásamt stærð þess.
#  Að lokum skrifar forritið út fjölda orða í fyrirspurninni ásamt hversu mörg þeirra koma fyrir í sammenginu. 

 
# Example main program:


# Example input/output:

# Set1: chocolate ice cream and candy bars are my favorite
# Set2: I like to eat broccoli and fish ice cream brussel sprouts
# Set1 size: 9
# Set2 size: 11
# Union: chocolate ice cream and candy bars are my favorite I like to eat broccoli fish brussel sprouts
# Union size: 17
# Query: chocolate cream fish good rubbish
# Query size: 5
# Found in union: 3
# Með því að skoða aðalforritið og úttak þess eigið þið að geta áttað ykkur á því 
# hvaða meðlimaföll þið þurfið að útfæra. 
#  Klasinn skal einungis hafa eina tilvikabreytu (private), self.__words, sem er listi af orðum.
class StringSet():
    def __init__(self,string):
        self.__words = string.split()
    
    def __str__(self):
        return_str = " ".join(self.make_set())
        return return_str
    
    def make_set (self):
        word_set = list()
        for element in self.__words:
            if element not in word_set:
                word_set.append(element)
        return word_set
    
    def size(self):
        self.__words = self.make_set()
        return len(self.__words)
    
    def __add__(self,other):
        union_set = list()
        for element in self.__words:
            if element not in union_set:
                union_set.append(element)
        for element in other.__words:
            if element not in union_set:
                union_set.append(element)
        return StringSet(" ".join(union_set))

    def at(self,index):
        return self.__words[index]

    def find(self, element):
        return element in self.__words
    

def main():
    set1 = StringSet('word1 word2 word3 word2 word1 word4')
    set2 = StringSet('word2 word5 word4 word6 word7 word3')
    set3 = set1 + set2
    print(set3)

main()