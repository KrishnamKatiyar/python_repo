class Employee:   # Base class
    company = "ITC"
    name = "default_name"
    salary = 0
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}.")

class Coder:
    lang = "Python"
    def printLang(self):
        print(f"Out of all languages, yours is {self.lang}")

class Programmer(Employee, Coder):  # Derived or child class
    company = "ITC Infotech"
    def showLang(self):
        print(f"The name is {self.name} and he is good in {self.lang} language.")

b = Programmer()

print(b.company)
print(b.show())