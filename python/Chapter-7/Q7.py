'''
Q7 - Write a program to print the following star pattern.


  *
 ***
*****

for n = 3


'''

# Number of rows
n = int(input("Enter any number : "))

# Loop through each row
for i in range(1, n + 1):
    # Print spaces
    print(" " * (n - i), end="")
    # Print stars
    print("*" * (2 * i - 1))


