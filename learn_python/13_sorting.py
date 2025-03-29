from operator import attrgetter
# SORTING LISTS, TUPLES AND OBJECTS
 
li = [9,1,8,2,7,3,6,4,5]
tup = (9,1,8,2,7,3,6,4,5)
di = {'name': 'Sam', 'job': 'programming', 'age': None, 'os': 'Windows'}

# use the sorted method to store the new sorted array (preferred method)
s_li = sorted(li)
s_tup = sorted(tup)
s_di = sorted(di)

# you can also sort the given list inplace ONLY WORKS ON LISTS
li.sort() # can reverse too

# tup.sort() # NOT POSSBILE

print(s_li)
print(s_tup)
print(s_di)


# SORT depending on a certain criteria
li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)

print(s_li)

di = {'name': 'Sam', 'job': 'programming', 'age': None, 'os': 'Windows'}
di2 = {'name': 'Cameron', 'job': 'dancer', 'age': None, 'os': 'Linux'}
di3 = {'name': 'John', 'job': 'nurse', 'age': None, 'os': 'Mac'}

di_list = [di, di2, di3]

s_di = sorted(di_list, key=lambda d: d['job'])

print(s_di)