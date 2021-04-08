                            #### HOW TO FETCH A DOCUMENT FROM A SERVER USING PYTHON ####

# Here are our goals:
    # we want to write a program which reads the address of a WWW site (e.g., pythoninstitute.org) using the standard input() 
        # function and fetches the root document (the main HTML document of the WWW site) of the specified site;
    # the program outputs the document to the screen;
    # the program uses TCP to connect to the HTTP server.

# Our program has to perform the following steps:
    # 1). create a new socket able to handle connection-oriented transmissions based on TCP;
    # 2). connect the socket to the HTTP server of a given address;
    # 3). send a request to the server (the server wants to know what we want from it)
    # 4). receive the server's response (it will contain the requested root document of the site)
    # 5). close the socket (end the connection)


# Obtaining user input
# We also need the name of the HTTP server we're going to connect to. In fact, it's not our problem. 
# The user knows it better. Let's ask him or her:
# The user input may can take two different forms:
    # it can be the domain name of the server (like www.pythoninstitute.org, but without the leading http://)
    # it can be the IP address of the server (like 87.98.235.184), but it must be said firmly that this variant is potentially ambiguous. 
        # Why? Because there can be more than one HTTP server located at the same IP address - 
        # the server you will reach may be not the server you intended to connect to.
'''
import socket

server_addr = input("What server do you want to connect to? ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''
# AF_INET = specify the Internet socket domain
# SOCK_STREAM = the latter argument is a socket type code (we may use the SOCK_STREAM symbol here to specify a high-level socket able 
    # to act as a character device - a device that can handle single characters, as we are interested in transferring data byte by byte, 
    # not as fixed sized blocks (e.g., a terminal is a character device, while a disk isn't)
# Such a socket is prepared to work on top of TCP protocol - it's the default socket configuration.
# If you want to create a socket to cooperate with another protocol, like UDP, you will need to use a different constructor syntax.

# Connecting to a server
# If we use a socket on the client's side, we are ready to make use of it. The server, however, has a few more steps to take.
# In general, servers are usually more complex than clients (as one server serves many clients simultaneously)

# The connect() method does what it promises - it tries to connect your socket to the service of the specified address and port (service) number.
'''sock.connect((server_addr, 80))'''

# NOTE: we make use of the variant where the two values are passed to the method as a 2 element tuple.
# NOTE: the form of the target service address (a pair consisting of the actual address and port number) 
    # is specific for the INET domain. Don't expect it to look the same in other domains.

# Why Port:80? 80 is a well-known service number for HTTP. Any browser will try and connect to 80, so we should too.

# If something goes wrong, the connect() method (and any other method whose results may be unsuccessful) RAISES AN EXCEPTION.
# But... what do we really want to tell the server anyway? 
# How do we talk to the HTTP server to be sure that it understands us? We have to speak in HTTP, of course.

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> # 

#### THE GET METHOD ####
# The HTTP protocol is one of the simplest Internet protocols
# A conversation with the HTTP server consists of requests (sent by the client) and responses (sent by the server).
# HTTP defines a set of acceptable requests - these are the request methods or HTTP words. The method asking the server to send a 
    # particular document of a given name is called GET (it's rather self-explanatory, isn't it?).
# To get a root document from a site named www.site.com the client should send the request containing a correctly formed GET method description:


# A GET Request
'''
GET / HTTP/1.1\r\n
Host: www.site.com\r\n
Connection: close\r\n
\r\n

