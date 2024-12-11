'''
Q3 - Create a class with a class attribute a; create an object from it and set 'a'
directly using object.a = 0. Does this change the class attribute?
'''

class Q3:
    a = 4

object = Q3()
print(object.a)  # class attr. will be printed bcz instance attr. is not set yet

object.a = 0    # instance attr. is nw set
print(object.a)  

print(Q3.a)  # it will print class attr. a which will not be changed bcs class attr. can't be changed permanently by instance attr.

