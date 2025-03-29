from math import pi
from datetime import datetime
# F_STRINGS

first_name = 'John'
last_name = 'Doe'

#older method
sentence = 'My name is {} {}'.format(first_name, last_name)

# new method
sentence = f'My name is {first_name.title()} {last_name}'

print(sentence)

person = { 'name': 'John', 'age': 23}

person_sentence = 'The name is {} and the age is {}'.format(person['name'], person['age'])

# f string
person_sentence = f'My name is {person['name']} and I am {person['age']} years old'

print(person_sentence)

calculation = f'4 times 11 is equal to {4 * 11}'

print(calculation)

# use it with loops
for n in range(1, 11):
    sentence = f'The value is {n:02}' # zero pad the front
    print(sentence)
    
    
# with floats
sentence = f'Pi is equal to {pi:.4f}' # 4 digits after the decimal

print(sentence)

# with datetime values
birthday = datetime(2002, 4, 23).strftime(f'%B-%m-%d')
sentence = f'Sam has a birthday on {birthday}'

print(sentence)