'''

# The GET method requires:
    # a line containing the method name (i.e., GET) followed by the name of the resource the client wants to receive; the root document is 
        # specified as a single slash (i.e., /); the line must also include the HTTP protocol version (i.e., HTTP/1.1) and must end with the 
        # characters \r\n; note: all lines must end the same way;
    # a line containing the name of the site (e.g., www.site.com) preceded by the parameter name (i.e., Host:)
    # a line containing a parameter named Connection: along with its value close, which forces the server to close the connection after the 
        # first request is served; it will simplify our client's code;
    # an empty line is a request terminator.

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> # 

#### THE SEND METHOD ####

'''
sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")
'''

# The send() method doesn't natively accept strings - this is why we have to use the b prefix before the literal parts of the request string.
    # This allows us to silently translate the string into bytes (the 'send' method's favourite.)
    # and is also why we should invoke bytes() to translate the string variable in the same manner.
# NOTE: the bytes' second argument specifies the encoding used to store the server's name. UTF8 seems to be the best choice for most modern OSs.
# The action performed by the send() method is extremely complicated - it engages not only many layers of the OS, but also lots of network 
    # equipment deployed on the route between the client and server, and obviously the server itself.
# Of course, if anything inside this complex mechanism fails, SEND WILL FAIL, too. As you may expect, an EXCEPTION is RAISED then.

# EXAMPLE:
'''
import socket

server_addr = input("What server do you want to connect to? ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_addr, 80))
sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")
reply = sock.recv(10000)
'''
# The recv() method waits for the server's response, gets it, and puts it inside a newly created object of type bytes.
    # The argument specifies the maximum acceptable length of the data to be recieve. If the server's response is longer than this limit, 
        # it will remain unreceived.
    # You will need to invoke recv() again (maybe more than once) to get the remaining part of the data. 
        # It's a general practice to invoke recv() as long as it returns some data.

#### CLOSING THE CONNECTION #### 

# we can close the connection using socket.shutdown()
    # we can pass argument socket.SHUT_RD to declare we will not read any more of the servers messages
    # we can pass argument socket.SHUT_WR to declare we will not weite anymore messages to the server.
    # we can pass argumrnt socket.SHUT_RDWR to specify both of the above.

'''
sock.shutdown(socket.SHUT_RDWR)
sock.close()
'''

# As our GET request demanded that the server close the connection as soon the response is sent and the server has 
    # been advised of our next steps (or rather of the fact that we've already done what we wanted to), we can assume 
    # that the connection is fully terminated at this moment.

# In order to check what we have recieved in our request, we can use the repr() method to represent the object.
    # using: print(repr(recieved_request))


import socket

server_addr = input("What server do you want to connect to? ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_addr, 80))
sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")
reply = sock.recv(10000)
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(repr(reply))

# Returns...
'''
b'HTTP/1.1 200 OK\r\nDate: Mon, 08 Mar 2021 18:32:33 GMT\r\nExpires: -1\r\nCache-Control: private, max-age=0\r\nContent-Type: text/html; charset=ISO-8859-1\r\nP3P: CP="This is 
not a P3P policy! See g.co/p3phelp for more info."\r\nServer: gws\r\nX-XSS-Protection: 0\r\nX-Frame-Options:...........etc, etc
'''
# We see two parts of the response:
    # the first line is the response header, the topmost line is the most important, as is says whether the server 
        # sent back the requested document or not. At the start there is a very significant three-digit number: 200
        # 200 is the status code for <ALL OKAY>, so checking to see if the first line contains 200 is a good place to start.
    # the second part is the document, relatively bloated and very messy to parse through it.

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> # 

#### WHAT CAN GO WRONG ####
    # Malformed or non-existent address:
        # The connection function throws an exception named socket.gaierror. Its name comes from a low-level function called getaddrinfo().
        # (connect() also uses getaddrinfo() to marshal a connection to a server.)
            # socket.gaierror: [Errno -2] Name or service not known
        # NOTE: socket.gaierror covers more than one possible reason for the failure.
            # the two examples shown here are:
                # 1). the address is syntactically correct but doesn't correspond to any existing server
                # 2). the address is obviously malformed
            # It is also possible that a server of a specified address exists and it is working but doesn't provide the desired service. 
                # for example, a dedicated mail server may not respond to the connections addressed to port number 80. 
                # Trying to connect to a server using the wrong service will throw a ConnectionRefusedError
    
    # The Socket.timeout exception
        # This exception is raised when the server's reaction doesn't occur in a reasonable time - the length of our patience can be set 
            # using a method named settimeout()
        # If you really want to induce such an exception, you'll have to do something naughty like break the network connection in the middle 
            # of a transfer, or shut down the server at a precisely chosen moment. You should probably not do these things...
