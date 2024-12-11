# Q4 - Write a recursive function to calculate the sum of first n natural numbers.

def sum_all(num):
    sum = 0
    if(num == 1):
        return 1
    return sum_all(num - 1) + num

print(sum_all(4))