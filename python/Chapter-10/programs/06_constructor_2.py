class Employee:
    language = "py"   
    salary = 120000    

    def __init__(self,name,language,salary):
        self.name = name
        self.salary = salary
        self.language = language

        print(f"Language is {self.language} and salary is {self.salary}")

    def getInfo(self):
        print(f"Language is {self.language} and salary is {self.salary}")

    @staticmethod  
    def greet(): 
        print("Hello")


krish = Employee("Krishh","python",-000) 
print(krish.name, krish.salary, krish.language)  

