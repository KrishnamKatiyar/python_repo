# Q4 - Write a program to find whether a given number is prime or not.

n = int(input("Enter the number : "))

for i in range(2,n):
    if(n%i == 0):
        print(f"{n} is not prime")
        break
else:
    print(f"{n} is prime")



#----------------------------------------------------------------

num = int(input("Enter the number : "))

i = 1 
f = 0

while(i<=num):
    if(num%i == 0):
        f += 1
    i+=1

if(f == 2):
    print("PRIME")
else:
    print("NOT PRIME")
    

