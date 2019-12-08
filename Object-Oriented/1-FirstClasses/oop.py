
class Employee:

    def __init__(self, first, last, pay): #here we initialize the variables of the class object
        self.first = first #this is attribute of the class
        self.last = last #this is attribute of the class
        self.email = first + '.' + last + '@email.com' #this is attribute of the class
        self.pay = pay #this is attribute of the class

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
