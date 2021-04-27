###         Inheritance!        ###

class Employee:

    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

### this is a subclass of Employee ###     
class Developer(Employee):
    raise_amount = 1.10

### in order for prog_lang to be added to the Developer class ONLy ###
### we must get the Employee class to fill in the fname, lname, pay ###
    def __init__(self, fname, lname, pay, prog_lang):
### super() refers to the superclass above Developer in the hierarchy ###
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())

dev_1 = Developer('Jeff', 'Goldblum', 55000, 'Python')
dev_2 = Developer('Sid', 'Meyers', 100000, 'Java')

mgr_1 = Manager('Sally', 'Barton', 90000, [dev_1])





