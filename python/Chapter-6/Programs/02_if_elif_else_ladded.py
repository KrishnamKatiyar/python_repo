age = int(input("Enter your age : "))

if(age>=18):
    print("you are above the age of consent")
    print("good for you")

elif(age==0):
    print("you're entering 0 which is not a valid age")

elif(age<0):
    print("you are entering an invalid age")

else:
    print("you are below the age of consent")

print("end of program")


'''
There can be any number of elif statements.
Last else is executed only if all the conditions inside elifs fail.
'''