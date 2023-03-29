import re

def txt_match(text):
    x = '^[a-z]+_[a-z]+$'
    if re.search(x, text):
        return 'yes'
    else:
        return 'no'

text = input()
print(txt_match(text))