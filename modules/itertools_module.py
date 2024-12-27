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