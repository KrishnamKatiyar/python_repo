# Q4 - Add a static method in problem 2, to greet the user with hello.

class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square of the number is {self.n * self.n}")

    def cube(self):
        print(f"Cube of the number is {self.n * self.n * self.n}")

    def squareRoot(self):
        print(f"Square root of the number is {self.n ** 1/2}")

    @staticmethod
    def greet():
        print("Hello there!")


num = calculator(4)
num.greet()
num.square()
num.cube()
num.squareRoot()