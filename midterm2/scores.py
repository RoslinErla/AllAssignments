#Skrifið Python forrit sem les rauntölur frá notanda 
# (með bili á milli talna), fjarlægir tvær minnstu tölurnar 
# og prentar út summu talnanna sem eftir eru. 
# Skrifa skal út villuskilaboð ef fjöldi talna sem sleginn er inn er < 2 
# en ekki þarf að villutékka inntakið að öðru leyti.
#Ábending: Innbyggð föll geta hjálpað!  Þið megið hins vegar ekki nota neina import setningu.
# Example 1:
# Enter scores separated by space: 1.1
# At least two scores needed!
 
# Example 2:
# Enter scores separated by space: 2.3 4.5 1.1 7.8 3.4 5.6
# Sum of scores (two lowest removed): 21.3


def input_from_user():
    scores = input("Enter scores separated by space: ")
    scores = scores.split()
    return scores

def enough_floats(lists):
    counter = 0
    for elements in lists:
        counter += 1
    return counter

def sort_list(lists):
    lists.sort()
    new_list = lists
    return new_list

def remove_minimum(lists):
    lists = list(map(float, lists))
    lists.remove(min(lists))
    lists.remove(min(lists))
    return lists

def sum_of_list(lists):
    the_sum = list(map(float, lists))
    the_sum = sum(the_sum)
    print("Sum of scores (two lowest removed): ", the_sum )

def main():
    scores = input_from_user()
    number_of_floats = enough_floats(scores)
    if number_of_floats < 2:
        print("At least two scores needed! ")
    else:
        sorted_list = sort_list(scores)
        minimum_removed = remove_minimum(sorted_list)
        sum_of_list(minimum_removed)
    

    

main()