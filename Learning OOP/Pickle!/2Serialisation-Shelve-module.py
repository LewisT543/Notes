                                #### THE SHELVE MODULE ####

# Serialization of Python objects using the shelve module
# Shelve is a module buit off of Pickle that allows us to store serialised objects in key:value pairs.
# These keys must be STRINGS as that is what the underlying database demands.


# Example:
# Meaning of the optional flag paramater:
"""
'r' >>>	Open existing database for reading only
'w'	>>> Open existing database for reading and writing
'c'	>>> Open database for reading and writing, creating it if it doesn’t exist (this is a default value)
'n'	>>> Always create a new, empty database, open for reading and writing
"""

import shelve

shelve_name = 'first_shelve.shlv'

my_shelve = shelve.open(shelve_name, flag='c')              # <<<<<<<<<<<<< This flag param here.
my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = {'code':'US dollar', 'symbol': '$'}
my_shelve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}
my_shelve.close()

new_shelve = shelve.open(shelve_name)
print(new_shelve['USD'])
new_shelve.close()

# ouput:
# {'code': 'US dollar', 'symbol': '$'}

# Step 1).
    # create the shelve
    # shelve_name = 'first_shelve.shlv'
# Step 2).
    # open it
    # my_shelve = shelve.open(shelve_name, flag='c')
# Step 3).
    # allocate the variables
    # my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
# Step 4).
    # close it
    # my_shelve.close()
# Step 5).
    # re-open and use it
    # new_shelve = shelve.open(shelve_name)
    # print(new_shelve['USD']), will print value associated with the 'USD' key.
    # new_shelve.close() to finish up with.

'''
You should treat a shelve object as a Python dictionary, with a few additional notes:

the keys must be strings;
Python puts the changes in a buffer which is periodically flushed to the disk. To enforce an immediate flush, 
call the sync() method on your shelve object.
When you call the close() method on an shelve object, it also flushes the buffers.

When you treat a shelve object like a Python dictionary, you can make use of the dictionary utilities:
the len() function;
the in operator;
the keys() anditems() methods;
the update operation, which works the same as when applied to a Python dictionary;
the del instruction, used to delete a key-value pair.

And the final remark is:

because the shelve module is backed by pickle, it isn’t safe to load a shelve from an untrusted source. 
As with pickle, loading a shelve can execute arbitrary code.
'''
