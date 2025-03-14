# What is the difference between the '==' and 'is'?
# '--' checks for equality
# 'is' checks for identity -> means checks the the same object in memory

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3 , 4, 5]

# equality
if list1 == list2: # True because they have the same values
    print('True')
else:
    print('False')

# identity 
if list1 is list2: # False since they are too completely different lists in memory
    print('True')
else:
    print('False')