# Q11 - Write a python program to rename a file to "renamed_by_ python.txt".

with open("./problems/old.txt") as f:
    content = f.read()

with open("./problems/renamed_by_ python.txt", "w") as f:
    f.write(content)