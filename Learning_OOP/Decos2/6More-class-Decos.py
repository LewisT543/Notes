# Quick Syntax reminder!

'''
@my_decorator
class MyClass:
    pass
obj = MyClass()

#########

def my_decorator(A):
    pass
class MyClass:
    pass
MyClass = my_decorator(MyClass())
obj = MyClass()
'''

# This is some confusing ass shit because __getattribute__ and __getattr__ are different special methods.
def object_counter(class_):
    class_.__getattr__orig = class_.__getattribute__

    def new_getattr(self, name):
        if name == 'mileage':
            print('Mileage has been read!')
        return class_.__getattr__orig(self, name)

    class_.__getattribute__ = new_getattr
    return class_

# Simple car class, un-decorated so far.
    # ...now with a decorator
@object_counter
class Car:
    def __init__(self, VIN):
        self.mileage = 0
        self.VIN = VIN

car = Car('ABC123')
print(f'The Mileage is {car.mileage}')
print(f'VIN : {car.VIN}')

# class_ is just class but with an underscore to avoid naming conflicts with pythons built in class keyword
# Add an _ after a word to prevent naming conflict
    # chicken = 1
    # chicken_ = 2
    # print(chicken, chicken_)
    #Output:
        # (1, 2)