# Q8 - If languages of two friends are same; what will happen to the program in Q6

'''
Q6 - Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.
'''

d = {}

name = input("Enter your name : ")
lang = input("Enter your favourite language : ")
d.update({name : lang}) 

name = input("Enter your name : ")
lang = input("Enter your favourite language : ")
d.update({name : lang})

name = input("Enter your name : ")
lang = input("Enter your favourite language : ")
d.update({name : lang})

name = input("Enter your name : ")
lang = input("Enter your favourite language : ")
d.update({name : lang})

print(d)

# dictionary can have same values but not same keys so even if language is same, there will not be any problem