# SELF REFERS TO THE INSTANCE, in this case EMPLOYEE is what self is
# referring to


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


emp_1 = Employee('Jeff', 'Goldblum', 55000)
emp_2 = Employee('Sid', 'Meyers', 100000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.raise_amount = 1.05
emp_1.raise_amount = 1.07

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)
