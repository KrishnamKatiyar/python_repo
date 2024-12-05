# Q8 - Write a program to make a copy of a text file "this. txt"

with open("./problems/this.txt") as f:
    content = f.read()

with open("./problems/this_copy.txt", "w") as f:
    f.write(content)

