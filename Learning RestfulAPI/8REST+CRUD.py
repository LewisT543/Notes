                        #### REST and CRUD ####

# A properly trained web server can be a very effective and convenient gateway to very complicated and heavy databases or other     
    # services designed for storing and processing information. Moreover, the structure of the database (or the service) may vary, 
    # e.g., it may be a simple relational database residing in a single file, or on the contrary, a huge, distributed cloud of 
    # cooperating servers; but the interface provided to the user (you) will always look the same.

# We can say that that's what REST was invented for. Thanks to it, very different programs written in very different technologies can 
    # utilize shared data through one, universal interface.
# The interface itself enables the user to perform a basic set of operations – they are elementary, but complex enough to build complex 
    # services. A set of four operations hides beneath the following mysterious acronym:

#### CRUD ####
# Create, Read, Update, Delete
    
# C means CREATE: 
    # If you are able to “create”, you can add new items to data collection, for example, write a new blog post, add a new picture to the gallery, 
        # store a new client's data in a customer database, etc.
    # At REST level, the creation of new items is implemented by the POST HTTP method.

# R means READ or, if you prefere, RETRIEVE:
    # Reading/retrieving is the very basic ability to browse data stored in a collection, e.g., reading posts on somebody's blog, 
        # viewing pictures in a gallery, studying customers' records in a database, etc.
    # At REST level, the retrieving of items is implemented by the GET HTTP method.

# U means Update:
    # You update data inside a collection when you modify the contents of the selected item without removing it, e.g., 
        # you edit your blog post, resize a picture in the gallery, enter the current customer’s sales information, etc.
    # At REST level, updating existing data is implemented by the PUT HTTP method.

# D for Delete:
    # Deletion occurs when you remove your post from the blog, purge a picture from the gallery or cancel a customer’s account.
    # At REST level, deleting existing data is implemented by the DELETE HTTP method.

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# Now we’re ready to carry out some simple but instructive experiments with JSON. We’ll use it as an intermediate language to 
    # communicate with the HTTP server, implementing CRUD and storing a sample collection of data.

# We'll make use of the previously presented json-server – we'll try to get it to work hard with all four letters making up CRUD;
# Our initial database, processed on our demands by the json-server, will be a collection of retro cars written down in the cars.json file; 
    # the json-server will read the file in and will handle its contents according to our actions;
# Each car is described by:
    # id – a unique item number; note – each item in the collection must have the property of this name – this is how the server identifies 
        # each item and differentiates the items from each other;
    # brand – a string;
    # model – a string;
    # production_year – an integer number;
    # convertible – a Boolean value;
# The initial file contains data for six cars – don't be surprised if the server modifies its contents; if you want to reset the collection to 
    # the initial state, stop the server (use Ctrl-C for this purpose), replace the file with its original version and start the server again.

import requests

try:
    reply = requests.get("http://localhost:3000/cars")
except requests.RequestException:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        print(reply.text)
    else:
        print("Server error")