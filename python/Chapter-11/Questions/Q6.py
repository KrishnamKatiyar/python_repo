'''
Q6 - Write str () method to print the vector as follows:
                    7i + 8i +10k
Assume vector of dimension 3 for this problem.
'''

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    

v1 = Vector(1,2,3)
v2 = Vector(4,5,6)

print(v1 + v2)
print(v1 * v2)