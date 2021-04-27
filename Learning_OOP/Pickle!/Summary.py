                                    #### SUMMARY ####

    # PICKLE
# it’s a Python implementation of the serialization process, so the pickled data cannot be exchanged with 
# programs written in other languages like Java or C++. In such cases, you should think about the JSON or XML formats, 
# which could be less convenient than pickling, but when assimilated are more powerful than pickling;

# the pickle module is constantly evolving, so the binary format may differ between different versions of Python. 
# Pay attention that both serializing and deserializing parties are making use of the same pickle versions;

# the pickle module is not secured against erroneous or maliciously constructed data. 
# Never unpickle data received from an untrusted or unauthenticated source.

    # SHELVE
# Think of it as a literal shelf with a set of 'pickle' jars stored on it, each labelled.
# Its essentially a dictionary consisting of 'pickled' objects as values, each labelled with a string type key.
# It requires a string type due to the underlying database format. 