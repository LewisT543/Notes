                            #### XML MODIFYING ####

# Let's modify the element tree and create a new XML file based on it with the following movie data:
'''
<?xml version="1.0"?>
<data>
    <movie title="The Little Prince" rate="5"></movie>
    <movie title="Hamlet" rate="5"></movie>
</data>
'''
# To change the tag of the Element object, we must assign a new value to its tag property.
# EXAMPLE

import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
for child in root:
    child.tag = 'movie'
    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)
print()
# output:
# movie {'title': 'The Little Prince'}
# author : Antoine de Saint-Exupéry
# year : 1943
# movie {'title': 'Hamlet'}
# author : William Shakespeare
# year : 1603

# In the example, during each iteration through the book elements, we replace them with the movie tag, 
    # and then make sure that all changes have gone through correctly.


    # MODIFYING AN XML DOCUMENT PART-2 #
# Our XML has a few unnecessary elements, such as author and year. In order to remove them, we need to use the 
    # method called remove, provided by the Element class.    
# The remove method removes the child element passed as its argument, which must be an Element object. Note that for 
    # this purpose we use the method called find, which you're already familiar with.

# EXAMPLE:

tree = ET.parse('books.xml')
root = tree.getroot()
for child in root:
    child.tag = 'movie'
    child.remove(child.find('author'))      # <<< Binning off the first instance of 'author' the parser can find in that 'level'
    child.remove(child.find('year'))        # <<< likewise for 'year'
    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)
print()


    # MODIFYING AN XML DOCUMENT PART-3 # 
# Do you remember the get method that gets the value of the attribute? The Element object also has a method called set, 
    # which allows you to set any attribute.
# The set method takes the attribute name and its value as arguments. In our case, we use it to set the highest rating for each of the movies.

# EXAMPLE:

tree = ET.parse('books.xml')
root = tree.getroot()
for child in root:
    child.tag = 'movie'
    child.remove(child.find('author'))
    child.remove(child.find('year'))
    child.set('rate', '5')          # <<< .set(attribute_name, value_to_set)
    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)

# output
# movie {'title': 'The Little Prince', 'rate': '5'}
# movie {'title': 'Hamlet', 'rate': '5'}


    # MODIFYING AN XML DOCUMENT PART-4 #
# You must have noticed that the modified XML document is not saved anywhere. To save all the changes we’ve made to the tree, 
    # we have to use the method called write.
# The write method has only one required argument, which is a file name of the output XML file, or a file object opened for writing. 
    # In addition, we can define character encoding by using the second argument (the default is US-ASCII). To add a prolog to our 
    # document, we must pass True in the third argument.

# Continued from above ^^^^^^^^^^^^^^^^
tree.write('movies.xml', 'UTF-8', True)

# output:
# FILE SAVED AS 'movies.xml'
# The created file looks like this:
'''
    <?xml version='1.0' encoding='UTF-8'?>
    <data><movie rate="5" title="The Little Prince" /><movie rate="5" title="Hamlet" /></data>
'''

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

    # BUILDING AN XML DOCUMENT PART-1 #
# The Element class constructor takes two arguments. The first is the name of the tag to be created, while the second (optional) is the 
    # attribute dictionary. In the example in the editor, we've created the root element represented by a data tag with no attributes.

# EXAMPLE:

root = ET.Element('data')
ET.dump(root)

# output:
# <data />

# In the example above, we use the dump method, which allows us to debug either the whole tree or a single element.

    # BULDING AN XML DOCUMENT PART-2 #
# In addition to the Element class, the xml.etree.ElementTree module offers a function for creating child elements called SubElement. 
    # The SubElement function takes three arguments.
# The first one defines the parent element, the second one defines the tag name, and the third (optional) defines the attributes of the element.

# EXAMPLE:

root = ET.Element('data')
movie_1 = ET.SubElement(root, 'movie', {'title': 'The Little Prince', 'rate': '5'})
movie_2 = ET.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '5'})
ET.dump(root)

# output:
# <data><movie rate="5" title="The Little Prince" /><movie rate="5" title="Hamlet" /></data>

# In the example, we've added two child elements called movie to the root element.
# The created elements are objects of the Element class, so we can use all of the methods that we learned about during this course.

# NOTE: To save a document using the write method, we need to have an ElementTree object. To do this, pass our root element to its constructor:

tree = ET.ElementTree(root)     # <<< This will create an ElementTree Object capable of the .write() method.