                                #### SHALLOW AND DEEP COPY ####

# a_list = [ 1, 'New York', 100]
# a_list: Variable(label)
# =: 'Assigned to'(reference)
# [1, 'New York', 100]: Object(can consist of other objects)

# The id() function:
# The built in id() function will return the 'identity' of an object.
# It is an integer which is guaranteed to be unique and constant during this objects lifetime.
# Two objects with non-overlapping lifetimes may have the same id() value.

# Example:

a_string = '10 days to departure'
b_string = '20 days to departure'

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))

# output:
'''
a_string identity: 139666519302832
b_string identity: 139666519302912
'''
# This identity can be considered the address of the object in memory, not an absolute memory address.

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# If two variables are pointed to the same object, the id() values will be the same

# Example:

a_string = '10 days to departure'
b_string = a_string

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
print()

# output:
# a_string identity: 140215825719984
# b_string identity: 140215825719984

# In this example, we have not created a new string, we have just refered to the same object twice.

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# Difference between '==' and 'is' operators:
# The '==' operator checks VALUES of objects and checks for value equality. Two different objects holding the same values would 
# satisfy the '==' operator.
# The 'is' operator checks to see if both operands refer to the SAME object, it checks IDENTITY.
# To best illustrate this, an Example:

a_string = ['10', 'days', 'to', 'departure']
b_string = a_string

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
print('The result of the value comparison:', a_string == b_string)
print('The result of the identity comparison:', a_string is b_string)

# output:
# a_string identity: 2853921611648
# b_string identity: 2853921611648
# The result of the value comparison: True
# The result of the identity comparison: True

print()

a_string = ['10', 'days', 'to', 'departure']
b_string = ['10', 'days', 'to', 'departure']

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
print('The result of the value comparison:', a_string == b_string)
print('The result of the identity comparison:', a_string is b_string)

# output:
# a_string identity: 2853923237312
# b_string identity: 2853924423552
# The result of the value comparison: True
# The result of the identity comparison: False

# We can look at this as two cenarios:
    # 1. SAME OBJECT TWO VARIABLES (a_list = [x, y, z]; b_list = a_list) 
    # a_list >>> |memory chunck| <<< b_list

    # 2. DIFFERENT OBJECT TWO VARIABLES (a_list = [x, y, z]; b_list = [x, y, z])
    # a_list >>> |memory chunk #1|      b_list >>> |memory chunk #2|



