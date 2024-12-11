class Employee:
    language = "py"   
    salary = 120000       # class attributes


krish = Employee()
krish.name = "Krish"  # object attribute or instance attribute
krish.salary = 0      # instance attribute takes preferece over class attribute
print(krish.name, krish.salary, krish.language) 