class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3


ob1 = Employee()
print(ob1.a)

ob2 = Programmer()
print(ob2.a, ob2.b)

ob3 = Manager()
print(ob3.a, ob3.b, ob3.c)

