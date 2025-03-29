# CONDITIONALS 

# Comparisons
# Equal ==
# Not Equal !=
# Greater Than >
# Less Than <
# Greater Than Equal >=
# Less Than Equal <=
# Object Identity: is

# boolean conditions
# and
# or
# not

# False Values:
# False
# None
# Zero of any numeric type
# any empty sequence ex. '', (), []
# any empty mapping ex. '', {}

language = 'JavaScript'

if language == 'Python': # based on conditional only prints if condition is true
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')
    
# switch case
match language:
    case 'Python':
        print('Language is Python')
    case 'Java':
        print('Language is Java')
    case _:
        print('No match')
        
user = 'User'
logged_in = False

# and both need to be true
# or only one need to be true
# not reverse an operation
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')
    
if not logged_in:
    print('Log in please')
else:
    print('Welcome')
    
# object identity tests if two objects have the same id meaning if they are the same object in memory
a = [1,2,3]
b = [1,2,3]
c = a

# if the values are the same
print(a == b)

# if the location in memory is the same
print(id(a))
print(id(b))
print(id(c))
print(a is b)

# Falsy Values
list_1 = []
dict_1 = {}
player = None

if len(list_1):
    print('Alive')
else:
    print('Dead')