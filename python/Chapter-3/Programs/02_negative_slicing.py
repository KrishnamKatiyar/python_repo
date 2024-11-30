name = "krishnam"


print(len(name))

print(name[:7])  # is same as [0:7]
print(name[:])   # is same as [0:len(name)]


"""
    0  1  2  3  4  5  6  7
    k  r  i  s  h  n  a  m ----
   -8 -7 -6 -5 -4 -3 -2 -1
"""


print(name[-5:-1])  # is same as [3:7]
print(name[3:7])

print(name[-8:])