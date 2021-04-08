                        #### SQLITE UPDATING AND DELETING ####

    # UPDATING DATA #
# Each of the tasks created has its own priority, but what if we decide that one of them should be done earlier than the others. 
    # How can we increase its priority? We have to use the SQL statement called UPDATE.
# The UPDATE statement is used to modify existing records in the database. Its syntax is as follows:
'''
UPDATE table_name
SET column1 = value1, column2 = value2, column3 = value3, …, columnN = valueN
WHERE condition;
'''
# If we'd like to set the priority to 20 for a task with idequal to 1, we can use the following query:
'''
UPDATE tasks SET priority = 20 WHERE id = 1;
'''
# IMPORTANT NOTE: If you forget about the WHERE clause, all data in the table will be updated.

import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (20, 1))
conn.commit()
conn.close()

    
    # DELETING DATA #
# After completing a task, we would like to remove it from our database. To do this, we must use the SQL statement called DELETE
'''
DELETE FROM table_name WHERE condition;
DELETE FROM tasks WHERE id = 1;
'''
# NOTE: If you forget about the WHERE clause, all data in the table will be deleted.

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('DELETE FROM tasks WHERE id = ?', (1,)) # Tuple here? Not sure why, could be required...
conn.commit()
conn.close()