weight_str = input("Weight (kg): ") # do not change this line
height_str = input("Height (cm): ") # do not change this line
weight = float(weight_str)
height = float(height_str)
height1= height / 100
bmi= (weight / height1**2) 
print("BMI is: ", bmi) # do not change this line
