class Logging_decorator(object):
    def __init__(self, origional_function):        
        self.origional_function = origional_function

    def __call__(self, *args, **kwargs):
        import logging
        logging.basicConfig(filename=f'{self.origional_function.__name__}.log', level=logging.INFO)
        logging.info(f'Program: {self.origional_function.__name__}. Ran with args: {args}, and kwargs: {kwargs}. ')
        return self.origional_function(*args, **kwargs)

@Logging_decorator
def display2(name, age):
    print(f'Your name is {name}, your age is {age}')

display2('Jeff', 21)