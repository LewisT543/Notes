
# 1. Create a class named TemperatureConverter and its convert_celsius_to_fahrenheit method. The convert_celsius_to_fahrenheit 
    # method should convert the temperature from Celsius to Fahrenheit. Use the following formula:
        # F = 9/5 * C + 32.
# 2. Create a class named ForecastXmlParser and its parse method responsible for reading data from forecast.xml. Use the 
    # TemperatureConverter class to convert the temperature from Celsius to Fahrenheit (rounded to one decimal place). 
    # The parse method should print the following results:
'''
    Monday: 28 Celsius, 82.4 Fahrenheit
    Tuesday: 27 Celsius, 80.6 Fahrenheit
    Wednesday: 28 Celsius, 82.4 Fahrenheit
    Thursday: 29 Celsius, 84.2 Fahrenheit
    Friday: 29 Celsius, 84.2 Fahrenheit
    Saturday: 32 Celsius, 89.6 Fahrenheit
    Sunday: 33 Celsius, 91.4 Fahrenheit    
'''

import xml.etree.ElementTree as ET


class TemperatureConverter:
    def convert_c_to_f(self, c):
        try:
            f = round(9/5 * c + 32, 1)
        except Exception as e:
            print(f'Error: {e.args}')
        return f

class ForecastXmlParser:
    def __init__(self):
        self.tree = ET.parse('forecast.xml')
        self.root = self.tree.getroot()
        self.converter = TemperatureConverter()
    
    def print_all(self):
        print()
        for item in self.root:
            fh = self.converter.convert_c_to_f(float(item[1].text))
            print(f'{item[0].text}: {item[1].text} Celsius, {fh} Farenheight')
        print()

forecast = ForecastXmlParser()
forecast.print_all()