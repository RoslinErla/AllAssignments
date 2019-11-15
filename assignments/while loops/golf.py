#In golf, pars for a hole range from 3 to 5.  Write a program using a while statement that allows the user to input the par and the score for each of the 18 holes.  Based on the number of shots compared to par, the program writes out the following:

#"invalid score", for less than 3 under par
#"albatross", for 3 under par
#"eagle", for 2 under par
#"birdie", for 1 under par
#"par", for par (neutral e.g. 4 on a par 4 hole)
#"bogey", for 1 over par
#"double bogey", for 2 over par
#"triple bogey", for 3 over par
#"bad hole", for scores more than 3 over par
#The input/output should look like this:
#Par of hole 1: 5
#Score on hole 1: 6
#bogey
#Par of hole 2: 4
#Score on hole 2: 4
#par
#Par of hole 3: 3
#Score on hole 3: 5
#double bogey
#Par of hole 4: 4
#Score on hole 4: 3
#birdie


hole = 1
while hole <= 18:
    par= int(input("Par of hole "+str(hole)+": "))
    score = int(input("Score on hole "+str(hole)+": "))
    if score - par < -3:
        print ("invalid score")
    elif score - par == -3:
        print ("albatross")
    elif score - par == -2:
        print ("eagle")
    elif score - par == -1:
        print ("birdie")
    elif score - par == 1:
        print ("bogey")
    elif score - par == 2:
        print ("double bogey")
    elif score - par == 3:
        print ("triple bogey")
    elif score - par == 0:
        print ("par")
    else:
        print ("bad hole")
    hole +=1