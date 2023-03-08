import os
path = os.listdir(r'C:\Users\Дана\Desktop\gig')

for i in path:
    if os.path.isdir(i):
        print('directories', i)
for i in path:
    if os.path.isdir(i) or os.path.isfile(i):
        print('\ndirestories and files', i)
for i in path:
    if os.path.isfile(i):
        print('\nfiles', i)
