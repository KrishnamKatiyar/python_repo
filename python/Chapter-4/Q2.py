# Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

s1 = int(input("Enter marks of subject 1 : "))
s2 = int(input("Enter marks of subject 2 : "))
s3 = int(input("Enter marks of subject 3 : "))
s4 = int(input("Enter marks of subject 4 : "))
s5 = int(input("Enter marks of subject 5 : "))

marks.append(s1)
marks.append(s2)
marks.append(s3)
marks.append(s4)
marks.append(s5)

t_marks = tuple(marks)

print(sorted(t_marks))

