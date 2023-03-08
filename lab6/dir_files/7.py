import os
f1 = os.popen("from.txt", "r")
f2 = os.popen("to.txt", "w")
for line in f1:
    f2.write(line)