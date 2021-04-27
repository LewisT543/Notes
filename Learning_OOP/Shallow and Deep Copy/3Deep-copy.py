                                #### DEEP COPYING ####

# Copying using the 'copy.deepcopy()' function from the python 'copy' module
# Copy using deepcopy() does the following:
# 1. Constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original
# 2. It takes more time to complete, as there are many more operations to be performed;
# 3. Is delivered by the python 'copy' module

# A SHALLOW COPY will refer to the SAME chunk in memory. A DEEP COPY will refer to a SEPERATE chunk in memory.

import copy

print("Let's make a deep copy")
a_list = [10, "banana", [997, 123]]
b_list = copy.deepcopy(a_list)
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

# output:
# Let's make a deep copy
# a_list contents: [10, 'banana', [997, 123]]
# b_list contents: [10, 'banana', [997, 123]]
# Is it the same object? False


print()
print("Let's modify b_list[2]")
b_list[2][0] = 112
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

# output:
# Let's modify b_list[2]
# a_list contents: [10, 'banana', [997, 123]]
# b_list contents: [10, 'banana', [112, 123]]
# Is it the same object? False

