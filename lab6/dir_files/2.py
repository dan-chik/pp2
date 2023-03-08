import os
print('Exist:', os.access('C:/Users/Дана/Desktop/gig/lab4', os.F_OK))
print('Readable:', os.access('C:/Users/Дана/Desktop/gig/lab4', os.R_OK))
print('Writable:', os.access('C:/Users/Дана/Desktop/gig/lab4', os.W_OK))
print('Executable:', os.access('C:/Users/Дана/Desktop/gig/lab4', os.X_OK))
