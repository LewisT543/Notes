                            #### JSON ####

# JSON stands for:
    # Java...
    # ...Script
    # Object
    # Notation

# Thankfully it is not only JavaScript we can use this kind of notation for. It works as a framework for data transfer regardless of language used.
# JSON is the answer to quite a basic need – the need to transfer data that is the content of an object or set of objects. 
    # The mechanism which solves it should be portable and platform independent.
# The problem we need to struggle with is how to represent an object (understood as a set of data of different types, including other objects)
    # or even a single value in a way that can survive network transfers and inter-platform conversions.
# JSON solves the problem using two simple tricks:
    # it uses UTF-8 coded text – this means that no machine/platform-dependent formats are used; it also means that the data JSON carries is readable 
        # (poorly, but always readable) and comprehensible by humans;
    # it uses a simple and not very expanded format (we can call it syntax, or even grammar) to represent mutual dependencies and relations between different 
        # parts of objects, and is able to transfer not only the values of objects’ properties, but also their names.
# If you want to transfer not only raw data but also all the names bound to it (like the way in which objects hold their properties), 
    # JSON offers a syntax which looks like a close relative of Python's dictionary, which is, in fact, a set of key:value pairs. Making 
    # such an assumption leads us to the following question – can we use Python's syntax to code and decode network messages in REST?

# This is how JSON comes to this:
# { "prop": 2.78 }

#### JSON INTEGER LITERALS ####
# JSON's integer literals use some different tricks to those of Python.
# JSON knows nothing about numbers written using radices different to 10, so literals like these:
    # 0x10
    # 0o10
    # 0b10... wont be recognised in a JSON environment. 
# A minus sign at the front makes a number negative.
# NOTE: Don't use leading zeros!!

#### JSON STRINGS ####
# JSON strings may look familiar, but there is one important difference – you must not use apostrophes to delimit the text. 
    # The only delimiter allowed is a quote, like here:
        # "Python"
    # This means that you can’t just insert a quote inside the string – you have to use our old friend backslash (\) followed by a quote instead.
        # "\"Monty Python's\""

# JSON strings cannot be split over multiple lines – each string must fit entirely on one line

#### BOOLEANS ####
# Boolean values: true, false (LOWER CASE ONLY)

#### null ####
# null: Same as pythons None. Representing a lack of value or meaning.

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> # 

# In JSON, all the above values may be combined (or packed) in two ways:
    # inside arrays (which are a very close relative to Python lists);
        # array = []
    # inside objects (which resemble Python dictionaries more than objects)
        # object = {}
        # name:value

# In this approach, a JSON object is a set of property specifications separated by commas.
# Example:
'''
    { me: "Python",
	pi: 3.141592653589,
	parsec: 3.0857E16, 
	electron: −1.6021766208E−19
	friend: "JSON",
	off: true,
	on: false,
	set: null }
'''
# Example with arrays:
'''
    {ob:{ar:["a", 1, 3.14, false]}}
    '''


#### WORKING WITH THE JSON LIBRARY IN PYTHON ####

# the first JSON module's power is the ability to automatically convert Python data (not all of it and not always) into a JSON string. 
    # If you want to carry out such an operation, you may use a function named dumps().

# json.dumps() example:
import json

# Literals
electron = 1.602176620898E10-19
print(json.dumps(electron))
#output:
# 16021766189.98

# Strings
comics = '"The Meaning of Life" by Monty Python\'s Flying Circus'
print(json.dumps(comics))
#output:
# "\"The Meaning of Life\" by Monty Python's Flying Circus"

# Lists
my_list = [1, 2.34, True, "False", None, ['a', 0]]
print(json.dumps(my_list))
#output:
# [1, 2.34, true, "False", null, ["a", 0]]

# NOTE: what will happen if we use a tuple instead of a list? The answer is predictable – nothing. As JSON cannot distinguish 
    # between lists and tuples, both of these are converted into JSON arrays.

my_dict = {'me': "Python", 'pi': 3.141592653589, 'data': (1, 2, 4, 8), 'set': None}
print(json.dumps(my_dict))
#output:
# {"me": "Python", "pi": 3.141592653589, "data": [1, 2, 4, 8], "set": null}

# JSON has a set of data rules to build JSON messages from native data:
    # Python Data       JSON element
    # dict              object
    # list/tuple        array
    # string            string
    # int/float         number
    # True/False        true/false
    # None              null

# This looks great, however...

# Example of issue:

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


some_man = Who('John Doe', 42)
try:
    print(json.dumps(some_man))
except TypeError:
    pass

#output:
# TypeError: Object of type 'Class' is not JSON serializable

# We clearly cannot just dump an entire object into JSON format. We must encode it before trying to dump it.
# There is a somewhat dirty trick that allows us to dump an object using its __dict__ property content. This will work, but we expect more.

# We have at least 2 options here:
# First Option - SUBSTITUTE DUMPS() # 
    # step 1). Substitute dumps() for your own function that knows how to handle your objects;
    # step 2). make dumps() aware of it by setting the keyword argument named default;

