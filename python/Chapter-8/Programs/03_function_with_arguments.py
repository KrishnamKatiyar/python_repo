def greeting(name):              # argument name is passed in the definition
    print(f"Good day, {name}")


greeting("Krishnam")             # name is given when calling the function
greeting("Kartikay") 


def greeting_2(name,ending):              # now 2 arguments name and ending should be passed
    print(f"Good day, {name}")
    print(ending)

greeting_2("Krishnam","Thankyou")        # these 2 arguments are provided during function calling in order
greeting_2("Kartikay","Thanks")