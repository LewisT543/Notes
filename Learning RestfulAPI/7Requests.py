                        #### REQUEST MODULE ####

# The HTTP protocol operates by using methods. We can say that the HTTP method is a two-way interaction between the client 
    # and the server (note: the client initiates the transmission) dedicated to the execution of a certain action.
# GET is one of them, and is used to convince the server to transfer some resources asked for by the client.
# A requests function named get() initiates execution of the HTTP GET method and receives the server's response.
# As you can see, the code is extremely simple and compact – we don't need to cope with a myriad of mysterious constants, symbols, functions, and notions.
'''
import requests

reply = requests.get('http://localhost:3000')
print(reply.status_code)
'''
#output:
# 200

# The only details we need to provide are the server’s address and the service port number - just like we did while using 
    # the browser’s address line. Note: the port number can be omitted if it is equal to 80, HTTP’s default port.
# As you can see, the get() function returns a result. It’s an object containing all the information describing the GET method’s execution.
# Of course, the most important thing we need to know is whether the GET method has succeeded. This is why we make use of the status_code 
    # property – it contains a standardized number describing the server’s response.

import requests

print(requests.codes.__dict__)
# output: Outputs all status_codes.

 # Anyway, you can use the codes property to test status codes in a more verbose way than by comparing them to bare integer values. 
    # What do you think about such a snippet?
    # if reply.status_code == requests.codes.ok:
    # Seems a bit more solid than checking it against 200.

# When you know that the server's response is correct, you would like to know the response itself, wouldn’t you?
# The server's response consists of two parts: the header and the contents. Both parts have their representation in the object returned 
    # by the get() function. Let's start with the header.
    # The response's header is stored inside the property named headers (it's a dictionary). Let's take a look at it:

reply = requests.get('http://localhost:3000')
print(reply.headers)
# Returns a big dictionary of all headers returned from a request.

# Most of them aren't of any interest to us, although some are crucial, 
    # e.g., Content-Type, which describes what the server response's contents really are.

print(reply.headers['Content-Type'])

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

#### THE TEXT PROPERTY ####
# The text property contains the response's content.

print(reply.text)

#output:
# CARS DATABASE (contents of my index.html page)

# NOTE: The property contains bare text taken as-is directly from the data stream, hence it is just a string. No conversions are applied.
# NOTE: Note: when both client and server are aware of the fact that the contents (no matter which part sent them) contain a JSON message, 
    # it is also possible to use a method named json() which returns exactly what we may expect – a dictionary or a list of dictionaries.

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

#### HTTP PROTOCOL METHODS ####
# In general, the HTTP protocol defines the following methods:

# GET METHOD # 
# GET is intended to fetch a piece of information (a resource) from the server; of course, a simple server offers more than one resource, 
    # so the GET method has the means of enabling the client to precisely specify its demands; if the client has no demands and initiates 
    # GET without resource identification, the server's answer will contain the root document – this is exactly what we saw some time ago, 
    # when our own server sent us this simple text CARS DATABASE.
# in other words – if you want the server to give you something, GET is the way to ask for it.

# POST METHOD #
# POST, like GET, is used to transfer a resource, but in the opposite direction: from the client to the server; just like in GET, the 
    # identification of the resource has to be given (the server wants to know what to name the piece of information it has received); it is also 
    # assumed that the resource the client sends is new to the server – it doesn't replace or overwrite any of the previously collected data;
# to make a long story short – if you want to give the server something new, POST is ready to be your deliverer.

# PUT METHOD #
# PUT, similarly to POST, transfers a resource from the client to the server, but the intention is different – the resource being sent is 
    # intended to replace the previously stored data;
# simply put – if you want to update something that the server is currently keeping, PUT will know the way.

# DELETE METHOD #
# DELETE – this name leaves no doubt: it is used to order the server to remove a resource from a given identification; the resource is 
    # unavailable from then on;

# OTHER METHODS #
# HEAD
# CONNECT
# OPTIONS
# TRACE

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# REQUEST VERSIONS OF HTTP METHODS:
    # The Requests module holds a python viable version of each of these methods.

# requests.get('http://server/service/existingdata')
# requests.post('http://server/service/newdata')
# requests.put('http://server/service/updatedata')
# requests.delete('http://server/service/deletedata')

# So what happens if one of these methods goes wrong?
# All requests functions are in the habit of raising an exception when they encounter any kind of communication problem, 
    # although some of the problems seem to be more common than others.

# <><><><><> #

    # TIMEOUT # 
# It's normal for the server not to respond immediately. But usually, we know very well how long we agree to wait 
    # and don't want to wait any longer. Can our expectations be met?
# yes...an Example:

try:
    reply = requests.get('http://localhost:3000', timeout=1) # timeout in 1 second
except requests.exceptions.Timeout:
    print('Sorry, Mr. Impatient, you didn\'t get your data')
else:
    print('Here is your data, my Master!')

# As you can see, the get() function takes one additional argument named timeout – it's the maximum time 
    # (measured in seconds and expressed as a real number) we agree to wait for a server's response. If the time is exceeded, 
    # get() will raise an exception named:
        # requests.exceptions.Timeout.

# <><><><><> #

    # CONNECTION ERROR #
# Of course, problems may appear much earlier, e.g., while establishing the connection:

try:
    reply = requests.get('http://localhost:3001', timeout=1)
except requests.exceptions.ConnectionError:
    print('Nobody\'s home, sorry!')
else:
    print('Everything fine!')

#output:
# Nobody's home, sorry!

# This code has no chance of running properly – it’s addressing its efforts to port 3001, while our server is listening at port 3000. 
    # No helping hand will fix this misunderstanding – client and server won't meet and an exception will be raised. Its name is:
        # requests.exceptions.ConnectionError

# <><><><><> #

    # INVALID-URL ERROR #
# Disasters of the URL variety raise an exception called: 

try:
    reply = requests.get('http:////////////')
except requests.exceptions.InvalidURL:
    print('Recipient unknown!')
else:
    print('Everything fine!')

#output:
# Recipient unknown!

# Entering a dud URL will raise this exception:
    # requests.exceptions.InvalidURL

# <><><><><> #

    # A LIST OF ALL REQUESTEXCEPTIONS #

# Heres one I prepared earlier:
'''
RequestException
|___HTTPError
|___ConnectionError
|   |___ProxyError	
|   |___SSLError	
|___Timeout
|   |___ConnectTimeout
|   |___ReadTimeout
|___URLRequired
|___TooManyRedirects
|___MissingSchema
|___InvalidSchema
|___InvalidURL
|   |___InvalidProxyURL
|___InvalidHeader
|___ChunkedEncodingError
|___ContentDecodingError
|___StreamConsumedError
|___RetryError
|___UnrewindableBodyError
'''

