                                #### THE __TRACEBACK__ ATTRIBUTE ####

# Each exception object owns a __traceback__ attribute.
# Python allows us to operate on the traceback details (use them in code) because every exception has one.

# Example:

class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


crew = ['John', 'Mary', 'Mike']

print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print(f.__traceback__)
    print(type(f.__traceback__))

# This __traceback__ attribute is a traceback object and must be treated as such.
# We can use format_tb() method; or the print_tb() method to print errors directly to console.

import traceback

try:
    personnel_check()
except RocketNotReadyError as f:
    print(f.__traceback__)
    print(type(f.__traceback__))
    print('\nTraceback details')
    details = traceback.format_tb(f.__traceback__)
    print("\n".join(details))

print('Final check is over')

# This allows us to essentially allow certain errors through our code. We know this as we see 'Final check is over',
# is printed following erroneous code above it.

# output:
'''<traceback object at 0x000001C6D8679700>
<class 'traceback'>

Traceback details
  File "c:/Users/Lewis/py/Learning OOP/Exceptions 2/5Traceback-attribute.py", line 38, in <module>
    personnel_check()

  File "c:/Users/Lewis/py/Learning OOP/Exceptions 2/5Traceback-attribute.py", line 19, in personnel_check
    raise RocketNotReadyError('Crew is incomplete') from e

Final check is over'''
