# Python Object Oriented Programming Class Variables

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
        
        Employee.num_of_emps += 1
        
    # create methods for different functionalities
    def full_name(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    

# instances
emp_1 = Employee('Sam', 'Smith', 50000)
emp_2 = Employee('Jamie', 'Oliver', 62000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)