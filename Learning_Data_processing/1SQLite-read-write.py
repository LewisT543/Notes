                            #### SQLite READING AND WRITING ####

# The database management system (DBMS) is the software responsible for:

    # creating a database structure;
    # inserting, updating, deleting, and searching data;
    # ensuring data security;
    # transaction management;
    # ensuring concurrent access to data for many users;
    # enabling data exchange with other database systems.

# The complete SQLite database is stored in only one file. Unlike other database management systems, 
    # SQLite doesn't require a separate server process to be running in order to communicate with the database.

# SQLite also supports transactions, which are a set of database operations that must be executed in full, 
    # or rolled back if one of them fails.

# The standard Python library has a module called sqlite3, providing an interface compliant with the DB-API 2.0 
    # specification described by PEP 249. 
# The purpose of the DB-API 2.0 specification is to define a common standard for creating modules to work with databases in Python.


# Example
    # To create a database, use the connect method provided by the sqlite3 module:

import sqlite3

'''
# Will create a database in the folder containing the file(s) trying to access it.
conn = sqlite3.connect('hello.db')
# Will create a database file at C:\sqlite called hello.db
conn = sqlite3.connect('C:\sqlite\hello.db')
# It's also possible to use a special name, :memory:, which creates a database in RAM:
conn =sqlite3.connect(':memory:')
'''

    # SQL - Standard Query Language # 
# Not gonna type any notes, its some basic ass shit.

# Example: TODO list

query = '''
CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);'''

# Using NOT NULL to prevent any null values
# added IF NOT EXISTS to make sure we arent trying to recreate the db

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute(query)


    # INSERTING DATA #
# the INSERT INTO statement
'''
INSERT INTO tasks (id, name, priority) VALUES (1, 'My first task', 1);
or
INSERT INTO tasks (name, priority) VALUES ('My first task', 1);
'''


    # INSERTING DATA PART-2 #
# The mysterious characters ? used in the INSERT INTO statement are query parameters 
    # that are replaced with the correct values during the execution of the statement.
# In the below example, the first character ? will be replaced with My first task, while the second will be replaced with l.

# Example:
conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')
c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('My first task', 1))  # USE THIS FORMAT FOR INPUTTING DATA

# IMPORTANT NOTE: This is to avoid an SQL injection attack in which malicious SQL is appended to a query that could possibly 
    # destroy our database. You can find more information about SQL injection and possible safeguard measures on the Internet.
# The execute method, as we mentioned before, has an optional argument in the form of an array of parameters. In our case, 
    # it takes a tuple, but it can be a simple array containing the same number of elements as the query parameters.


    # INSERTING DATA PART-3 COMMIT() AND CLOSE()#
# COMMIT() is used to finalise changes and apply them to the database
# CLOSE() will end a connection to the database

conn.commit()
conn.close()


    # THE EXECUTEMANY() METHOD #
# Imagine a situation where you want to add three tasks to the database. If we used the execute method, 
    # we would have to do three separate queries.
# This isn't good practice. Fortunately, the Cursor object offers us a method called executemany.
# The executemany method allows you to insert multiple records at once. As an argument, it accepts an SQL 
    # statement and an array containing any number of tuples.
# EXAMPLE:

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')
tasks = [
    ('My first task', 1),
    ('My second task', 5),
    ('My third task', 10),
]
c.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)
conn.commit()
conn.close()

    
    # A REFACTORED EXAMPLE #

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')
    
    def add_task(self):
        name = input('Enter task name: ')
        priority = int(input('Enter priority integer: '))

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()
    
app = Todo()
app.add_task()

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

    # READING DATA PART-1 #
# The SELECT statement allows you to read data from one or more tables. Its syntax looks like this:
    # SELECT column FROM table_name;    >>>     reads data from column in table_name
    #or
    # SELECT column1, column2, column3, …, columnN FROM table_name;     >>>     reads data from multiple columns
    #or
    # SELECT * FROM table_name;     >>>     reads all data from table_name
# If we'd like to read only the names of the tasks saved in the tasks table, we could use the following query:
    # SELECT name FROM tasks;   >>>     single column
    # SELECT name, priority FROM tasks;   >>>     multiple columns
    # SELECT * FROM tasks;      >>>     select all values from all cols
    # (The last variant will display the values saved in the id, name and priority columns.)


    # READING DATA PART-2 #
# After calling the execute method with the appropriate SELECT statement, the Cursor object is treated as an iterator.

conn = sqlite3.connect('todo.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM tasks'):
    print(row)
conn.close()

# NOTE: Access to individual columns is done using an index, e.g., print (row [0]) will display the values saved in the id column.


    # READING DATA PART-3 #
# If you don't want to treat the Cursor object as an iterator, you can use its method called fetchall. The fetchall method fetches all records.
# NOTE: The fetchall method is less efficient than the iterator, because it reads all records into the memory and then returns a list of tuples. 
    # For small amounts of data, it doesn't matter, but if your table contains a huge number of records, this can cause memory issues.
# NOTE: The fetchall method returns an empty list when no rows are available.

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('SELECT * FROM tasks')
rows = c.fetchall()
for row in rows:
    print(row)
conn.close()


    # READING DATA PART-4 #
# In addition to the iterator and the fetchall method, the Cursor object provides a very useful method called fetchone to retrieve 
    # the next available record.
# NOTE: The fetchone method returns None if there is no data to read.

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('SELECT * FROM tasks')
row = c.fetchone()
print(row)
row = c.fetchone()
print(row)
conn.close()
