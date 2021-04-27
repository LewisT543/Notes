                        #### JSON-SERVER ####

# Use NODE.JS and JSON-SERVER to create a server environment

# We know JSON
# We know Sockets
# We know about web connections. Lets put it all together.

# We need a server serving a web service... And a tool simpler than socket to communicate with the server. (socket is too verbose for this)

# We need our own, private HTTP server which will work only for us and successfully play the role of a RESTFul API foundation.

# Node.JS and json-server have been installed.
    # json-server --watch cars.json
    # This means the server is ready to server incoming connections.

# Now open your favorite Internet browser and type the following URL into the address line:
    # http://localhost:3000
# This means we are now connected to the same CPU we are working on (localhost) on port number 3000 (json-server's default port)
# Press Crtl-C in the console if you want to terminate the server.
