class Employee:
    language = "py"   
    salary = 120000    

    def __init__(self):   # this is dunder method(those methods who starts with double underscore) which is aumatically called 
        print("I am calling this object")

    def getInfo(self):
        print(f"Language is {self.language} and salary is {self.salary}")

    @staticmethod  
    def greet(): 
        print("Hello")


krish = Employee()
krish.name = "Krish"  
print(krish.name, krish.salary, krish.language)  

krish.getInfo()
krish.greet()