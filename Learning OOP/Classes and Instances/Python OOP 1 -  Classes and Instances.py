

class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email  = fname + '.' + lname + '@company.com' 
        
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)


emp_1 = Employee('Jeff', 'Goldblum', 55000)
emp_2 = Employee('Sid', 'Meyers', 100000)

# print(emp_1.email)
# print(emp_2.email)


print(Employee.fullname(emp_1))
