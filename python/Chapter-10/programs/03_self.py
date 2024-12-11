class Employee:
    language = "py"   
    salary = 120000    

    def getInfo(self):
        print(f"Language is {self.language} and salary is {self.salary}")

    def greet(self):
        print("Hello")


krish = Employee()
krish.name = "Krish"  
print(krish.name, krish.salary, krish.language)  

krish.getInfo()
krish.greet()