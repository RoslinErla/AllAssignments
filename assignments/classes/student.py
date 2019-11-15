# Implement the class Student.  
# An instance of the class has varaibles for student id (integer) 
# and a list of four float grades. An instance is created like: 

# student1 = Student(1, [3.0, 4.6, 3.4, 5.4])
# When an instance of a student is printed,  the result should be as follows:

# Student ID: 1
# Grades: [3.0, 4.6, 3.4, 5.4]

# It should be possible to compare two students with the < operator.  
# The comparison is based on the average grade of the instances:

# student1 = Student(1, [3.0, 4.6, 3.4, 5.4])
# student2 = Student(2, [9.5, 9.0, 8.9, 9.8])

# if student1 < student2:
#     print("student1 < student2")

class Student:
    def __init__(self,student_id,grade_list):
        self.id = student_id
        self.grades = grade_list
    
    def __str__(self):
        return_string = "Student ID: {}\nGrades: {}".format(self.id, self.grades)
        return return_string
    
    def average(self):
        the_sum = 0
        for elements in self.grades:
            the_sum += float(elements)
        return the_sum / len(self.grades)

    
    def __lt__(self,other):
        return self.average() < other.average()


a = Student(1, [3.0, 4.6, 3.4, 5.4])
b = Student(2, [9.5, 9.0, 8.9, 9.8])
print(a < b)
print(b < a)