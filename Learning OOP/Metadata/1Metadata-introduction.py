                                #### METAPROGRAMMING ####

# Metaprogramming is a technique in which a computer programs have the ability to modify their own code
# For python, code modification can occur during its execution. 
# Some examples of this are:
    # Implementing decorators
    # overriding operators
    # implementing the 'properties' protocol

# Another example of metaprogramming is the idea of...

    # METACLASSES
# In python, metaclasses are classes whos instances are also classes.
# Just as a regular class defines the behaviour of certain objects, a metaclass allows for customisation
# of class instantiation.
# The functionality of the metaclass partly coincides with that of class decorators, but metaclasses act in a 
# different way to decorators:
    # Decorators, bind the names of decorated function or classes to new callable objects. Class decorators are applied when
    # classes are instantiated
    # Metaclasses redirect the class instantiation to dedicated logic, contained in the metaclassws. Metaclasses are applied when class
    # definitions are read to create classes long before classes are instantiated.

# Use cases:
    # logging
    # registering classes at creation time
    # interface checking
    # automatically adding new methods
    # automatically adding new variables

# Example:

class Dog:
    pass

age = 10
codes = [33, 92]
dog = Dog()

print(type(age))
print(type(codes))
print(type(dog))
print(type(Dog))

# output:
# <class 'int'>
# <class 'list'>
# <class '__main__.Dog'>
# <class 'type'>

# The output here displays the types of objects.
# <class 'type'> is the odd one out.

for t in (int, list, type):
    print(type(t))

# output:
# <class 'type'>
# <class 'type'>
# <class 'type'>
# <class 'type'>

# This demonstrates what type actually is.
# The hieracrchy is as such:
    # Class object 
    # Class
    # Metaclass
    # type

# 'type' is a class that generates classes defined by a programmer
# metaclasses are subclasses of the 'type' class.

print('\n\n\n')
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

    # SOME SPECIAL ATTRIBUTES

# __name__, inherent for classes; contains the name of the class;
# __class__,inherent for both classes and instances; contains information about the class to which a class instance belongs;
# __bases__, inherent for classes; it’s a tuple and contains information about the base classes of a class;
# __dict__, inherent for both classes and instances; contains a dictionary (or other type mapping object) of the object's attributes.

# Example:

dog = Dog()
print('"dog" is an object of class named:', Dog.__name__)
print()
print('class "Dog" is an instance of:', Dog.__class__)
print('instance "dog" is an instance of:', dog.__class__)
print()
print('class "Dog" is  ', Dog.__bases__)
print()
print('class "Dog" attributes:', Dog.__dict__)
print('object "dog" attributes:', dog.__dict__)

# output:
# "dog" is an object of class named: Dog

# class "Dog" is an instance of: <class 'type'>
# instance "dog" is an instance of: <class '__main__.Dog'>

# class "Dog" is   (<class 'object'>,)

# class "Dog" attributes: {
#     '__module__': '__main__', '__dict__': <attribute '__dict__' of 'Dog' objects>, 
#     '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None
# }
# object "dog" attributes: {}

for element in (1, 'a', True):
    print(element, 'is', element.__class__, type(element))

# output:
# 1 is <class 'int'> <class 'int'>
# a is <class 'str'> <class 'str'>
# True is <class 'bool'> <class 'bool'>

# element.__class__ will return the same information as calling type(element) (ONE ARGUMENT ONLY)
print('\n\n\n')

# When the type() function is called with THREE ARGUMENTS, then it dynamically creates a new class.
    
    # type(, , ) / type(__name__, __bases__, __dict__) >>> type() with three arguments:
# The first argument is the new __name__ attribute
# The second argument is a tuple of classes from which the new class will inherit. This becomes the __bases__ attribute
# The third argument specifies a dictionary containing method definitions and variables for the class body. The elements of this
# argument become the __dict__ attribute and state the classes NAMESPACE.

Dog = type('Dog', (), {})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

# output:
# The class name is: Dog
# The class is an instance of: <class 'type'>
# The class is based on: (<class 'object'>,)
# The class attributes are: {
#     '__module__': '__main__', '__dict__': <attribute '__dict__' of 'Dog' objects>, 
#     '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None
# }

# This example has empty __bases__ and __dict__ arguments. Thus creating a simple class,
# with only a __name__ attribute.



# A More dynamic example:
print('\n\n\n')

def bark(self):
    print('Woof, woof')

class Animal:
    def feed(self):
        print('It is feeding time!')

Dog = type('Dog', (Animal, ), {'age':0, 'bark':bark})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

doggy = Dog()
doggy.feed()
doggy.bark()
