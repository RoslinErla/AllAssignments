# Your task is to implement a payroll proessing system for different kinds of employees.
# Salaries are paid weekly.

# Hourly employees get paid an hourly rate, 
# but if they work more than 40 hours per week, 
# the get paid 1.5 times the hourly rate for the excess.

# Salaried employees get paid according to their annual salary, 
# no matter how many hours they work.  You can assume 52 weeks in a year.
# Managers are salaried employees who get paid a salary and a weekly bonus.
# By studying the following main program, 
# you should be able to figure out which classes and attributes you need.'

# Hint: You should have one class, Employee, that expresses the commonality among the other classes.

# from employee import HourlyEmployee, SalariedEmployee, Manager

# def print_salaries(staff):
#     for employee in staff:
#         name = employee.get_name()
#         hours = int(input("Hours worked by " + name + ": "))
#         pay = employee.weekly_pay(hours)
#         print("{}: {:.2f}".format(name, pay))

# # The main program starts here
# staff = []
# staff.append(HourlyEmployee("Harry Morgan", 30.0))  # 30.0 is the hourly wage
# staff.append(SalariedEmployee("Sally Lin", 52000.0)) # 52000 is the annual salary
# staff.append(Manager("Mary Smith", 104000.0, 50.0))  # 104000 is the annual salary, 50.0 is the weekly bonus
# print_salaries(staff)
# Output:

# Hours worked by Harry Morgan: 45
# Harry Morgan: 1425.00
# Hours worked by Sally Lin: 40
# Sally Lin: 1000.00
# Hours worked by Mary Smith: 50
# Mary Smith: 2050.00

class Employee():
    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name


class HourlyEmployee(Employee):
    def __init__(self,name,wage):
        Employee.__init__(self,name)
        self.wage = wage

    def weekly_pay(self,hours):
        paid = self.wage * 40
        paid += (self.wage * 1.5) * (hours - 40)
        return paid



class SalariedEmployee(Employee):
    def __init__(self,name,salary):
        Employee.__init__(self,name)
        self.salary = salary
    
    def weekly_pay(self,salary):
        paid = self.salary / 52
        return paid

class Manager(Employee):
    def __init__(self,name,salary,bonus):
        Employee.__init__(self,name)
        self.bonus = bonus
        self.salary = salary
    
    def weekly_pay(self,salary):
        paid = (self.salary / 52) + self.bonus
        return paid

emp3 = Manager("Mary Smith", 91000.0, 60.0)
print(emp3.weekly_pay(60))