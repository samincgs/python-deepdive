# Python Object Oriented Programming Inheritance

# class to create different individual unique employees
class Employee:
    # class variables
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@gmail.com'
        
        
    # create methods for different functionalities
    def full_name(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# inheritance
# allows us to create a new class that shares the attributes and methods from the original class we are inheriting    
class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)
        self.language = prog_language
    
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
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
    
    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.full_name())

# instances
emp_1 = Employee('Sam', 'Smith', 50000)
emp_2 = Employee('Jamie', 'Oliver', 62000)

dev_1 = Developer('Jonny', 'Pols', 27000, 'Java')

mng_1 = Manager('Suzy', 'Mous', 40329)

print(emp_1.email)
print(emp_1.email)

# print(help(Developer))

print(dev_1.email)
print(dev_1.full_name())
print(dev_1.language)

print(mng_1.full_name())

mng_1.add_emp(emp_1)
mng_1.add_emp(emp_2)

mng_1.print_emp()

# isinstance
# tells us if an object is an instance of a class
print(isinstance(mng_1, Manager))
print(isinstance(mng_1, Employee))
print(isinstance(mng_1, Developer))

#issubclass
# tells us if a class is a subclass of another class
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Manager))