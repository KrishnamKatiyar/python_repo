f = open("text.txt")

# line = f.readlines()    # returns the list of all lines
# print(line,type(line))

# line1 = f.readline()
# print(line1, type(line1))
# line2 = f.readline()
# print(line2, type(line2))
# line3 = f.readline()
# print(line3, type(line3))
# line4 = f.readline()
# print(line4, type(line4))

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()