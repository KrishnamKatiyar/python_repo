# Write a program to store seven fruits in a list entered by the user.

fruits = []

f1 = input("Enter fruit 1 : ")
f2 = input("Enter fruit 2 : ")
f3 = input("Enter fruit 3 : ")
f4 = input("Enter fruit 4 : ")
f5 = input("Enter fruit 5 : ")
f6 = input("Enter fruit 6 : ")
f7 = input("Enter fruit 7 : ")

fruits.append(f1)
fruits.append(f2)
fruits.append(f3)
fruits.append(f4)
fruits.append(f5)
fruits.append(f6)
fruits.append(f7)

print(fruits)
print(type(fruits))

n_fruits = tuple(fruits)
print(n_fruits)
print(type(n_fruits))