                                #### EXAMPLE INHERITANCE AND COMPOSITION ####
'''
Define classes representing:
    tires (as a bundle needed by a car to operate); methods available: get_pressure(), pump(); attribute available: size
    engine; methods available: start(), stop(), get_state(); attribute available: fuel type
    vehicle; method available: __init__(VIN, engine, tires); attribute available: VIN

based on the classes defined above, create the following objects:
    two sets of tires: city tires (size: 15), off-road tires (size: 18)
    two engines: electric engine, petrol engine

instantiate two objects representing cars:
    the first one is a city car, built of an electric engine and city tires
    the second one is an all-terrain car build of a petrol engine and off-road tires

play with the cars by calling methods responsible for interaction with components.
'''



class Tires:
    def __init__(self, size):
        self.size = size

    def get_pressure(self):
        return 'Pressure is 5.'

    def pump(self):
        return 'Pumping'

class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        return 'Starting Engine'

    def stop(self):
        return 'Stopping Engine'

    def get_state(self):
        return 'Getting the state of the engine'

class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires
        

city_tires = Tires(15)
off_road_tires = Tires(18)
electric_engine = Engine('Electric')
petrol_engine = Engine('Petrol')

city_car = Vehicle(1234, electric_engine, city_tires)
all_terrain_car = Vehicle(4321, petrol_engine, off_road_tires)

print(city_car.engine.stop())
print(all_terrain_car.tires.get_pressure())