import re
def add_spaces(text):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', text)

text = "LifeIsGoodEnjoy"
print(add_spaces(text))