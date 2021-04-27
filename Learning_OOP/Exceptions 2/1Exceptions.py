                                #### EXCEPTION HANDLING 2 ####

# In python Exceptions are objects.
# There are 63 types of built in exceptions. Obviously you can make your own too using inheritance.

# Try-except, prevents operation in the try section if it would be erroneous. The except section will try
# to handle the issue.
try:
    print(int('a'))
except ValueError:
    print('You tried to do a bad thing...')

print()
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# A common convention is to catch error as e or e_variable. The error will be an object with different attributes
# depending on the type of error being raised. Typically it will be stored in e.args or e_variable.args
try:
    print(int('a'))
except ValueError as e_variable:
    print(e_variable.args)

print()
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# Here we can access ImportError instance attributes such as e.args, e.name and e.path
# Args contains the argument >>> ('No module named 'abcdefghijk'',)
# Name is the module name >>> 'abcdefghijk'
# Path is the path to any file triggering an exception. Can be None. >>> None (local error)
try:
    import abcdefghijk

except ImportError as e:
    print(e.args)
    print(e.name)
    print(e.path)

print()
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# The Unicode Error:
# UnicodeError is a sublass of ValueError. It occurs when something goes wrong with unicode coding and decoding.

# e           =       'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte
# e.encoding  =       utf-8
# e.reson     =       invalid start byte
# e.object    =       b'\x80'
# e.start     =       0
# e.end       =       1
try:
    b'\x80'.decode("utf-8")
except UnicodeError as e:
    print(e.args) # <<<< This will print all the below in a list.
    print(e)
    print(e.encoding)
    print(e.reason)
    print(e.object)
    print(e.start)
    print(e.end)

