# STRING DATA TYPE AND METHODS

message = 'Hello World'
greeting = 'Hello'
name = 'Michael'

message = '''
This is a multiline comment
where I can write as many lines as i want.
This is awesome!
'''

print(message)
print(len(message)) # length of string
print(message[0]) # access one part of the string by index
print(message[0:5]) # get a range of values in the string by slicing it Hello
print(message[6:]) # dont have to specify start (if value not provided it starts at the beginning) or stop (if value not provided it stops at the end) World
print(message[0::2]) # last value is the increment counter 

# string methods
# lowercase the string
print(message.lower())

# uppercase the string
print(message.upper())

# count the number of occurences for a certain string
print(message.count('o'))

# find the index for a certain string (first occurence) if index doesnt exist return -1
print(message.index('l'))

# replace a str in a variable with a str
new_message = message.replace('World', 'Universe')
print(new_message)

# add multiple strings together
print(greeting + ', ' + name)
print(greeting, name)
# f string
print(f'{greeting}, {name.title()}. Welcome!')

# show all methods for the data type
print(dir(name))