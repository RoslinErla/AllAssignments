# Útfærið klasann Bug í skránni bug.py, sem líkir eftir pöddu (e. bug) sem ferðast eftir láréttri línu, annaðhvort til hægri eða vinstri. Upphaflega færist paddan til hægri en hún getur skipt um átt.  Í sérhverri færslu breytist staða pöddunnar um eitt skref í þá átt sem er virk hverju sinni.

# Með því að skoða aðalforritin hér fyrir neðan og úttak þeirra eigið þið að geta áttað ykkur á því hvaða gögn og aðgerðir klasinn Bug þarf að hjúpa.


# from bug import Bug

# print("Bug 1:")
# bug1 = Bug(10)  # creates an instance of a bug whose initial position is at 10
# print(bug1)

# for i in range(1,3):
#     bug1.move()
#     print(bug1)

# bug1.turn()

# for i in range(1,5):
#     bug1.move()
#     print(bug1)

# print("Bug 2:")
# bug2 = Bug(5)   # creates an instance of a bug whose initial position is at 5
# bug2.turn()
# bug2.move()
# print(bug2)

# if bug1 > bug2:
#     print("Bug1 has travelled further than bug2")

# print("Bug 3:")
# # creates an instance of a bug whose initial position is the sum of the position of bug1 and bug2
# bug3 = bug1 + bug2  
# print(bug3)
# bug3.move()
# bug3.move()
# print(bug3)
# if bug3 > bug1:
#     print("Bug3 has travelled further than bug1")
# Úttak aðalforritsins.  Athugið að staða pöddunnar er sýnd með 'b':

# The output of the main program.  Note that the position of the bug is marked with a 'b':

# Bug 1:
# xxxxxxxxxbxxxxxxxxxx
# xxxxxxxxxxbxxxxxxxxx
# xxxxxxxxxxxbxxxxxxxx
# xxxxxxxxxxbxxxxxxxxx
# xxxxxxxxxbxxxxxxxxxx
# xxxxxxxxbxxxxxxxxxxx
# xxxxxxxbxxxxxxxxxxxx
# Bug 2:
# xxxbxxxxxxxxxxxxxxxx
# Bug1 has travelled further than bug2
# Bug 3:
# xxxxxxxxxxxbxxxxxxxx
# xxxxxxxxxxxxxbxxxxxx
# Bug3 has travelled further than bug1
# Ef paddan er þegar á hægri endanum á línunni og reynir að fara til hægri þá breytist staða hennar ekki neitt.  Sama gildir um vinstri endann:

# If the bug is currently at the right end of the horizontal line and tries to move further right, its position will not change.  The same holds for the left end:

# from bug import Bug

# print("Bug 1:")
# bug1 = Bug(18)  # creates an instance of a bug whose initial position is at 18
# print(bug1)

# for i in range(1,5):
#     bug1.move()
#     print(bug1)
# Bug 1:
# xxxxxxxxxxxxxxxxxbxx
# xxxxxxxxxxxxxxxxxxbx
# xxxxxxxxxxxxxxxxxxxb
# xxxxxxxxxxxxxxxxxxxb
# xxxxxxxxxxxxxxxxxxxb
# Sama gildir líka þegar búið er til tilvik af Bug:

# The same holds when creating a bug instance:

# from bug import Bug

# bug1 = Bug(25)
# print(bug1)

# bug2 = Bug(-5)
# print(bug2)
# xxxxxxxxxxxxxxxxxxxb
# bxxxxxxxxxxxxxxxxxxx
START = 1
END = 20
class Bug(object):
    def __init__(self, position):
        """Starts the program of with the position and the direction set to right"""
        self.position = position
        self.direction = "r"
    
    def __str__(self):
        """Checks the position of the bug and prints out the bug marked as "B" """
        if self.position < START: #The bug can never travel farther than the string allows
            self.position = START #If it tries to at the beginnig of the string we hold it at the start
        elif self.position > END: 
            self.position = END # If it tries to at the end of the string we hold it at the end
        empty_string = "" #Start with an empty string 
        for x in range(START, END+1 ):
            if x == self.position: #If the bug is at this location we but a "b" there
                empty_string += "b"
            else:
                empty_string += "x" #else we put an "x"
        return empty_string

    def move(self):
        """Moving the bug either left or right at the string"""
        if self.direction == "r" and self.position < END: #If the position is at the end of the string we dont update the position
            self.position += 1

        elif self.direction == "l" and self.position > START: #If the position is at the start of the string we dont update the position
            self.position -= 1
        else:
            self.position = self.position
        
    def turn(self):
        """If the bug was going right it is now going left"""
        if self.direction =="r":
            self.direction = "l"
        elif self.direction == "l":
            self.direction = "r"

    def __gt__(self,other):
        """Checks if the position of one bug is greater than the location of the other bug"""
        return self.position > other.position
    
    def __add__(self,other):
        """Adds the position of 2 bugs and makes that the position of the 3rd one"""
        self.position = self.position + other.position
        return Bug(self.position)





bug = Bug(6)
print(bug)
bug.move()
print(bug)
bug.turn()
for i in range(0,5):
  bug.move()
  print(bug)
bug.turn()
bug.move()
print(bug)
