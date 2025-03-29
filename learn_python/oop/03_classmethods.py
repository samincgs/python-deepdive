import datetime
# Python Object Oriented Programming Class Methods and Static Methods
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
    
    # create a class method so we dont have to use the instance of self
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    # create a class using the class value instead of creating it them
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    # static methods dont take instance or class (create when needed to create a normal function that is loosely connected to the object)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    
    

# instances
emp_1 = Employee('Sam', 'Smith', 50000)
emp_2 = Employee('Jamie', 'Oliver', 62000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

Employee.set_raise_amt(1.05)

new_emp_1 = Employee.from_string(emp_str_1)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_1.raise_amount)

print(new_emp_1.email)

my_date = datetime.date(2024, 7, 4)

print(Employee.is_workday(my_date))