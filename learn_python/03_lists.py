# ALL ABOUT LISTS, TUPLES AND SETS and related methods
# Lists (mutable) -> can be changed
courses = ['History', 'Math', 'Physics', 'CompSci']

# print(courses)

# # length of courses
print(len(courses))

# # access value
print(courses[0])

# # last value
print(courses[-1])

# # first two values
print(courses[:2])

# # last two values
print(courses[2:])

# list methods
# # add item to the end of the game
courses.append('Art')

# # add item to a specific spot in the list
courses.insert(0, 'Gym')

# use extend to add multiple values to the list
courses_2 = ['Art', 'Education']

courses_2.extend(['Math', 'English'])

# remove a value from the list
courses.remove('Math')

#remove the last value of the list (can store the popped value)
popped = courses.pop()

# sort the list
nums = [1,5,2,4,3]

# reverse the list
courses.reverse()

courses.sort()
nums.sort(reverse=True)

# sorted version of our list without changing the variable 
sorted_courses = sorted(courses)

# useful built in methods
print(min(nums))
print(max(nums))
print(sum(nums))

# find the index of a certain value
print(courses.index('CompSci'))

# check if a value is in the list
print('Gym' in courses)

# loop through list
for item in courses:
    print(item)

# get the index and value when u loop through a list
for index, item in enumerate(courses, start=1):
    print(f'{index}: {item}')


print(courses)
print(courses_2)
print(nums)
print(sorted_courses)

# turn list into strings
course_str = ', '.join(courses)

# also turn a string back to a list
new_list = course_str.split(', ')
print(new_list)

print(course_str)

# issues with list
list_1 = ['Car', 'Truck', 'Van'] 
list_2 = list_1

list_1.append('Bike') # both list1 and list2 are changed because they are both the same mutable object

print(list_1)
print(list_2)


# Tuples (immutable) -> cannot be changed
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

# tuple_1[0] = 'Art' # error typeError does not support item assignment

print(tuple_1)
print(tuple_2)

# Sets are values are unordered and have no duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci'} 
art_courses = {'History', 'Math', 'Art', 'Design'}

cs_courses.add('Math')

print(cs_courses) # sets dont care for order, changes order everytime 

print('History' in cs_courses) # sets are very good at checking for values in it, fastest operation

# see what two sets have in common
print(cs_courses.intersection(art_courses))

# see what values are in one set but arent in another
print(cs_courses.difference(art_courses))

#combine both sets into one
print(cs_courses.union(art_courses))

#to create an empty set 
new_set = set() # not {}