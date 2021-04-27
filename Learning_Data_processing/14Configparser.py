                            #### CONFIGPARSER ####

# Currently, many popular services provide an API that we can use in our applications. Integration with these services requires 
    # authentication using data such as a login and password, or simply an access token.

# Each service may require different data for authentication, but one thing is certain – we need to store it somewhere in our 
    # application. It's not a good idea to hardcode them directly in the code.

# A better solution is to use the configuration file, which will be read by the code. In Python, this is possible thanks to a 
    # module called configparser.

# The configparser module is available in the Python standard library. To start using it, we need to import the appropriate module:


    # WHAT DOES THE CONFIGURATION FILE LOOK LIKE? #
# The structure of the configuration file is very similar to Microsoft Windows INI files. It consists of sections that are identified 
    # by names enclosed in square brackets. The sections contain items consisting of key value pairs. Each pair is separated by a 
    # colon : or equals sign =.

'''
[DEFAULT]
host = localhost # This is a comment.

[mariadb]
name = hello
user = user
password = password

[redis]
port = 6379
db = 0
'''

# Our configuration file contains the DEFAULT, mariadb and redis sections.

# The DEFAULT section is slightly different because it contains the default values that can be read in the other sections of the file. 
    # In our case, there's a common host for all sections.
# The second section called mariadb stores the data necessary to connect to the MariaDB database. 
    # These are the database name, username, and password.
# The last section contains Redis configuration data, consisting of the port and database number. In addition, both in this section and 
    # in the mariadb section, we have access to the host option defined in the DEFAULT section. In a moment, you'll learn how to read 
    # this data using the configparser module.

# NOTE: The whitespace at the beginning and end of keys and values is removed.


    # PARSING THE CONFIGURATION FILE #

import configparser

config = configparser.ConfigParser()
print(config.read('config.ini'))

print('Sections:', config.sections(),'\n')

print('mariadb section:')
print('Host:', config['mariadb']['host'])
print('Database:', config['mariadb']['name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', int(config['redis']['port']))
print('Database number:', int(config['redis']['db']))



# Accessing the data contained in the config file is not difficult.
# We can use the sections() method.
    # DEFAULT does not get printed by the .sections() method, this is default behaviour of the .sections method.
# once we have the configparser.ConfigParser() object, we can acess the data using named indexing.
    # <config['mariadb']['host']> <<< Will return 'host' data at section 'mariadb'.

# Despite the fact that the DEFAULT section is omitted as a result of the sections method, we still have access to its options. 
    # Both the mariadb and redis sections can read the host option.
# Its also possible to access the values stored in the options by using the get method. The get method requires the section name 
    # and key to be passed. This is what it looks like in practice:
        # print('Host:', config.get('mariadb', 'host')) 
        # print('Host:', config['mariadb']['host'])


config = configparser.ConfigParser()

dict = {
    'DEFAULT': {
        'host': 'localhost'
    },
    'mariadb': {
        'name': 'hello',
        'user': 'root',
        'password': 'password'
    },
    'redis': {
        'port': 6379,
        'db': 0
    }
}

config.read_dict(dict)       # read_dict() accepts a dictionary whose keys are section names, while the values include 
                                         # dictionaries containing keys and values.

print('Sections:', config.sections(),'\n')

print('mariadb section:')
print('Host:', config['mariadb']['host'])
print('Database:', config['mariadb']['name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', int(config['redis']['port']))
print('Database number:', int(config['redis']['db']))


# NOTE: The configparser module also has read_file and read_string methods that allow you to read the configuration from an open 
    # file or string. You can find more information about these methods in the documentation.


    # CREATING A CONFIGURATION FILE #
# To create a configuration file, you should treat the ConfigParser object as a dictionary. 
# Creating a configuration file is as easy as parsing it. If you know how to work with dictionaries, it's a piece of cake.

config = configparser.ConfigParser()

config['DEFAULT'] = {'host': 'localhost'}
config['mariadb'] = {'name': 'hello',
                     'user': 'root',
                     'password': 'password'}
config['redis'] = {'port': 6379,
                   'db': 0}

with open('config.ini', 'w') as configfile:
    config.write(configfile)

# ouput:
# config.ini gets re-written with new values passed to config['<section_name>']

# A configuration loaded using the read method can also be modified. To change a single option, simply set the new value to the 
    # appropriate key, and then save the file using the write method:

config = configparser.ConfigParser()
config.read('config.ini')

config['redis']['db'] = '1'

with open('config.ini', 'w') as configfile:
    config.write(configfile)


    # INTERPOLATING VALUES #
# The big advantage of the configuration file is the possibility of using interpolation. It allows you to create 
    # expressions consisting of a placeholder under which the appropriate value will be substituted.
'''
[DEFAULT]
host = localhost

[mariadb]
name = hello
user = user
password = password

[redis]
port = 6379
db = 0
dsn = redis://%(host)s
'''
# The configuration file has been extended with another option called dsn. Its value contains the placeholder %(host)s, 
    # which needs to be replaced by an appropriate value.
# Placing any key between % and s informs the parser of the need to interpolate. Of course, all the work is done for us, 
    # and we only get the ready results.
# For the dsn option, it'll be the following string: redis://localhost. Note that the placeholder %(host)s has been 
    # replaced by the value stored in the host option.

print('Interpolating values'.upper())