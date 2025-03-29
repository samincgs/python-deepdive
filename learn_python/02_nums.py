# ALL ABOUT INTEGERS AND FLOATS and related methods

num = 3
num = 3.14

# get the type of the variable
print(type(num))

# # addition
print(3 + 2)

# # subtraction
print(3 - 2)

# # multiply
print(3 * 2)

# # divide
print(3 / 2)

# # or floor division (drop the decimal)
print(3 // 2)

# # exponent/ power
print(3 ** 2)

# modulus
print(3 % 2)

# find if number is even or odd
if (num % 2 == 0):
    print('even')
else:
    print('odd')


# parenthesis matters
print(3 * (2 + 1))

# incrementing 
num += 1
print(num)

# methods
# absolute vakue
print(abs(-3))

# # round a value
print(round(3.75))
print(round(3.75, 1))

num_1 = 3
num_2 = 2

# # comparison operators
print(num_1 == num_2) # equals
print(num_1 != num_2) # does not equal
print(num_1 >= num_2) # greater than
print(num_1 <= num_2) # smaller than

# common problem num is a string
num_1 = '100'
num_2 = '200'

# casting
num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)