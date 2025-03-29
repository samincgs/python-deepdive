# DICTIONARIES -> HASHMAPS or associative arrays KEY and VALUE pairs

student = {'name': 'John', 'age': 25, 'courses' : ['Math', 'CompSci']}

# add a value to the dict
student['phone'] = '555-5555'

# if you add to an existing key it will update the value
student['name'] = 'Sam'

# use the method to update multiple values
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

#remove a key
del student['age'] 
# pop the value
age = student.pop('age')


print(student)
print(age)
print(student['name']) #access elements in a dict

# print(student['phone']) #KeyError when accessing index that doesnt exist

print(student.get('phone')) # Returns None if not found instead of KeyError when searching for index


#check length of dict
print(len(student))

# see all the keys
print((student.keys()))

# see all the values
print(student.values())

# see keys and values
print(student.items())


# loop through all the keys and values in the dict
for key,value in student.items(): # when looping it checks the keys
    print(f'{key}: {value}')