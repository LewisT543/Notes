                                #### SHALLOW COPYING ####

# Copying (the [:] array slice)
# using [:] allows us to take a slice of the whole list and copy it. This is a fresh copy of the list object.

print("Part 1")
print("Let's make a copy")
a_list = [10, "banana", [997, 123]]
b_list = a_list[:]
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

# output:
# Part 1
# Let's make a copy
# a_list contents: [10, 'banana', [997, 123]]
# b_list contents: [10, 'banana', [997, 123]]
# Is it the same object? False

print()
print("Part 2")
print("Let's modify b_list[2]")
b_list[2][0] = 112
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

# output:
# Part 2
# Let's modify b_list[2]
# a_list contents: [10, 'banana', [112, 123]]
# b_list contents: [10, 'banana', [112, 123]]
# Is it the same object? False

# Interrestingly, even though b_list is a copy of a_list and a seperate object, a change to b_list will also take effect 
# on a_list too.

# Explaination:

# 1. The 'a_list' object is a compound object (made up of other objects)

# 2. We’ve run a shallow copy that constructs a new compound object, b_list in our example,
# and then populated it with REFERENCES to the objects found in the original.

# 3. A shallow copy is only one level deep. The copying process does not recurse and therefore does not create 
# copies of the child objects, but instead populates b_list with REFERENCES to the already existing objects.

# a_list       memory       b_list
#   [0]  >>>    10     <<<    [0]
#   [1]  >>>  'banana' <<<    [1]
#   [2]  >>> [997,123] <<<    [2]