# Q1 - Create a Class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

krish = Programmer("Krishh", 120000, 200333)
print(krish.name, krish.salary, krish.company, krish.pincode)
harry = Programmer("Harry", 150000, 105369)
print(harry.name, harry.salary, harry.company, harry.pincode)