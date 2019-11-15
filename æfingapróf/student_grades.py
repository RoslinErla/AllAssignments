# Skrifið Python forrit sem heldur utan um einkunnir fjögurra nemanda.
# Hver nemandi á einkvæmt nafn (þ.e enginn nemandi heitir það sama) og 3 einkunnir.
 
# Write a Python program that manages grades for four students. 
# Each student has a unique name and 3 grades.
 
# Notandi á að geta slegið inn nöfn allra nemandanna sem og einkunnir hvers og eins nemanda.
# Forritið skal prenta út nöfn allra nemanda í stafsrófsröð og einkunnir þeirra.
# Að lokum prentar forritið út nafn nemandans með hæstu meðaleinkunnina ásamt meðaleinkunninni hans. Meðaleinkunnin skal vera prentuð út með tveimur aukastöfum.
 
# The user should be able to input the name of each student and the corresponding grades for each student.
# The program prints the names of each student in alphabetical order along with their grades.
# Finally, the program prints the name of the student with the highest average grade along with the student's average grade. The average grade should be printed with 2 digits after the decimal point.
 
# Ef að tveir eða fleiri nemendur eru með sömu meðaleinkunnina skal birta þann nemanda sem kemur fyrir fyrstur í stafrófinu.
# If two or more students have the same average grade the student that appears first in the alphabetical order should be printed.
import operator

STUDENTS = 4
GRADES = 3

def make_student_dict(a_dict):
    grade_list= list()

    for i in range(STUDENTS):
        name = input("Student name: ")

        for i in range(1, GRADES+1):
            grades = input("Input grade number" +" " + str(i) + ": ")
            grade_list.append(float(grades))
        a_dict[name] = grade_list
        grade_list = list()

    return a_dict

def print_dict(a_dict):
    new_dict = sorted(a_dict.items(), key=operator.itemgetter(0))
    print("Student list:")
    for tuples in new_dict:
        print(tuples[0], ":",tuples[1])

def find_average(a_dict):
    for keys in a_dict:
        ave = 0
        for elements in a_dict[keys]:
            ave += elements
            average = ave / GRADES
            a_dict[keys] = average
    return a_dict

def print_highest_ave (a_dict):
    new_dict = sorted(a_dict.items(), key=operator.itemgetter(1),reverse=True)
    print("Student with highest average grade:")
    key_list = list()
    for keys in new_dict:
        key_list.append(keys[0])
    key = key_list[0]
    print(key,"has an average grade of {:.2f}".format(a_dict[key]))


def main():
    student_dict = dict()
    make_student_dict(student_dict)
    print_dict(student_dict)
    find_average(student_dict)
    print_highest_ave(student_dict)


main()
