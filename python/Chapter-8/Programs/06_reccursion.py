'''
Definition
Recursion occurs when a function calls itself directly or indirectly. 
It is used to solve problems that can be divided into smaller, similar subproblems.

Structure of a Recursive Function - 
-> Base Case: Stops the recursion.
-> Recursive Case: Function calls itself with a smaller input.
'''

def factorial(n):
    if(n==0 or n==1):     # base case
        return 1
    return n * factorial(n-1)     # function is calling itself here

num = int(input("Enter any number : "))
print(f"Factorial of given number is {factorial(num)}")



def fibonacci(n):
    if n <= 1:  # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Print the first 5 Fibonacci numbers

for i in range(5):
    print(fibonacci(i), end=" ")  # Output: 0 1 1 2 3
