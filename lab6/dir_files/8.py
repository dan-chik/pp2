import os
p=(r"C:\Users\Дана\Desktop\gig\lab6\dir_files\todelete.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file doesnt exist")