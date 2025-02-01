# A lambda function is the same with a normal function in python
# The whole idea of lambda functions or (also known as an anonymous function) is that they are made to be passed into a higher order function
# A higher order function is a function that essentially takes in a function as input or returns a function

def add(x, y):
    return x + y

print(add(4, 5))

# is the same thing
add_func = lambda x, y: x + y

print(add_func(4, 5))

def my_map(my_func, my_iter):
    result = []
    for item in my_iter:
        new_item = my_func(item)
        result.append(new_item)
    return result

nums = [3, 4, 5, 6, 7]

# lambda function is passed onto higher order function my map and was used to cubed every item of the iterable
cubed = my_map(lambda x: x ** 3, nums)

print(cubed)


