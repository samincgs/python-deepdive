# File Objects READD & WRITE FILES

# first method
# f = open('test.txt', 'r') # open the file and mention mode

# # print the name of the file
# print(f.name) 

# #print the mode of the file we are working on
# print(f.mode)

# # must close the file after ur done
# f.close()

# READ
# use a context manager instead
# with open('test.txt', 'r') as f:
#     f_contents = f.read(100) # reads the whole text in the txt file (may crash if the file is too big) can take in size argument to limit the amount of characters
#     print(f.tell())
    
    # f_contents = f.readlines()puts all the lines in the text file in a list
    
    # f_contents = f.readline() # gets the first line # everytime you use f.readline() it reads the next line
    
    # f.seek(0) -> sets the reading position back to char placed in method
    
    # best way to read the file no memory issue
    # for line in f:
    #    print(line, end='') 
     
# print(f.closed)

# # WRITE
# with open('test2.txt', 'w') as f:
#     f.write('Test')
#     # f.seek(0)
#     f.write('Test2') # writes again to the end of the file

# create a copy of a text file
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
            
            
# copy a large picture file
with open('blue_loafers.jpg', 'rb') as rf:
    with open('blue_loafers_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)