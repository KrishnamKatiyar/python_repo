f = open("text.txt")
print(f.read())
f.close()

# same can be written as : 

with open("text.txt") as f:
    print(f.read())

# now you don't have to close the file explicitly