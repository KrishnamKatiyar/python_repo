class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3


ob1 = Employee()
print(ob1.a)

ob2 = Programmer()
print(ob2.a, ob2.b)

ob3 = Manager()
print(ob3.a, ob3.b, ob3.c)

