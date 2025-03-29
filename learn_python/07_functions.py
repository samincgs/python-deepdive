# FUNCTIONS

# def keyword stands for definition
# we use functions to reuse code without repeating ourselves
# we use functions to take an input value and do calculations and return an output

def hello_func():
    return 'Hello Function'

# know what the function returns
print(hello_func().upper())

print(len('Test'))

# add arguments to function
def hello_func(greeting, name = 'You'):
    return f'{greeting}, {name}'


print(hello_func('Hi', 'Samin'))

#positional arguments -> ('Hi', 'Samin')
#keyword arguments -> (name = 'Samin', greeting = 'Hi')

# arg is all the total arguments (non keyword)

courses = ['Math', 'Art']
info = {'name':'John', 'age': 22}

def student_info(*args, **kwargs):
    
    print(args) # prints all positional arguments
    print(kwargs) # prints all keyword arguments

# * to unpack lists and tuples and dictionary keys, ** to unpack dictionary both keys and values -> name = 'John'
student_info(*courses, **info)

