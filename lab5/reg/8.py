import re
text = "LifeIsAJoke"
x = '[A-Z][^A-Z]*'

print(re.findall(x, text))
#print(re.split(r'^[A-Z]{1}[a-z]*$', text))