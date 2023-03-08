f = open(r'C:\Users\Дана\Desktop\gig\lab6\dir_files\testfile.txt')
cnt = 0
for line in f:
    cnt+=1

print('Number of lines in the file: ', cnt)