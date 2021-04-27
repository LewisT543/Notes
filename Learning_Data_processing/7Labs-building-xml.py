
# You are a programmer working for an online store. Your task is to build an XML document containing information 
    # about the three vegan products available in the store:
'''
<?xml version="1.0"?>
<shop>
    <category name="Vegan Products">
        <product name="Good Morning Sunshine">
            <type>cereals</type>
            <producer>OpenEDG Testing Service</producer>
            <price>9.90</price>
            <currency>USD</currency>
        </product>
        <product name="Spaghetti Veganietto">
            <type>pasta</type>
            <producer>Programmers Eat Pasta</producer>
            <price>15.49</price>
            <currency>EUR</currency>
        </product>
        <product name="Fantastic Almond Milk">
            <type>beverages</type>
            <producer>Drinks4Coders Inc.</producer>
            <price>19.75</price>
            <currency>USD</currency>
        </product>
    </category>
</shop>
'''
 # Save the document to the shop.xml file. Use UTF-8 character encoding and don't forget to add the prolog to the beginning of the file.

import xml.etree.ElementTree as ET

class XMLBuilder:
    
    attributes_1 = {'type': 'cereals', 'producer': 'OpenEDG Testing Service', 'price': '9.90', 'currency': 'USD'}
    attributes_2 = {'type': 'pasta', 'producer': 'Programmers Eat Pasta', 'price': '15.49', 'currency': 'EUR'}
    attributes_3  = {'type': 'beverages', 'producer': 'Drinks4Coders Inc.', 'price': '19.75', 'currency': 'USD'}
    
    def __init__(self):
        self.root = ET.Element('shop')
        self.subtitle = ET.SubElement(self.root, 'category', {'name': 'Vegan Products'})
        self.prod_1 = ET.SubElement(self.subtitle, 'product', {'name': "Good Morning Sunshine"})
        self.prod_2 = ET.SubElement(self.subtitle, 'product', {'name': "Spaghetti Veganietto"})
        self.prod_3 = ET.SubElement(self.subtitle, 'product', {'name': "Fantastic Almond Milk"})

    def add_tags_with_text(self, parent, tags):
        elements = []
        for tag in tags:
            element = ET.SubElement(parent, tag)
            element.text = tags[tag]
            elements.append(element)
        return elements

xml = XMLBuilder()
xml.add_tags_with_text(xml.prod_1, XMLBuilder.attributes_1)
xml.add_tags_with_text(xml.prod_2, XMLBuilder.attributes_2)
xml.add_tags_with_text(xml.prod_3, XMLBuilder.attributes_3)
ET.dump(xml.root)
tree = ET.ElementTree(xml.root)
tree.write('shop.xml', 'UTF-8', True)
# SOOOO turns out this is really fucking stupid. In order to make the XML document, this tutorial suggests hardcoding the attribute dictionaries.
# my answer to that is: Just type it into the fucking XML doc if your gonna type each one out... Stupid task.
