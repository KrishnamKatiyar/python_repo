# Q6 - Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter table number : "))

fact = 1

for i in range(1,num+1):
    fact = fact*i             # 5! = 1*2*3*4*5

print(f"Factorial of {num} is {fact}")
