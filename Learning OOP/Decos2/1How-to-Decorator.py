                                            # >>> IMPORTANT DECORATOR STUFF <<< # 

# A decorator is a very powerful and useful tool in Python, because it allows programmers to modify the behavior of a function, 
# method, or class.

# Decorators allow us to wrap another callable object in order to extend its behavior.

# Decorators rely heavily on closures and *args and **kwargs.

from datetime import datetime

# Firstly we must define our decorator
    # Essentially I am rewriting generic_funct to include the functionality of my decorator (timestamper) on the fly.
    # Its important to remember that the original function is not actually ever run.

def timestamper(my_function): #2
    def internal_wrapper(*args, **kwargs): #4
        timestamp = datetime.now()  #5
        print(f'{my_function.__name__} called...') #6 
        print(f'At time {timestamp}...\nwith arguments {args}, {kwargs}') #7 
        my_function(*args, **kwargs) #8
        print('Decorator still operating...') #11
    return internal_wrapper #3

@timestamper # 1
def generic_funct(*args, **kwargs): #9
    print(f'{generic_funct.__name__} called with args {args} and kwargs {kwargs}.') #10

generic_funct('a', 'b', exec=True)