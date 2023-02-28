import re

def txt_match(text):
    x = '^[A-Z]{1}+[a-z]'
    if re.search(x, text):
        return "yes"
    else:
        return "no"

text = input()
print(txt_match(text))