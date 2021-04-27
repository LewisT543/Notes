                                #### CHAINING EXCEPTIONS ####

# This chaining concept introduces two attributes of exception instances:
#   the __context__ attribute, 
#  which is inherent for implicitly chained exceptions;
#   the __cause__ attribute, 
#  which is inherent for explicitly chained exceptions.

# These are useful for keeping a reference to the original exception object in a consistent way.
# useful for later processing like logging.

# Example:

a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    #print(0 / 0)
    print(e)

# Output of this code indicates that 2 exceptions were chained together. The IndexError from trying to print
# element 3 of a_list[[0], [1]], triggered a DivisionByZeroError by way of the except statement.
print()
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>#

# The following exception demonstrates the __context__ attribute
try:
    print(a_list[3])
except Exception as e:
    try:
        # the following line is a developer mistake - they wanted to print progress as 1/10	but wrote 1/0
        print(1 / 0)
    except ZeroDivisionError as f:
        print('Inner exception (f):', f)
        print('Outer exception (e):', e)
        print('Outer exception referenced:', f.__context__)
        print('Is it the same object:', f.__context__ is e)

# output:
# Inner exception (f): division by zero
# Outer exception (e): list index out of range
# Outer exception referenced: list

