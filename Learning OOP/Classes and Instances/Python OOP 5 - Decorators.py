
##### Non-OOP, using a wrapper #####

def decorator_function(origional_function):
    def wrapper_function(*args, **kwargs):
        print(f'Wrapper run before {origional_function.__name__}') 
        return origional_function(*args, **kwargs)
    return wrapper_function

# Decorators are essentially doing this:
#    display = decorator_function(display)

##### Object-style, using a class with __init__ and __call__ methods

class decorator_class(object):
    def __init__(self, origional_function):
        self.origional_function = origional_function

    def __call__(self, *args, **kwargs):
        print(f'class run before {self.origional_function.__name__}') 
        return self.origional_function(*args, **kwargs)
#####

#@decorator_function
@decorator_class
def display():
    print('display function run')

#@decorator_function
@decorator_class
def display2(name, age):
    print(f'Your name is {name}, your age is {age}.')

display2('Jeff', 21)