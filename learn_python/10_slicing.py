# deepdiving into slicing
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list[5]) # with index access array
print(my_list[-1]) # negative index to access array from the back
print (my_list[-10])

# list [start:end:step] get a range
print(my_list[3:-2])

# the whole list
print(my_list[1:]) # 1- 9

print(my_list[:-1]) # 0 - 8

# entire list reversed
print(my_list[::-1])

my_list2 = my_list[:]

# slicing strings
sample_url ='http://coreyms.com'

# reverse the url
print(sample_url[::-1])

# get the top level domain
print(sample_url[-4:])

# print the url without the https://
print(sample_url[7:])

# print the url without the https:// or the toplevel domain
print(sample_url[7:-4])

# practice
random_string = 'QuantumComputingIsFascinating'

# the first 7 characters of the string
print(random_string[:7])

# extract the last 10 characters of the string
print(random_string[-10:])

# extract the characters from index 8 to 15 excluding 15
print(random_string[8:15])

# extract every second character from the entire string
print(random_string[::2])

# reverse the string
print(random_string[::-1])