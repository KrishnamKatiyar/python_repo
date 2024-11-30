'''
Q9 - Write a program to print the following star pattern.
for n = 3

***
* *
***

'''

# Number of rows
n = int(input("Enter any number : "))

# Loop through each row
for i in range(1, n + 1):
    if i == 1 or i == n:
        # Print a full row of stars for the first and last row
        print("*" * n)
    else:
        # Print a row with stars at the edges and spaces in between
        print("*" + " " * (n - 2) + "*")
