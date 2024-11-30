'''
A function is a block of reusable code that performs a specific task. 
Functions help reduce code redundancy and make programs easier to maintain and debug

Defining a Function - 

def function_name(parameters):
    """
    Optional docstring to describe the function.
    """
    # Function body
    return value  # Optional return statement

Calling a Function - 

function_name(arguments)


'''


a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
c = int(input("Enter the number : "))

avg = (a+b+c)/3
print(avg)

d = int(input("Enter the number : "))
e = int(input("Enter the number : "))
f = int(input("Enter the number : "))

avg = (d+e+f)/3
print(avg)

#-----------------------------------------------

def avg():                                       # defining the function named avg
    a = int(input("Enter the number : "))
    b = int(input("Enter the number : "))
    c = int(input("Enter the number : "))

    avg = (a+b+c)/3
    print(avg)

avg()                                            # calling the function named avg
avg()


'''
There are two types of functions in python:
    • Built in functions (Already present in python)
    • User defined functions (Defined by the user)

Examples of built in functions includes len(), print(), range() etc.

The avg function we defined is an example of user defined function.
'''

