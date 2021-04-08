class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email  = fname + '.' + lname + '@company.com' 

        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

# this classmethod allows the parsing of hyphonated data, creating Employee
# instances of the provided data.
    @classmethod
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
emp_1 = Employee('Jeff', 'Goldblum', 55000)
emp_2 = Employee('Sid', 'Meyers', 100000)


emp_1.set_raise_amt(1.05)


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


###         Use cases for a classmethod as an alternate constructor         ###

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# this is a simple way of fixing the issue of a different format of data input
# this can be done better with a classmethod if it is a reccuring issue

# fname, lname, pay = emp_str_1.split('-')
# new_emp_1 = Employee(fname, lname, pay)
# print(new_emp_1.email)

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)

new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.pay)


###     Static Methods!     ###
# static methods do not get passed self, or cls, or any other class variables

import datetime
my_date = datetime.date(2020, 8, 10)

print(Employee.is_workday(my_date))








