'''
Q4 - A file contains a word "Donkey/' multiple times. You need to write a program which
replace this word with ##### by updating the same file.
'''

word = "Donkey"

with open("./problems/file.txt", "r") as f:
    content = f.read()

newContent = content.replace(word, "######")

with open("./problems/file.txt", "w") as f:
    content = f.write(newContent)