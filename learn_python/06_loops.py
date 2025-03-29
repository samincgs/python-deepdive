# LOOPS AND ITERATIONS

nums = [1, 2, 3, 4, 5]

# break out of iteration of for loop
for num in nums:
    if num == 3:
        print("Found")
        break
    print(num)

# continue skips to the next iteration of the loop
for num in nums:
    if num == 3:
        print("Found")
        continue
    print(num)

# nested loops
for num in nums:
    for letter in "abc":
        print(num, letter)

# loop through a certain range
for i in range(1, 11):
    print(i)

x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
