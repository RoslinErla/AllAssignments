# Implement the class Dice.  
# You should be able to find out which variables and methods 
# Dice needs by inspecting the following main program and its output.

# def run_dice_experiment():
#     dice1 = Dice(6)
#     dice2 = Dice(6)
#     for _ in range(0,10):
#         dice1.roll()
#         dice2.roll()
#         sum_dice = dice1 + dice2
#         print("dice1: {}, dice2: {}, sum dice: {}".format(str(dice1), str(dice2), str(sum_dice)))
#         sum_dice.roll()
#         print("sum dice: {}".format(str(sum_dice)))

# # Main program starts here
# seed_number = int(input("Enter a seed: "))
# random.seed(seed_number)
# run_dice_experiment()
# Input/output:

# Enter a seed: 11
# dice1: 4, dice2: 5, sum dice: 9
# sum dice: 8
# dice1: 4, dice2: 5, sum dice: 9
# sum dice: 10
# dice1: 2, dice2: 2, sum dice: 4
# sum dice: 9
# dice1: 4, dice2: 6, sum dice: 10
# sum dice: 10
# dice1: 2, dice2: 1, sum dice: 3
# sum dice: 8
# dice1: 3, dice2: 2, sum dice: 5
# sum dice: 2
# dice1: 5, dice2: 6, sum dice: 11
# sum dice: 11
# dice1: 1, dice2: 5, sum dice: 6
# sum dice: 7
# dice1: 4, dice2: 6, sum dice: 10
# sum dice: 12
# dice1: 5, dice2: 6, sum dice: 11
# sum dice: 3
# You need to submit the main program as well as your Dice class in Mimir. 

import random
class Dice():
    def __init__(self,sides):
        self.sides = sides
        self.random = 0

    def roll(self):
        self.random = random.randint(1,self.sides)

    def __add__(self,other):
        new_dice = Dice(self.sides + other.sides)
        new_dice.random = self.random + other.random
        return new_dice
    
    def __str__(self):
        return str(self.random)


def run_dice_experiment():
    dice1 = Dice(6)
    dice2 = Dice(6)
    for _ in range(0,10):
        dice1.roll()
        dice2.roll()
        sum_dice = dice1 + dice2
        print("dice1: {}, dice2: {}, sum dice: {}".format(str(dice1), str(dice2), str(sum_dice)))
        sum_dice.roll()
        print("sum dice: {}".format(str(sum_dice)))

# Main program starts here
seed_number = int(input("Enter a seed: "))
random.seed(seed_number)
run_dice_experiment()