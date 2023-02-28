import re

def txt_match(text):
    x = '^a(b*)$' # starts with a (^a), 0 or more repetitions of b (b*), end ($) 
    if re.search(x, text):
        return "yes"
    else:
        return "no"

text = input()
print(txt_match(text))