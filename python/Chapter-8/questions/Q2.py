# Q2 - Write a python program using function to convert Celsius to Fahrenheit

def celToFahren(c):
    f = (c * (9/5)) + 32
    return f

celsius = float(input("Enter temperature in celsius : "))

print(f"Temperature in Fahrenheit will be {round(celToFahren(celsius) , 2)}")

