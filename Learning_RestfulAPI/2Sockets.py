                        #### BSD SOCKETS ####

# A socket is a kind of end-point, a point where the data is available to get it from and where the data may be sent to.
# The main idea behind BSD sockets is closely connected to Unix philosophy contained in the words everything is a file. 
    # A socket may be often treated as very specific kind of file.
# NOTE: MS Windows reimplements BSD sockets in the form of the WinSock. However this doesnt mean we change the way we 
    # work with sockets in windows

# Initially BSD sockets were designed to organize communication in two different domains:
    # Unix domain (Unix for short) - a part of BSD sockets used to communicate programs working within one operating system 
        # (i.e., simultaneously present in the same computer system)
    # Internet domain (INET in short) - a part of BSD socket API used to communicate programs working within different computer systems, 
        # connected together using a TCP/IP network (note: this doesn't preclude the use of INET sockets to communicate processes working 
        # in the same system)



#### SOCKET ADDRESSES ### 
# The two programs wanting to exchange their data must be able to identify each other - to be precise, 
# they must have the ability to clearly indicate the socket they want to connect through.

# INET domain sockets are identified (addressed) by pairs of values:
    # the IP address of the computer system inside which the socked is located;
    # the port number (more often referred to as service number)

# IP ADDRESS:
    # An IP address (more precisely: IP4 address) is a 32-bit long value used to identify computers connected to any TCP/IP network. 
    # The value is usually presented as four numbers from the range 0..255 (i.e., eight bits long) coupled together with dots (e.g., 87.98.239.87).
    # There is also a newer IP standard, named IP6, using 128 bits for the same purpose. Due to its slight prevalence 
    # (according to data published in August 2016, less than 20% of computers in the world are reachable by IP6 addressing) 

# Port Number (Socket/Service number):
    # The socket/service number is a 16-bit long integer number identifying a socket within a particular system. 
        # as you may have guessed already, there are 65,536 (2 ** 16) possible socket/service numbers.
    # The term service number came from the fact that many standard network services usually use the same, constant socket numbers 
        # e.g., the HTTP protocol, a carrier of data used by REST, usually uses port 80.
        
# Protocol
    # A protocol is a standardized set of rules allowing processes to communicate with each other. 
    # We may say that a protocol is a kind of network savoir-vivre specifying the rules of behaviour for all participants.

# Protocol Stack
    # A protocol stack is a multilayer (hence the name) set of cooperating protocols providing a unified repertoire of services. 
        # The TCP/IP protocol stack is designed to cooperate with networks based on the IP protocol (the IP networks).     
    # The conceptual model of network services describes the protocol stack in a way where the most basic, elementary services 
        # are located at the bottom of the stack, while the most advanced and abstractive lie on the top.
    # It is assumed that any higher layer implements its functionalities using services provided by the adjoining lower layer 
        # (note: it is the same as in the other parts of the operating system, e.g., you program implements its functionality 
        # using OS services and OS services implement their functionalities using hardware facilities).

# IP
    # The IP (Internetwork Protocol) is one of the lowest parts of TCP/IP protocol stack. Its functionality is very simple - 
        # it is able to send a packet of data (a datagram) between two network nodes.
    # IP is a very unreliable protocol. It doesn't guarantee that:
        # 1). any of the sent datagrams will reach the target (moreover, if any of the datagrams is lost, it may remain undetected)
        # 2). the datagram will reach the target intact;
        # 3). a pair of sent datagrams will reach the target in the same order as they were sent.
    # The upper layers are able to compensate all the IP's shortcomings.

# TCP
    # The TCP (Transmission Control Protocol) is the highest part of the TCP/IP protocol stack.
    # It uses datagrams (provided by the lower layers) and handshakes (an automated process of synchronizing the flow of data) 
        # to construct a reliable communication channel able to transmit and receive single characters.
    # Its functionality is very complex, as it guarantees that:
        # 1). a stream of data reaches the target, or the sender is informed that communication has failed;
        # 2). data reaches the target intact.
# UDP
    # The UDP (User Datagram Protocol) lies at the higher part of TCP/IP protocol stack, but lower than the TCP. It doesn't use handshakes, 
        # which has two serious consequences:
        # 1). it is faster than TCP (due to fewer overheads)
        # 2). it is less reliable than TCP.

# TCP or UDP:
    # TCP is first choice for security concerned application. SECURITY (WWW, REST, mail transfer)
    # UDP is first choice where response timings are crucial. SPEED (DNS, DHCP)



#### CONNECTION-ORIENTED VS. CONNECTIONLESS COMMUNICATION ####

# CONNECTION ORIENTED
# A form of communication which demands some preliminary steps to establish the connection and 
    # other steps to finish it is connection-oriented communication.
# Usually, both parties involved in the process aren't symmetrical i.e., their roles and routines are different. 
    # Both sides of the communication are aware that the other party is connected.

# A phone call is a perfect example of connection-oriented communication:
    # the roles are strictly defined: there is a caller and there is a callee;
    # the caller must dial the callee's number and wait till the network routes the connection;
    # the caller must wait for the callee to answer the call (the callee may reject the connection, or just not answer the call)
    # the actual communication won't start until all the previous steps are completed successfully;
    # the communication ends when either of the parties hangs-up.

# TCP/IP networks use the following names for both sides of the communication:
    # the side that initiates the connection (caller) is named CLIENT;
    # the side that answers the client (callee) is named SERVER.
# Connection-oriented communications are usually built on top of TCP.

# CONNECTIONLESS
# A communication which can be established ad-hoc (snap - just like that) is connectionless communication. 
    # Both parties usually have equal rights, but neither of the parties is aware of the other side's state.

# Using walkie-talkies is a very good analogy for connectionless communication, because:
    # either of the parties of communication may initiate the communication at any time; it only requires pushing the talk button;
    # talking to the mic doesn't guarantee that anybody will hear (it’s necessary to wait for an incoming answer to be sure)
# Connectionless communications are usually built on top of UDP.
