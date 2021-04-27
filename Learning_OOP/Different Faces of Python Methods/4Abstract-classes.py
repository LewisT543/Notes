                                #### ABSTRACT CLASSES ####

# Abstract classes act as a blueprint from which other classes can be created.
# Abstract Methods are methods applied to the abstract class and inherited by subclasses.
# !!! All of the abstract methods in the abstract class MUST BE OVERRIDEN by a subclass BEFORE the subclass can be instantiated.

import abc

class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass


class GreenField(BluePrint):
    def hello(self):
        print('Welcome to Greenfield')


gf=GreenField()
gf.hello()

# bp = BluePrint()
# This will not work as python cannot instantiate abstract classes. Running it will raise a type-error 
# as it contains an @abstractmethod decorator. 

#><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><#

class RedField(BluePrint):
    def yellow(self):
        pass

# rf = RedField()
# We cannot instantiate RedField class as it has no 'hello()' method. And as we know, EVERY abstract 
# method MUST be OVERWRITTEN. 

class PurpleField(RedField):
    def hello(self):
        print('Hi from Purplefield.')

# However, we can then let PurpleField inherit the RedField class. Running this will work as RedField has inherited the
# abstract label from BluePrint. And then PurpleField finally overrides RedField and BluePrint 'Hello()' methods.

pf = PurpleField()
pf.hello() 