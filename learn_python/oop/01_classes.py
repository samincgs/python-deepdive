# Python Object Oriented Programming

# class to create different individual unique employees
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@gmail.com'
        
    # create methods for different functionalities
    def full_name(self):
        return f'{self.first} {self.last}'

# instances
emp_1 = Employee('Sam', 'Smith', 50000)
emp_2 = Employee('Jamie', 'Oliver', 62000)

print(emp_1)
print(emp_2)

# can also use methods directly from the Class
print(Employee.full_name(emp_1))

# can manually add attributes (not preferred)
# emp_1.first = 'Sam'
# emp_1.last = 'Smith'
# emp_1.email = 'Sam@gmail.com'
# emp_1.pay = 50000

# emp_2.first = 'Jamie'
# emp_2.last = 'Olive'
# emp_2.email = 'Jamie2@gmail.com'
# emp_2.pay = 62000

print(emp_1.email)
print(emp_2.email)
print(emp_1.full_name())
print(emp_2.full_name())