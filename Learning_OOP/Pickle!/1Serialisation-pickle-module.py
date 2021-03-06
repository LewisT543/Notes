                                #### SERIALISATION OF PYTHON OBJECTS USING THE PICKLE MODULE ####

# In Python, object serialization is the process of converting an object structure into a stream of 
# bytes to store the object in a file or database, or to transmit it via a network.
# This byte stream contains all the information necessary to reconstruct the object in another Python script.

# The reverse process is called DESERIALISATION... surprising I know

# Python objects can also be serialized using a module called 'pickle', 
# and using this module, you can 'pickle' your Python objects for later use.

# The following data types can be 'pickled'
    # None, Booleans
    # Integers, Floating point numbers, Complex numbers
    # Strings, Bytes, Bytearrays
    # Tuples, Lists, Sets, Dictionaries containing 'pickleable' objects
    # Objects, including objects with references to other objects (remember to avoid cycles!?)
    # References to functions and classes, but not their definitions.

# Example:
# This allows us to dump data as a bytestream.
import pickle

a_dict = dict()
a_dict['EUR'] = {'code':'Euro', 'symbol': '€'}
a_dict['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
a_dict['USD'] = {'code':'US dollar', 'symbol': '$'}
a_dict['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}

a_list = ['a', 123, [10, 100, 1000]]

with open('multidata.pckl', 'wb') as file_out:
    pickle.dump(a_dict, file_out)
    pickle.dump(a_list, file_out)


# This allows us to load it back up
with open('multidata.pckl', 'rb') as file_in:
    data1 = pickle.load(file_in)
    data2 = pickle.load(file_in)

print(type(data1))
print(data1)
print(type(data2))
print(data2)
print('\n\n\n')

# At the beginning of the serialization module, we mentioned that serialized objects could be persisted in a 
# database or sent via a network. This implies another two functions corresponding to the pickle.dumps() 
# and pickle.loads() functions:

# pickle.dumps(object_to_be_pickled) – expects an initial object, returns a byte object. 
# This byte object should be passed to a database or network driver to persist the data;

# pickle.loads(bytes_object) – expects the bytes object, returns the initial object.

a_list = ['a', 123, [10, 100, 1000]]
bytes = pickle.dumps(a_list)
print('Intermediate object type, used to preserve data:', type(bytes))

# now pass 'bytes' to appropriate driver
# therefore when you receive a bytes object from an appropriate driver you can deserialize it

print(bytes)
b_list = pickle.loads(bytes)
print('A type of deserialized object:', type(b_list))
print('Contents:', b_list)
print('\n\n\n')

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# Attempts to pickle a non-pickleable object will result in PicklingError exceptions.
# Trying to pickle highly recursive data structures may exceed the maximum recursion depth and a, RecursionError will be
# raised.
# Note that functions (both built-in and user-defined) are pickled by their name reference, not by any value. 
# This means that only the function name is pickled; neither the function’s code, nor any of its function attributes, are pickled.

# Hence, your role is to ensure that the environment where the class or function is unpickled is able to import the class or function 
# definition. In other words, the function or class must be available in the namespace of your code reading the pickle file.
# Otherwise, an AtrributeError exception will be raised.

# Example:
'''
class Cucumber:
    def __init__(self):
        self.size = 'small'

    def get_size(self):
        return self.size

cucu = Cucumber()

with open('cucumber.pckl', 'wb') as file_out:
    pickle.dump(cucu, file_out)
'''    
# On first glance it looks like we have pickled our class sucessfully
# However, if we get rid of the class definition from the namespace, we get an error when we run this second bit.
#####

with open('cucumber.pckl', 'rb') as file_in:
    data = pickle.load(file_in)

print(type(data))
print(data)
print(data.size)
print(data.get_size())

# output:
# Traceback (most recent call last):
  # File "main.py", line 4, in <module>
    # data = pickle.load(file_in)
# AttributeError: Can't get attribute 'Cucumber' on <module '__main__' from 'main.py

'''The remedy for the above problems is: the code that calls the load() or loads() 
functions of pickle should already know the function/class definition.'''