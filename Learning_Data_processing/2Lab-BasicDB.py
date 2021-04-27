
# Create a find_task method, which takes the task name as its argument. The method should return the record found or None otherwise.
# Block the ability to enter an empty task (the name cannot be an empty string).
# Block the ability to enter a task priority less than 1.
# Use the find_task method to block the ability to enter a task with the same name.
# Create a method called show_tasks, responsible for displaying all tasks saved in the database.

import sqlite3

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()
            
    def show_menu(self):
        print()
        print('  ****MENU****')
        print('1. SHOW Tasks')
        print('2. ADD Task')
        print('3. CHANGE Priority')
        print('4. DELETE Task')
        print('0. EXIT')
        print()

    def get_user_choice(self):
        try:
            user_choice = int(input('Enter your choice (0-4): '))
        except TypeError or ValueError:
            print('Invalid choice: Please enter an integer between 0 and 4.')
        while user_choice not in [0,1,2,3,4]:
            print('Invalid Choice: Please select a number from the menu.')
            user_choice = int(input('Enter your choice (0-4): '))
        else:    
            return user_choice
        

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')

    def input_id(self):
        id = input('Enter ID: ')
        while not id.isdigit():
            print('Invalid ID: Must be integer.')
            id = input('Enter ID: ')
        return id
    
    def input_name(self):
        name = input('Enter task name: ')
        while name == '':
            print('Invalid name: Cannot be empty.')
            name = input('Enter task name: ')
        return name

    def input_priority(self):
        priority = input('Enter priority integer: ')
        while not priority.isdigit() and int(priority) < 1:
            print('Invalid priority: Must be integer greater than zero.')
            self.input_priority()      
        else:
           return int(priority)       

    def find_task(self, name):
        for row in self.c.execute('SELECT * FROM tasks'):
            if row[1] == name:
                return row
        return None

    def find_task_id(self, id):
        for row in self.c.execute('SELECT * FROM tasks WHERE id = ?', (id,)):
            return row
        else:
            None       

    def add_task(self):
        name = self.input_name()
        prio = self.input_priority()
        while self.find_task(name):
            print(self.find_task(name))
            print('Invalid name: Entry already exists with that name.')
            self.input_name()
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, prio))
        self.conn.commit()
    
    def change_priority(self):
        chosen_id = self.input_id()
        print(self.find_task_id(chosen_id))
        if self.find_task_id(chosen_id) == None:
            print('Invalid Update: Cannot find entry with that ID.')
            return
        new_priority = self.input_priority()
        self.c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (new_priority, chosen_id))
        self.conn.commit()
    
    def delete_task(self):
        delete_id = self.input_id()            
        if self.find_task_id(delete_id):
            self.c.execute('DELETE FROM tasks WHERE id = ?', (delete_id,))
        else:
            print('Invalid Delete: ID not present in DB.')
            return
        
    def show_tasks(self):
        for row in self.c.execute('SELECT * FROM tasks'):
            print(row)


db1 = Todo()
while True:
    db1.show_menu()
    choice = db1.get_user_choice()
    if choice == 0:
        print('Goodbye!')
        exit()
    elif choice == 1:
        db1.show_tasks()
    elif choice == 2:
        db1.add_task()
    elif choice == 3:
        db1.change_priority()
    elif choice == 4:
        db1.delete_task()
    