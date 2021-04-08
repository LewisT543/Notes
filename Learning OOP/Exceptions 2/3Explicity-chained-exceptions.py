                                #### EXPLICITLY CHAINED EXCEPTIONS ####

# This time we'd like to convert an explicit type of exception object to another type of exception 
# object at the moment when the second exception is occurring.

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

#personnel_check()

# This allows us to specifically pinpoint the issue, provided we are aware it is a possible error and can pre-define it
# in our code.

# The __cause__ attribute:
# the cause attribute will tell us what errors caused the exception instance in question.

try:
    personnel_check()
except RocketNotReadyError as f:
    print('General exception: "{}", caused by "{}"'.format(f, f.__cause__))

# output:
# Final check procedure
#         The captain's name is John
#         The pilot's name is Mary
#         The mechanic's name is Mike
# General exception: "Crew is incomplete", caused by "list index out of range"

# This doesnt cause a traceback error and doesnt break out of our program, considered handled in a 'safe' way.

# Extended example:
def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100 / 0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e

crew = ['John', 'Mary', 'Mike']
fuel = 100
check_list = [personnel_check, fuel_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))

# This allows us to see two different errors AND the errors they were triggered by (all as RocketNotReadyException(s)), 
# all without 'breaking' the program.
# output:
# ...
# RocketNotReady exception: "Crew is incomplete", caused by "list index out of range"
# RocketNotReady exception: "Problem with fuel gauge", caused by "division by zero"

