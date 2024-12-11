# Q2 - Write a class "calculator" capable of finding square, cube and square root of a number.

class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square of the number is {self.n * self.n}")

    def cube(self):
        print(f"Cube of the number is {self.n * self.n * self.n}")

    def squareRoot(self):
        print(f"Square root of the number is {self.n ** 1/2}")


num = calculator(4)
num.square()
num.cube()
num.squareRoot()