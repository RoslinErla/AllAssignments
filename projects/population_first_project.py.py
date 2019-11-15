USA_population = int(307357870)
years_str= input("Years: ")
years= int(years_str)

#Finding seconds in a year by taking the amount of days multiplied by the amount of hours in a day, minutes in an hour and seconds in a minute and then the amount of years that was input
seconds =365*24*60*60*years

#If a person is born every 7 seconds then you get the amount of births by dividing the amount of seconds by 7
births = seconds / 7

#if there is a new immigrant every 35 seconds then you find out how many immigrants there are in x years by dividing the seconds  by 35
immigrants= seconds / 35


#If a person dies every 13 secs then you find out how many people died by dividing the amounts of seconds by 13
deaths= seconds / 13

if years < 0:
    print(" Invalid input!")
else:
    population =  USA_population + births+immigrants-deaths
    population = int(population)
    print(" New population after", years, "years is", population)