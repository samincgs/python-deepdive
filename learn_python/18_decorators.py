# Decorators

# RECAP
# First Class Functions: Treat functions like any other object (pass as arguments, return functions or assign to a variable)

# Closures: allow us to take advantage of first class functions and return an inner function that remembers and has access to variables local to the scope which they were created

def outer_func(msg):
    message = msg
    
    def inner_func():
        print(message) 
    return inner_func

hi_func = outer_func('hi')
bye_func = outer_func('bye')

# my_func() # this is what a closure is, it remembers the message variable even though it has finished executing
hi_func()
hi_func()
bye_func()


# Decorators
# A decorator is a function that takes another function as an argument and adds some sort of functionality and returns a function
# all of this must be done without altering the original function you passed in
# used to easily add functionality to our existing functions

def decorator_function(orig_func):
    def wrapper_function(*args, **kwargs): # add *args and **kwargs to add parameters
        print(f'wrapper executed this before {orig_func.__name__}')
        return orig_func(*args, **kwargs)
    return wrapper_function

# class version of the decorator function
class DecoratorClass:
    def __init__(self, orig_func):
        self.orig_func = orig_func
        
    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.orig_func.__name__}')
        return self.orig_func(*args, **kwargs)


@decorator_function
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print(f'display function ran with arguments {name} and {age}')

def display():
    print('display function ran')

@DecoratorClass
def display_info(name, age):
    print(f'display function ran with arguments {name} and {age}')
    
# same as 
# func = decorator_function(display)
    
# display()

display_info('sam', 22)
