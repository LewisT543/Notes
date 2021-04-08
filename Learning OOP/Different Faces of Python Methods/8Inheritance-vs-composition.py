                                #### INHERITANCE VS COMPOSITION ####

### INHERITANCE
# Inheritance models what is called an 'IS A' relation.
# Examples:
    # a Laptop is a (specialized form of) Computer;
    # a Square is a (specialized form of) Figure;
    # a Hovercraft is a Vehicle.

# Following this, once you inherit a property from a superclass, the subclass will have this property too.
'''inheritance extends a class's capabilities by adding new components and modifying existing ones; in other words, 
the complete recipe is contained inside the class itself and all its ancestors; the object takes all the class's belongings 
and makes use of them'''

### COMPOSITION
# Composition models what is called a 'HAS A' relation.
# Examples:
    # a Laptop has a network card;
    # a Hovercraft has a specific engine.

# Composition is the process of composing an object using other different objects. The objects used in the composition deliver
# a set of desired traits (properties and/or methods) so we can say that they act like blocks used to build a more complicted structure.
'''composition projects a class as a container (called a composite) able to store and use other objects (derived from other classes) 
where each of the objects implements a part of a desired class's behavior. It’s worth mentioning that blocks are loosely coupled with 
the composite, and those blocks could be exchanged any time, even during program runtime.'''

class Car:
    def __init__(self, engine):
        self.engine = engine

class GasEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print(f'Starting {self.hp}hp gas engine')

class DieselEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print(f'Starting {self.hp}hp diesel engine')


my_car = Car(GasEngine(4))
my_car.engine.start()
my_car.engine = DieselEngine(2)
my_car.engine.start()

# Basically we are able to have an object become part of another object. Accessible using: TopLevelClass.MidLevelClass.method().

# Another Example using both methods.
    # If a problem fits a 'IS A' relationship, use Inheritance.
    # If a problem fits a 'HAS A' relationship, use Composition

class Base_Computer:
    def __init__(self, serial_number):
        self.serial_number = serial_number


class Personal_Computer(Base_Computer):        
    def __init__(self, sn, connection):         # <<<< Composition Example (connection param is an object of class Connection.)
        super().__init__(sn)
        self.connection = connection
        print('The computer costs $1000')

# This is the base connection Class, the 3 classes that inherit from this are then used in the composition above
# That allows us to do personal_computer.connection.method()...

class Connection:
    def __init__(self, speed):
        self.speed = speed

    def download(self):
        print('Downloading at {}'.format(self.speed))


class DialUp(Connection):
    def __init__(self):
        super().__init__('9600bit/s')

    def download(self):
        print('Dialling the access number... '.ljust(40), end='')
        super().download()


class ADSL(Connection):
    def __init__(self):
        super().__init__('2Mbit/s')

    def download(self):
        print('Waking up modem... '.ljust(40), end='')
        super().download()


class Ethernet(Connection):
    def __init__(self):
        super().__init__('10Mbit/s')

    def download(self):
        print('Constantly connected... '.ljust(40), end='')
        super().download()

# I started my IT adventure with an old-school dial up connection
my_computer = Personal_Computer('1995', DialUp())
my_computer.connection.download()

# then it came year 1999 with ADSL
my_computer.connection = ADSL()
my_computer.connection.download()

# finally I upgraded to Ethernet
my_computer.connection = Ethernet()
my_computer.connection.download()
