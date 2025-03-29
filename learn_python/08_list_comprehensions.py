# LIST, DICTIONARY, SETS comprehension

nums = [1,2,3,4,5,6,7,8,9,10]

# i want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# list comprehension
my_list2 = [n for n in nums]

# i want n x n for each n in nums
my_list3 = [(num * num) for num in nums]

# i want n for each n in nums if n is even
my_list4 = [num for num in nums if num % 2 == 0]

# i want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list5 = [(letter, num) for letter in 'abcd' for num in range(4)]

# dictionary comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# without dictionary comprehension
hero_list = list(zip(names, heroes))
my_dict = {}
for name, hero in zip(names, heroes):
    my_dict[name] = hero
    
print(my_dict)

# with dictionary comprehension
my_dict2 = {name: hero for name, hero in zip(names, heroes)}


# all hero names without Peter as one of them
my_dict3 = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}


# set comprehension
nums = [1,1, 1, 2,3, 1, 4,5, 5, 6,7, 2, 3, 8, 12, 9,10]
my_set = set(nums)

my_set2 = {num for num in nums}

print(my_list5)
print(hero_list)
print(my_dict2)
print(my_dict3)

print(my_set)
print(my_set2)