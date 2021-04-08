                                #### ALTERNATE CONSTRUCTORS ####

# This is obviously a very poor example, a keyword argument would replace this whole @classmethod.
# However, the premise of being able to construct objects with different constructors is useful to understand.


class Car:
    # Regular constructor creates a car object with a VIN only
    def __init__(self, vin):
        print('Ordinary __init__ was called for', vin)
        self.vin = vin
        self.brand = ''

    # Classmethod constructor allows us to add Brand in too
    # cls is referenced in the first parameter spot, followed by the params for the object construction.
    @classmethod
    def including_brand(cls, vin, brand):
        print('Class method was called')
        # _car to signal it is an INTERNAL variable.
        # This is apprently the convention for the creation of an object (__init__ looks like this?)
            # Make the obj
        _car = cls(vin)
            # Add brand to it ( make sure you have allowed the allocation of 'Brand' by setting the variable
            # to an empty string on construction.)
        _car.brand = brand
            # Finally return the altered object
        return _car

#Regular __init__ (default)
car1 = Car('ABCD1234')
#Special __init__ (.including_brand())
car2 = Car.including_brand('DEFG5678', 'NewBrand')

print(car1.vin, car1.brand)
print(car2.vin, car2.brand)


