                            #### XML ####

# XML stands for:
    # eXtendable
    # Markup
    # Language

# XML is a language. But not a programming language, (it is possible to build ontop of XML but why would you?). XML is - like JSON - a UNIVERSAL
    # AND TRANSPARENT CARRIER of any type of data. For example, MSOffice applications use XML (docX, etc) for all sorts of data types.
# As you probably suspect, XML is much older than JSON. Moreover, it's heavier and less flexible. 
    # We can even say that XML seems to be bloated compared to JSON.    

# We’re not going to teach you how to use XML in Python.

# XML EXAMPLE:

'''
<?xml version = "1.0" encoding = "utf-8"?> 
<!-- cars.xml - List of cars ready to sell -->
<!DOCTYPE cars_for_sale SYSTEM "cars.dtd">
<cars_for_sale>
   <car>
      <id>1</id>
      <brand>Ford</brand>
      <model>Mustang</model>
      <production_year>1972</production_year>
      <price currency="USD">35900</price>
   </car>
   <car>
      <id>2</id>
      <brand>Aston Martin</brand>
      <model>Rapide</model>
      <production_year>2010</production_year>
      <price currency="GBP">32000</price>
   </car>
</cars_for_sale>
'''

# Eww, disgusting, looks like HTML. JSON all the way my friend...
# Pretty much the only similarity between JSON and XML is that they both use plain text. 

import xml.etree.ElementTree

cars_for_sale = xml.etree.ElementTree.parse('cars.xml').getroot()
print(cars_for_sale.tag)
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for prop in car:
        print('\t\t', prop.tag, end='')
        if prop.tag == 'price':
            print(prop.attrib, end='')
    print(' =', prop.text)

# Creating XML programmatically:

import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse('cars.xml')
cars_for_sale = tree.getroot()
for car in cars_for_sale.findall('car'):
    # Delete the mustang
    if car.find('brand').text == 'Ford' and car.find('model').text == 'Mustang':
        cars_for_sale.remove(car)
        break
# Add something else
new_car = xml.etree.ElementTree.Element('car')
xml.etree.ElementTree.SubElement(new_car, 'id').text = '4'
xml.etree.ElementTree.SubElement(new_car, 'brand').text = 'Maserati'
xml.etree.ElementTree.SubElement(new_car, 'model').text = 'Mexico'
xml.etree.ElementTree.SubElement(new_car, 'production_year').text = '1970'
xml.etree.ElementTree.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
cars_for_sale.append(new_car)
tree.write('newcars.xml', method='')

# As you can see, working with XML doesn't require you to be a rocket scientist, but – if we’re being honest – 
    # JSON is more convenient and – last but most important – most currently implemented services use JSON, not XML.

