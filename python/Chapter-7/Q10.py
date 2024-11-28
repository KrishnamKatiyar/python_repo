# Q10 - Write a program to print multiplication table of n using for loops in reversed order.

num = int(input("Enter table number : "))

print(f"\nTable of {num} in reverse is :-\n")

for i in range(1,11):
    print(f"{num} * {11-i}  =  {num*(11-i)}")