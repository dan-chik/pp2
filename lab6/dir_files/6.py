"""for i in "abc":
    f=open("{}.txt".format(i), "x")"""

import string

for letter in string.ascii_uppercase:
    with open('{}.txt'.format(letter), 'w') as f:
        f.write(letter)