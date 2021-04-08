
# When we buy a new phone, it's necessary to import old contacts. Why not import them from a CSV file? 
# Look again at the familiar contacts.csv file, and then design your new phone as follows:

    # 1). Create a class called PhoneContact representing a single contact. The PhoneContact class should contain the name 
        # and phone properties;
    # 2). Create a class called Phone that will store your contacts. First, implement the method called load_contacts_from_csv, 
        # responsible for reading data from the CSV file into the class property called contacts. 
        # The contacts property should contain a list of PhoneContact objects;
    # 3). Add to the Phone class a method called search_contacts, which accepts any phrase entered by the user from the keyboard, 
        # and then based on it perform a search for all matching contacts (case insensitive). If there are no results, print the message: 
        # "No contacts found"

import csv
import pandas as pd


class PhoneContact:
    def __init__(self, name, number):
        self.name = name 
        self.number = number
    

class Phone:
    def __init__(self):
        self.contact_location = 'contacts.csv'
        self.contacts = []
        self.fieldnames = ['Name', 'Phone']
        self.load_contacts_from_csv()
        self.run()

    def run(self):
        while True:
            self.print_menu()
            choice = self.read_users_choice()
            if choice == '0':
                print("Bye!")
                exit(0)
            elif choice == '1':
                self.print_contacts()
            elif choice == '2':
                self.search_contacts()
            elif choice == '3':
                self.add_contact()
            elif choice == '4':
                self.del_contact()

    
    def load_contacts_from_csv(self):
        with open(self.contact_location, newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=self.fieldnames)
            for line in reader:
                contact = PhoneContact(line['Name'], line['Phone'])
                self.contacts.append(contact)

    def search_contacts(self):
        results = []
        txt = self.get_search_input()
        for i in range(len(self.contacts)):
            if txt in self.contacts[i].name or txt in self.contacts[i].number:
                results.append(self.contacts[i])
        if len(results) == 0:
            print('No Contacts Found')
            return
        else:
            i = 1
            print('\t**Results**')
            for contact in results:
                print(f'{i}). {contact.name} : {contact.number}')
                i += 1

    def get_search_input(self):
        search = input('Type to search: ')
        while len(search) > 40:
            search = input('Type to search: ')
        if len(search) < 40:
            return search
    
    def print_contacts(self):
        for contact in self.contacts:
            print(f'{contact.name} : {contact.number}')

    def add_contact(self):
        def phone_format(n):                                                                                                                                  
            return format(int(n[:-1]), ",").replace(",", "-") + n[-1]

        contact_name = self.enter_name()
        contact_num = phone_format(self.enter_number())
        with open(self.contact_location, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([contact_name, contact_num])
        self.load_contacts_from_csv()

    def enter_name(self):
        name = input('Enter name of contact: ')
        if name == '':
            return None
        if name.isalpha() and len(name) < 40:
            return str(name)
        else:
            self.enter_name()

    def enter_number(self):
        number = input('Enter number of contact: ')
        if number == '':
            return None
        if number.isdigit() and len(number) < 9:
            return int(number)
        else:
            self.enter_number()

    def del_contact(self):
        to_be_deleted = self.get_search_input()
        with open(self.contact_location, 'w+', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for line in csv.DictReader(csvfile):
                if to_be_deleted not in line['Name'] or to_be_deleted not in line['Number']:
                    writer.writerow(line)
        

    def contact_valid(contact):
        flags = 0
        if contact == '':
            return True
        for c in contact:
            if c.isalnum() or c ==' ':
                continue
            else:
                flags += 1
                print(f'Flags: {flags}')
        if flags == 0 and len(contact) < 40:
            return True
        else:
            return False
    
    def print_menu(self):
        print()
        print('  ****MENU****')
        print('1. List contacts')
        print('2. Search contacts')
        print('3. Add new contact')
        print('4. Delete contact')
        print('0. Exit')
        print()
    
    def read_users_choice(self):
        def make_choice():
            x = input('Enter your choice (0...4): ')
            return x

        choice = make_choice()
        while choice not in ['0', '1', '2', '3', '4']:
            print('Invalid choice, please enter a number between 0 and 4.')
            choice = make_choice()
        return str(choice)

phone = Phone()
phone.search_contacts()
phone.print_contacts()

# functions to add: add an interface similar to the command line db.
# favourites list [0-10 (speed-dial)]
# Use property decorators for:
    # add_contact
    # modify_contact
    # delete_contact
 

