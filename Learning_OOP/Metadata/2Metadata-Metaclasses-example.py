
# My_Meta is derived from type, thus it is a Metaclass
class My_Meta(type):
    # We define our own __new__() method, its role is to call the __new__ method of the parent class to create a new class
    def __new__(mcs, name, bases, dictionary):
        # __new__ uses mcs to refer to class, just a convention
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.custom_attribute = 'Added by My_Meta'
        return obj

class My_Object(metaclass=My_Meta):
    pass

print(My_Object.__dict__)

# output:
# {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'My_Object' objects>, 
# '__weakref__': <attribute '__weakref__' of 'My_Object' objects>, '__doc__': None, 
# 'custom_attribute': 'Added by My_Meta'} <<<< Our custom attribute has been added to the object!

print('\n\n\n')
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# This example code will equip a class with the greetings() method if it is missing one.

def greetings(self):
    print('Just a greeting function, but it could be something more serious like a check sum')

class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):

        # This if statement checks the attribute dict for greetings, adding it if not present
        if 'greetings' not in dictionary:
            dictionary['greetings'] = greetings 

        obj = super().__new__(mcs, name, bases, dictionary)
        return obj

class My_Class1(metaclass=My_Meta):
    pass

class My_Class2(metaclass=My_Meta):
    def greetings(self):
        print('We are ready to greet you!')

myobj1 = My_Class1()
myobj1.greetings()
myobj2 = My_Class2()
myobj2.greetings()

# output:
# Just a greeting function, but it could be something more serious like a check sum
# We are ready to greet you!

# 