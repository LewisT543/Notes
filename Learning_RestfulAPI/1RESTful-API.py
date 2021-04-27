                        #### INTRODUCTION ####

# After completing this course you will know:
    # the basic concepts of network programming, REST, network sockets, and client-server communication;
    # how to use and create sockets in Python, and how to establish and close the connection with a server;
    # what JSON and XML files are, and how they can used in network communication;
    # what HTTP methods are, and how to say anything in HTTP;
    # how to build a sample testing environment;
    # what CRUD is;
    # how to build a simple REST client, and how to fetch and remove data from server, add new data to it, 
        # and update the already-existing data.

# REST stands for:
    # RE presentational
    # S tate
    # T ransfer

# Representational
    # RE stands for Representational. It means that our machinery stores, transmits and receives representations, while the term 
    # representation reflects the way in which data or states are retained inside the system and presented to the users.
    # REST uses a very curious way of representing its data - it's always text. Pure, plain text.
    # REST is focused on a very specific kind of data - the data which reflects states.

# State
    # S stands for State. The word state is key to understanding what REST is and what it could be used for.
    # Imagine any object. The object contains a set of properties. We can say that the values of all the object's properties constitute its state.
    # If any of the properties changes its value, this inevitably entails the effect of changing the whole object's state. 
        # Such a change is often called a transition.
    # Imagine you want to affect an object's state through the network. No, you are not able to invoke any of its methods. Sorry, that's impossible. 
        # You can't do it directly. But you can do it using REST

# Transfer
    # T stands for Transfer. The network is able to act as a carrier allowing you to transmit states' representations to and from the server.
    # Note: not the object, but its states, or actions able to change the states, are subject to the transfer. 

# REST = REPRESENTATIONAL STATE TRANSFER