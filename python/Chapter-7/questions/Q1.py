# Q1 - Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter table number : "))

print(f"\nTable of {num} is :-\n")

for i in range(1,11):
    print(f"{num} * {i}  =  {(num*i)}")