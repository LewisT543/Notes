                            #### IMPLEMENTING CRUD FOR A BASIC CARS DATABASE ####

#### READING ####
import requests

try:
    reply = requests.get('http://localhost:3000/cars')
except requests.RequestException:
    print('Communication Error')
else:
    if reply.status_code == requests.codes.ok:
        print(reply.text)
    else:
        print('Server-Error')

# This allows us to read everything off of the server / database
# The HTTP server is able to transfer virtually any kind of data: text, image, video, sound, and many others.
# how do we recognize that we’ve actually got the JSON message?

# The server response's header contains a field named Content-Type. The field's value is analyzed by the requests 
    # module, and if its value announces JSON, a method named json() returns the string containing the received message.

try:
    reply = requests.get('http://localhost:3000/cars')
except requests.RequestException:
    print('Communication Error')
else:
    if reply.status_code == requests.codes.ok:
        print(reply.headers['Content-Type'])
        print(reply.json())
    else:
        print('Server-Error')

# NOTE: The line starting with application/json – this is a premise used by the requests module to diagnose the response's contents.

    # Reading RAW Json data #

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    for car in json:
        show_car(car)


try:
    reply = requests.get('http://localhost:3000/cars')
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    else:
        print('Server error')

# Okay so this isnt bad... but its not pandas...

    # Specific GET requests #
# Pointing to a specific id in the database will return the object at that location. In this case id=2
    
    # reply = requests.get('http://localhost:3000/cars/2') 

# all we need to change from above is adding:
    # elif reply.status_code == requests.codes.not_found:
        # print("Resource not found")


# A particular server may manipulate data before sending it to the client. The json-server is able to sort the 
    # items using any of the properties as a sort key (by default, it sorts items by their ids).
# The json-server assumes that a URI formed in the following way:
    # http://server:port/resource?_sort=property

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


try:
    reply = requests.get('http://localhost:3000/cars?_sort=production_year') # Sorts by production year in an Ascending order.
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')

# NOTE: in order to reverse the order we can write the URL as such:
    # http://server:port/resource?_sort=property&_order=desc
    # Notice the ?_ used to signify the end of the identifier and the start of an extra option
    # we then see &_ used to signify the end of the sort-type
    # order=desc will give us descending results

#### Server tings ####
# By default, a server implementing HTTP version 1.1 works in the following manner:
    # - it waits for the client's connection;
    # - it reads the clients response;
    # - it sends its response;
    # - it keeps the connection alive, waiting for the client's next request
    # - if the client is innactive for some time, the server silently closes the connection; this means that the client is obligued
        # to open a new connection if it wants to send another request

# The server informs the client whether the connection is kept or not by using a field named Connection placed in the responses header.
    # HTTPv1.1 DEFAULT = Connection=keep-alive
    # close means that the server is going to close the connection as soon as the response is fully transmitted 
        # (this was the server’s default behavior in HTTP 1.0).
# If the client knows that it won't bother the server with subsequent requests for some time, it may encourage the server to temporarily 
    # change its habits and close the connection immediately. It will conserve the server's resources.  
    # How do we do that?...

#### DELETING ####
# 1. we'll ask the server to delete one car of a specified id knowing that the server will keep the connection alive;
# 2. we’ll ask the server to present the current contents of the offer while suggesting that the connection should be closed immediately 
    # after the transmission.

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


headers = {'Connection': 'Close'} # Setting up our 'Close' behaviour for Connection property
try:
    reply = requests.delete('http://localhost:3000/cars/7') # Delete the car with ID=7
    print("res=" + str(reply.status_code))      # Should return 'res=200' if deletion was successful
    reply = requests.get('http://localhost:3000/cars/', headers=headers) # headers=headers is us updating the {'Connection': 'Keep-alive'} to
except requests.RequestException:                                              # {'Connection': 'Close'} (server will close after transaction)
    print('Communication error')
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')

#### CREATING ####
# 1). we add json to the import list, we will need it to make textual representations of the new item/car.

import json

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


h_close = {'Connection': 'Close'}
h_content = {'Content-Type': 'application/json'}
new_car = {'id': 7,
           'brand': 'Porsche',
           'model': '911',
           'production_year': 1963,
           'convertible': False}
print(json.dumps(new_car)) # Shows the newly created object in JSON format
try:
    reply = requests.post('http://localhost:3000/cars', headers=h_content, data=json.dumps(new_car)) 
    # Significant line: 1). URL points to the resource, not a particular item. 
                      # 2). headers=h_content, update the Content-Type header to make sure the server knows its recieving something 
                            # that isnt a regular request
                      # 3). data=json.dumps(new_car) is the JSON message being passed to the server.
    
    print("reply=" + str(reply.status_code))             # Reply=201 - This means it worked, 201 is the code for 'Created'.
    reply = requests.get('http://localhost:3000/cars/', headers=h_close)
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')


#### UPDATING ####

# The last remaining letter is U, so now we'll update one of the existing items.
# Updating an item is actually similar to adding one.

import requests, json

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


h_close = {'Connection': 'Close'}
h_content = {'Content-Type': 'application/json'}
car = {'id': 6,
       'brand': 'Mercedes Benz',
       'model': '300SL',
       'production_year': 1967,
       'convertible': True}
try:
    reply = requests.put('http://localhost:3000/cars/6', headers=h_content, data=json.dumps(car)) # Points directly to item being updated
    print("res=" + str(reply.status_code))                                                        # almost same format as creating a new entry
    reply = requests.get('http://localhost:3000/cars/', headers=h_close)
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')