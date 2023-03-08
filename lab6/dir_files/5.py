import os
f = os.popen(r'C:\Users\Дана\Desktop\gig\lab6\dir_files\forlistfile.txt')
mylist = ["please", "put", "me", "max", "points"]
for i in mylist:
    f.write(i)
f.close()