age = int(input("Enter your age : "))

# if statemnt 1
if(age%2 == 0):
    print("age is even")

# end of if statement 1


# if satement 2
if(age>=18):
    print("you are above the age of consent")
    print("good for you")

elif(age==0):
    print("you're entering 0 which is not a valid age")

elif(age<0):
    print("you are entering an invalid age")

else:
    print("you are below the age of consent")

# end of if statement 2

print("end of program")