import re

def txt_match(text):
    x = 'a.*?b$' # (.*) - all characters
    if re.search(x, text):
        return 'yes'
    else:
        return 'no'

text = input()
print(txt_match(text))