# Example:

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')


some_man = Who('John Doe', 42)
print(json.dumps(some_man, default=encode_who))

#output:
# {"name": "John Doe", "age": 42}

# NOTE: raising a TypeError exception is obligatory – this is the only way to inform dumps() that your function isn't able to 
    # convert objects other than those derived from the class Who.

# The second approach - OVERLOADING JSON.JSONENCODER CLASS #
# ...is based on the fact that the serialization is actually done by the method named default(), which is a part of the json.JSONEncoder class
# It gives you the opportunity to overload the method defining a JSONEncoder's subclass and to pass it into dumps() 
    # using the keyword argument named cls

# Example:

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    # Overloading the json.JSONEncoder
    def default(self, w):
        if isinstance(w, Who):
            # If instance of Who >>> use w.__dict__
            return w.__dict__
        else:
            # If not an instance of Who >>> use typical json.JSONEncoder.default() method
            return super().default(self, z)


some_man = Who('John Doe', 42)
print(json.dumps(some_man, cls=MyEncoder))
#output:
# {"name": "John Doe", "age": 42}

#### DESERIALISATION ####
# We know about turning python data into JSON data, but not very much about turning JSON data back into python data.
# The function that can do this for us is called loads().
    # It takes a string, hence the s in loads() 

    #### LOADS() with LITERALS
# This is how it goes:

jstr = '16021766189.98'
electron = json.loads(jstr)
print(type(electron))
print(electron)

#output:
# <class 'float'>
# 16021766189.98

    #### LOADS() with STRINGS
# The loads function can cope with strings too:

jstr = '"\\"The Meaning of life\\" by Monty Python\'s flying circus"'
# Double backslashes are completely neccessary, the string delivered to loads() must be a COMPLETE JSON string. This means that the backslash
    # must precede all quotes existing within the same string. Removing any of them will make the string invalid and loads() will have a meltdown.
comics = json.loads(jstr)
print(type(comics))
print(comics)

#output:
# <class 'str'>
# "The Meaning of life" by Monty Python's flying circus


    #### LOADS() with LISTS
# loads() works just the same with lists too.

jstr = '[1, 2.34, true, "False", null, ["a", 0]]'
my_list = json.loads(jstr)
print(type(my_list))
print(my_list)

#output:
# <class 'list'>
# [1, 2.34, True, 'False', None, ['a', 0]]


    #### LOADS() with OBJECTS
# objects >>> python dicts

json_str = '{"me":"Python","pi":3.141592653589, "data":[1,2,4,8],"friend":"JSON","set": null}'
my_dict = json.loads(json_str)
print(type(my_dict))
print(my_dict)

#output:
# <class 'dict'>
# {'me': 'Python', 'pi': 3.141592653589, 'data': [1, 2, 4, 8], 'friend': 'JSON', 'set': None}


# NOTE: Our tests show that the table we presented before works successfully in both directions. There’s only one specific 
    # difference: if a number encoded inside a JSON string doesn't have any fraction part, Python will create an integer 
    # number, or a float number otherwise.

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

#### DESERIALISING JSON 
# But what about Python's objects – can we deserialize them in the same way as we performed the serialization?
# As you can see, there’s a keyword argument name object_hook, which is used to point to the function responsible for creating a brand new 
    # object of a needed class and for filling it with actual data.
# example:

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + 'is not JSON serializable')


def decode_who(w):
    return Who(w['name'], w['age'])


old_man = Who("Jane Doe", 23)
json_str = json.dumps(old_man, default=encode_who)
new_man = json.loads(json_str, object_hook=decode_who) # THIS LINE HERE 
print(type(new_man))
print(new_man.__dict__)

#output:
# {'name': 'Jane Doe', 'age': 23}

# NOTE: the decode_who() function receives a Python entity, or more specifically – a dictionary. As Who's constructor 
    # expects two ordinary values, a string and a number, not a dictionary, we have to use a little trick – we've employed 
    # the double * operator to turn the directory into a list of keyword arguments built out of the dictionary's key:value pairs.
# NOTE: the function, specified by the object_hook will be invoked ONLY when the JSON string describes a JSON object.

#### DESERIALISING JSON - OBJECT APPROACH ####
# A purer object approach is also possible, and is based on redefining the JSONDecoder class.
# We don't need to rewrite any method, but we do have to redefine the superclass constructor, which makes our job a little more painstaking.
# The new constructor is intended to do just one trick – set a function for object creation.

# Example:

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    # Custom encoder from earlier ^^^^^ see above
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, z)


class MyDecoder(json.JSONDecoder):
    # Notice this inherits from json.JSONDecoder
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        # **d turns d into an unpacked list of keyword arguments (think similar to **kwargs)
        return Who(**d)


some_man = Who('Jane Doe', 23)
json_str = json.dumps(some_man, cls=MyEncoder)
new_man = json.loads(json_str, cls=MyDecoder)

print(type(new_man))
print(new_man.__dict__)

#ouput:
# <class '__main__.Who'>
# {'name': 'Jane Doe', 'age': 23}