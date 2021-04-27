class WarehouseDecorator:

    def __init__(self, material):
        self.material = material

    def __call__(self, func_to_dec):
        def internal_wrapper(*args, **kwargs):
            print(f'Wrapping books: {args}, in material: {self.material}')
            print(f'Calling {func_to_dec.__name__}, with args {args} and kwargs {kwargs}')
            func_to_dec(*args, **kwargs)
            print('Finished!')
        return internal_wrapper

@WarehouseDecorator('Bubble-Wrap')
def pack_books(*args):
    print(f'Packing books: {args}')

pack_books('alice', 'catinhat')