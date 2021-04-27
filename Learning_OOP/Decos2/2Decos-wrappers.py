def warehouse_decorator(material): #1
    def wrapper(our_function): #3
        def internal_wrapper(*args): #5
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material)) #6
            our_function(*args) #7
            print('finish') #10
        return internal_wrapper #4
    return wrapper #2


@warehouse_decorator('kraft')
def pack_books(*args): # 8
    print("We'll pack books:", args) #9


@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


@warehouse_decorator('film')
def pack_things(*args):
    print('Packing:', args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
pack_things('log', 'brick', 'postman')