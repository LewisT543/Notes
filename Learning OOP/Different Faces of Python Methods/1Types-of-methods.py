                                #### Different types of Methods (OOP) ####

### INSTANCE METHODS                                   
# Instance methods are basically these ***, any method which applies to the specific instance of the class.

class Example:
    def __init__(self, value):
        self.__internal = value

    #INSTANCE METHOD >> categorised by (self), refering to the specific instance of the class
    def get_internal(self):
        return self.__internal

# Two seperate Example objects(instances), each able to perform the get_internal() function on itself.
e1 = Example(10)
e2 = Example(20)
print(e1.get_internal())
print(e2.get_internal())
print('><><><>  EX1  <><><><')

### CLASS METHODS
# A class method is any method that changes the functionality of a CLASS
# They are bound to the class as opposed to the instances of said class.
# They can be used as an alternative way to create objects

class Example2:
    __internal_counter = 0 

    def __init__(self, value):
        self._val = value
        Example2.__internal_counter += 1

    # CLASS VARIABLE >>> categorised by (cls) parameter, refering to the class in general 
    @classmethod
    def get_internal_counter(cls):
        return f'Number of Objects created: {cls.__internal_counter}'

    # Instance Variable
    def get_val(self):
        return f'Value of instance: {self._val}'

print(Example2.get_internal_counter())
ex1 = Example2(10)
print(Example2.get_internal_counter())
print(ex1.get_val())
ex2 = Example2(99)
print(Example2.get_internal_counter())
print(ex2.get_val())
print('><><><>  EX2  <><><><')

### STATIC METHODS
# Static methods are methods that do not require or expect a (cls) or (self) param.
# They are usually related to the class but do not necessarily change the Class or Instance 
# and do not need an instance to operate from.
# Utility method only!


class BankAccount:

    def __init__(self, iban):
        print('__init__ called')
        self.iban = iban

    # Notice only iban being passed
    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False


account_numbers = ['8' * 20, '7' * 4, '2222']

for elem in account_numbers:
    if BankAccount.validate(elem):
        print(f'Successfully Validated Iban: {elem}. This number may be used to create a bank account.')
    else:
        print(f'Validation failed, {elem} invalid.')

print('><><><>  EX3  <><><><')