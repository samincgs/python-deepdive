# Iterators & Iterables

# A list is an iterable but not an iterator

# An iterable is something that can be looped over (more specifically it means that the object needs to return an iterable object from its __iter__ method)
nums = [1, 2, 3] # list
i_nums = iter(nums) # get the iterator object of the num list
for num in nums:
    print(num)

print(i_nums)
# how to know if something can be looped over: it needs to have a special dunder method called __iter()__ 
print(dir(list)) # iterable
print(dir(i_nums)) # iterator

# an iterator is an object with a state that remebers where it is during iteration (needs to have a dunder __next__ method and know what state it is)
print(next(i_nums)) # iterator has next method
print(next(i_nums)) # iterator has next method
print(next(i_nums)) # iterator has next method
# also remembers where the state is

# in the background a for loop is getting an iterator of the current obj and then keeps doing next until it stops the iteration (stops when a StopIteration exception is raised)
while True: # no going backwards in an iterator
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

# create a class that acts like an iterable (like the range function)
class MyRange: # both an iterable and an iterator
    def __init__(self, start, end):
        self.value = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        current_value = self.value
        self.value += 1
        return current_value
    
nums = MyRange(1, 10)

for num in nums:
    print(num)
    
# generators (easy to read iterators) they look like normal functions but instead of returning a result they yield a value
# generators are iterators but dunder __iter__ and __next__ are created automatically
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1
        
nums = my_range(1, 5)
for num in nums:
    print(num)
    
# iterators dont need to end as long as there is a next value