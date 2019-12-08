
class Employee:

    raise_amount = 1.04 #this is class variable
    num_of_employes = 0 #this is a class variable to keep track how many workers do we have
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        
        Employee.num_of_employes+ = 1 #we are adding one each time when we are creating class object of Emplyee and its subclasses

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
