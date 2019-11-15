#Einstein's famous equation states that the energy in an object at rest equals its mass times the square of the speed of light.  (The speed of light is 300,000,000 m/s.)

#Complete the skeleton code below so that it:
#* Accepts the mass of an object (remember to convert the input string to a number, in this case, a float).
#* Calculate the energy, e
#* Prints e

m = float(input("Enter the mass of an object: "))
c = 300000000
e= m*(c**2)
print("e=" ,e)
#e=m*c**2
