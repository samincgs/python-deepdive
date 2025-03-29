# First Class Functions
# A programming language is said to have first-class functions if it treats functions as first-class citizens.


'''
First-Class Citizen (Programming):
A first-class citizen (sometimes called first-class object) in a programming language is an entity
which supports all the operations generally available to other entities. These operations typically include
being passed as an argument, returned from a function, and assigned to a variable.

Higher Order Function: A function that accepts other functions as arguments or returns functions as a result 
'''

def square(x):
    return x * x

# f = square # you can assign a variable to the function (one of the aspects of what it means to be a first class function)
# print(square)
# print(f(5))

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1,2,3,4,5])

print(squares)

cubes = my_map(cube, [1,2,3,4,5])

print(cubes)

def logger(msg):
    
    def log_message():
        print('Log:', msg)
        
    return log_message

log_hi = logger('Hi!')
log_hi() # rememebers the msg before it executes and this is known as a closure