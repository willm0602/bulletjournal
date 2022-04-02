import random
from string import ascii_letters

def random_str(_len):
    _str = ''
    for i in range(_len):
        ch = random.choice(ascii_letters)
        _str+=ch
    return _str