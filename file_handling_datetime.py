from datetime import datetime
from datetime import date


#print(datetime.now().time())
#print(date.today())
now = datetime.now()
#print(now)

#print(now.strftime('%d-%M-%Y %H:%M:%S'))
#print(now.strftime('%d-%m-%Y %H:%M:%S'))
#print(now.strftime('%d-%B-%Y %H:%M:%S'))
#print(now.strftime('%d-%b-%Y %H:%M:%S'))

# CREATING FILES : WRITE TO, READ, APPEND, DELETE and CLOSE a File

# r: read, w: write, a: append, r+: write and read file
#file = open('./data.csv', 'r+')
#print(file.read())
#for f in file:
#   print(f)
#file.close()
print('Another way to read file is using with:')

import os.path
filename = 'data.csv'
if os.path.isfile(filename):
    print(f'{filename} does exit')
    with open(filename, 'r') as file:
        print(file.read())
else:
    print(f'{filename} does not exit')