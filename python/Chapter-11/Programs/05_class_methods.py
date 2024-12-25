# A class method is a method which is bound to the class and not the object of the class.
# @classmethod decorator is used to create a class method.

class Empolyee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    def show2(cls, instance = None):
        if instance and hasattr(instance, 'a'):
            print(f"The instance attribute of a is {instance.a}")
        else:
            print(f"The class attribute of a is {cls.a}")

ob = Empolyee()
ob.a = 43
ob.show()
ob.show2()