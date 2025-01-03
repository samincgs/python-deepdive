import itertools
# itertools is a collection of tools that work with iterators in a fast and effective way

# count - returns an iterator that counts that keeps on going
counter = itertools.count() # takes argument start (where it starts) and step(how much it increments/decrements each time)

print(next(counter)) 
print(next(counter)) 
print(next(counter)) 


# zip longest - zips two iterables but instead of doing it for only the shortest one it does it with the longest one and pairs the remaining with None

data = [100, 200, 300, 400]

daily_data = list(itertools.zip_longest(range(10), data))

print(daily_data)


# cycle - also returns an iterable that goes on forever (keeps going over the list cycling back)
counter = itertools.cycle(['on', 'off'])
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 

# repeat - takes some input and repeats it indefinetely (can specify how many times) will return StopIteration error after the times value
counter = itertools.repeat(2, times=3)


# combinations - are all the different types you can group a certain number of items where order does not matter


# permutations

# chain