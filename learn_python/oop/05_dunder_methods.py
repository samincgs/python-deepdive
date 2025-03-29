# Python Object Oriented Programming Dunder Methods -> any methods surrounded by __ is called dunder
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
        self.email = f'{first}.{last}@gmail.com'
        
        # applied to all employee class
        Employee.num_of_emps += 1
        
    def full_name(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    # unambiguous representation of an object used to debug and log things about the object (used for the developer)
    def __repr__(self): # use as a minimum if ur gonna use the def __str__ because it depends on repr
        return f'Employee({self.first}, {self.last}, {self.pay})'

    # reading representation of an object, used as a display to see information about the object (used to display to console)
    def __str__(self):
        return f'{self.full_name()} - {self.email}'
    
    def __len__(self):
        return len(self.full_name())
    
    

# instances
emp_1 = Employee('Sam', 'Smith', 50000)
emp_2 = Employee('Jamie', 'Oliver', 62000)

print(emp_1) # gives vague info about the object but using the repr gives us a proper log (calls str first then repr)
print(repr(emp_1))
print(str(emp_1))

print(len('test')) # the same thing
print('test'.__len__())

# use with employee object
print(len(emp_1))