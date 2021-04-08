                                #### Encapsulation ####

# Encapsulation is used to hide the attributes inside a class, preventing unauthorised parties from having direct access to them.
# To access these attributes we can use methods. These methods may 'get' a value or modify a value in some way.

### @PROPERTY DECORATOR
# Naming conventions! Important!
# the getter method is decorated with '@property'. It designates the name of the attribute to be used by the external code;
# the setter method is decorated with '@name.setter'. The method name should be the attribute name;
# the deleter method is decorated with '@name.deleter'. The method name should should be the attribute name.

class TankError(Exception):
    pass

class Tank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__level = 0

    @property           # <<<<<<<<<<<<<<< Property decorator applies to level() method
    def level(self):      # <<<<<<<<<<<<< CALLED BY anything trying to read __level, eg. print(my_tank.level) will route here.                
        return self.__level # <<<<<<<<<<< This acts as our 'getter' or reader.

    @level.setter       # <<<<<<<<<<<<<<< Decorated with @level.setter. This is our way to modify the 'private' attribute self.__level
    def level(self, amount): # <<<<<<<<<< Notice the method has the SAME NAME! This is fine because python will know which one to call,              
        if amount > 0:                  # based on the @level.setter decorator. 
                                        # CALLED BY anything trying to modify __level, eg. my_tank.level += 1 will route here.                        
            # fueling
            if amount <= self.capacity:
                self.__level = amount
            else:
                raise TankError('Too much liquid in the tank')
        elif amount < 0:
            raise TankError('Not possible to set negative liquid level')

    @level.deleter      # <<<<<<<<<<<<<< Decorated with @level.deleter. Provides the ability to set self.__level to None.
    def level(self):      # <<<<<<<<<<<< Again, same sort name, different decorator.
                                       # CALLED BY anything trying to remove __level, eg. del my_tank.level, will route here.      
        if self.__level > 0:
            print('It is good to remember to sanitize the remains from the tank!')
        self.__level = None

# our_tank object has a capacity of 20 units
our_tank = Tank(20)

# our_tank's current liquid level is set to 10 units
our_tank.level = 10
print('Current liquid level:', our_tank.level)

# adding additional 3 units (setting liquid level to 13)
our_tank.level += 3
print('Current liquid level:', our_tank.level)

# let's try to set the current level to 21 units
# this should be rejected as the tank's capacity is 20 units
try:
    our_tank.level = 21
except TankError as e:
    print('Trying to set liquid level to 21 units, result:', e)

# similar example - let's try to add an additional 15 units
# this should be rejected as the total capacity is 20 units
try:
    our_tank.level += 15
except TankError as e:
    print('Trying to add an additional 15 units, result:', e)

# let's try to set the liquid level to a negative amount
# this should be rejected as it is senseless
try:
    our_tank.level = -3
except TankError as e:
    print('Trying to set liquid level to -3 units, result:', e)

print('Current liquid level:', our_tank.level)

del our_tank.level