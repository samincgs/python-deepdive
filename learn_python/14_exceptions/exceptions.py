# EXCEPTIONS
# needed when code throws errors (for example opening/saving files)
try: # try to open the file 
    f = open('text_file.txt', 'r')
    # sgf = sdf
    if f.name == 'corrupt_file.txt':
        raise Exception
    
except (FileNotFoundError, NameError): # if it gives an error, resolve it (use specific errors)
    print('File was not found')
else: #  (runs only if we do not throw an exception)
    print(f.read())
    f.close()
finally: # runs no matter what
    print('Executing finally')