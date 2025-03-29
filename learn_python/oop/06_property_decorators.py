# Python Object Oriented Programming Property decorator
# special methods that change certain functionality

# class to create different individual unique employees
class Employee:
    
    # class variables
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = f'{first}.{last}@gmail.com'
        
        # applied to all employee class
        Employee.num_of_emps += 1
    
    @property   
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'
    
    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @full_name.deleter
    def full_name(self):
        print('Delete Name!')
        self.first = None
        self.last = None

        
    
    

# instances
emp_1 = Employee('Sam', 'Smith', 50000)

emp_1.first = 'Jim'

emp_1.full_name = 'Poly Gon'

print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name)

del emp_1.full_name