                            #### XML PARSING ####

# xml.etree.ElementTree – has a very simple API for analyzing and creating XML data. It's an excellent choice for people 
    # who have never worked with the Document Object Model (DOM) before.
# Extensible Markup Language (XML) is a markup language intended for storing and transporting data, e.g., by systems using the 
    # SOAP communication protocol. One of its main advantages is the ability to define your own tags that make the document more readable 
    # to humans. XML is a standard recommended by the W3C organization. Let's look at what elements XML documents contain:
        
        # PROLOG – the first (optional) line of the document. In the prolog, you can specify character encoding, e.g., <?xml version="1.0" 
            # encoding="ISO-8859-2"?> changes the default character encoding (UTF-8) to ISO-8859-2.
        
        # ROOT ELEMENT – the XML document must have one root element that contains all other elements. In the example below, 
            # the main element is the data tag.
        
        # ELEMENTS – these consist of opening and closing tags. The elements include text, attributes, and other child elements. 
            # In the example below, we can find the book element with the title attribute and two child elements (author and year).
        
        # ATTRIBUTES – these are placed in the opening tags. They consist of key-value pairs, e.g., title = "The Little Prince".
    
    # NOTE: Each open XML tag must have a corresponding closing tag.

# <><><><><>><><><><><><><>><><><><><><><>><><><><><><><>><><><><><><><>><><><><><><><>><><><><><><><>><><><><><><><>><><><><><><><>><><> #

    # XML PARSING PART-1 #
# Processing XML files in Python is very easy thanks to the ElementTree class provided by the xml.etree.ElementTree module.
# The ElementTree object is responsible for presenting the XML document in the form of a tree on which we can move up or down.

# To create a tree (an ElementTree object) from an existing XML document, pass it to the parse method.

import xml.etree.ElementTree as ET

# we can use parse to get the tree from the XML doc and then we can find the root using getroot()
tree = ET.parse('books\\books.xml')
root = tree.getroot()

# using fromstring() we can pass XML in string form
# NOTE: The fromstring method doesn't return the ElementTree object, but instead returns the root element represented by the Element class.
root = ET.fromstring(
    '''<?xml version="1.0"?>
    <data>
        <book title="The Little Prince">
            <author>Antoine de Saint-Exupéry</author>
            <year>1943</year>
        </book>
        <book title="Hamlet">
            <author>William Shakespeare</author>
            <year>1603</year>
        </book>
    </data>''')


    # XML PARSING PART-2 #
# In this example, we use the following properties:
# TAG – this returns the tag name as a string
# ATTRIB – this returns all attributes in the tag as a dictionary. To retrieve the value of a single attribute, 
    # use its key, e.g., child.attrib['title'].

tree = ET.parse('books\\books.xml')
root = tree.getroot()
print('The root tag is:', root.tag)
print('The root has the following children:')
for child in root:
    print(child.tag, child.attrib)

# output:
# The root tag is: data
# The root has the following children:
# book {'title': 'The Little Prince'}
# book {'title': 'Hamlet'}


    # XML PARSING PART-3 #
# In addition to iterating over tree elements, we can access them directly using indexes.
# we use the current book element to retrieve text from its child elements
# EXAMPLE:

tree = ET.parse('books\\books.xml')
root = tree.getroot()
print("My books:\n")
for book in root:
    print('Title: ', book.attrib['title'])
    print('Author:', book[0].text)
    print('Year: ', book[1].text, '\n')

# Using book[0] will refer to the first child of the book element (in this case: {'title': 'The Little Princess'})
# using book[0][0] will refer to the first child of book[0].
    # in this case book[0][0].text = 'Author: Antoinede Saint-Exupery'


    # XML PARSING PART-4 #
# The xml.etree.ElementTree module, or more precisely, the Element class, provides several useful methods for 
    # finding elements in an XML document. Let's start with the method called iter.

# The ITER method returns all elements by having the tag passed as an argument. The element that calls it is treated 
    # as the main element from which the search starts.
# In order to find all matches, the iterator iterates recursively through all child elements and their nested elements.

# Example:

tree = ET.parse('books.xml')
root = tree.getroot()
for author in root.iter('author'):  # <<< pass 'author', the name of the element atribute to .iter() 
    print(author.text)

# output:
# Antoine de Saint-Exupéry
# William Shakespeare


    # XML PARSING PART-5 #
# The Element object has a method called findall() to search for direct child elements.
# Unlike the iter() method, the findall() method only searches the children at the first nesting level.

tree = ET.parse('books.xml')
root = tree.getroot()
for author in root.findall('author'):
    print(author.text)

# NOTE: The example doesn't return any results, because the findall method can only iterate over the book elements 
    # that are the closest children of the root element.
# To display the value of the title attributes, we use the get() method, which looks much better than a book.attrib ['title'] call. 
    # Its use is very simple: just enter the name of the attribute and optionally (as a second argument) the value that will be 
    # returned if the attribute is not found (the default is None).
# NOTE: The findall method also accepts an XPath expression.
    # XPath expression - An XPath expression generally defines a pattern in order to select a set of nodes. These patterns are used by 
        # XSLT to perform transformations or by XPointer for addressing purpose. XPath specification specifies seven types of nodes which 
        # can be the output of execution of the XPath expression.
    # XPath uses a path expression to select node or a list of nodes from an XML document.
    # NEEDS MORE RESEARCH MAYBE? DO PEOPLE ACTUALLY USE XML?


    # XML PARSING PART-6 #
# Another useful method used to parse an XML document is a method called find. The find method returns the first child element containing 
    # the specified tag or matching XPath expression.

# EXAMPLE:
tree = ET.parse('books.xml')
root = tree.getroot()
print(root.find('book').get('title'))
   
# output:
# The Little Prince

# In the example, we use the find method to find the first child element containing the book tag, and then display the value of its 
    # title attribute. Note that the element from which we start the search is the root element.