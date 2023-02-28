# camel case - without spaces or punctuation, indicating the separation of words with a single capitalized letter, and the first word starting with either case
# snake case - each space is replaced by an underscore (_) character, and the first letter of each word written in lowercase


def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel('life_is_good'))