import logging
import random
import time

FORMAT = '%(levelname)s - %(message)s'

class BatterySimulation:
    def __init__(self, logger):
        self.logger = logger
    
    def simulate_last_hour(self):
        for min in range(1, 60+1):
            temperature = random.randint(20, 40)
            if temperature < 30:
                self.logger.debug('{0} C'.format(temperature))
            elif temperature >= 30 and temperature <= 35:
                self.logger.warning('{0} C'.format(temperature))
            elif temperature > 35:
                self.logger.critical('{0} C'.format(temperature))
            else:
                raise Exception('Temperature out of range.')



FORMAT = '%(levelname)s - %(message)s'

# Set the logger
logger = logging.getLogger('battery.temperature')
logger.setLevel(logging.DEBUG)

# Sort out the filehandler
handler = logging.FileHandler('battery_temperature.log', mode='w')
handler.setLevel(logging.DEBUG)

# Format
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

# add the handler to the logger
logger.addHandler(handler)

battery_simulation = BatterySimulation(logger)
battery_simulation.simulate_last_hour()


