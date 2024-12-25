class Employee:   # Base class
    company = "ITC"
    name = "default_name"
    salary = 0
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}.")

# class Programmer:
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLang(self):
#         print(f"The name is {self.name} and he is good in {self.lang} language.")

class Programmer(Employee):  # Derived or child class
    company = "ITC Infotech"
    def showLang(self):
        print(f"The name is {self.name} and he is good in {self.lang} language.")

a = Employee()
b = Programmer()

print(a.company, b.company)