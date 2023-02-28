import re

def txt_match(text):
    x = '^ab{2,3}$'
    
    if re.search(x, text):
        return "yes "
    else:
        return "no"

text = input()
print(txt_match(text))