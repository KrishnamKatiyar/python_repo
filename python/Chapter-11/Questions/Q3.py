'''
Q3 - Create a class 'Employee' and add salary and increment properties to it.
Write a method 'salaryAfterlncrement' method with a @property decorator with a setter
which changes the value of increment based on the salary.
'''

class Employee:
    salary = 100000
    increment = 20

    @property
    def salaryAfterlncrement(self):
        return self.salary + (self.salary * (self.increment/100))

    @salaryAfterlncrement.setter
    def salaryAfterlncrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100

e = Employee()
print(e.salaryAfterlncrement)

e.salaryAfterlncrement = 120000
print(e.increment)