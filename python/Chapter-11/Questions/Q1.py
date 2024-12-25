# Q1 . Create a class (2-D vector) and use It to create another class representing a 3-D vector.

class two_D_Vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vertor is {self.i}i + {self.j}j")

class three_D_Vector(two_D_Vector):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The vertor is {self.i}i + {self.j}j + {self.k}k")


ob1 = two_D_Vector(1,2)
ob1.show()

ob2 = three_D_Vector(1,2,3)
ob2.show()
