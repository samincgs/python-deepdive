# LEARNING ABOUT SCOPE IN PYTHON

'''
LEGB
Local, Enclosing, Global, Built-IN
'''

import builtins

print(dir(builtins))

# global variable main body of the file
m = min([5, 1, 4, 2, 3]) # built in scope
print(m)
x = 'global x'

def test(z):
    # global x # can use to make variable in a global scope
    # local to the test function
    # y = 'local y'
    # print(y)
    x = 'local x'
    print(x)
    print(z)

def outer():
    x = 'outer x'
    def inner():
        # nonlocal x
        x = 'inner x'
        print(x)
    
    inner()
    print(x)
    

    
test('local z')
print(x)
outer()