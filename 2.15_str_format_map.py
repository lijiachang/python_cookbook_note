from collections import UserDict

s = '{name} has {n} message.'
name = 'Guido'


class SafeSub(UserDict):
    def __missing__(self, key):
        return '{' + key + '}'


print(s.format_map(SafeSub(vars())))

import sys


def sub(text):
    return text.format_map(SafeSub(sys._getframe(1).f_locals))


name = 'Guido'

print(sub('hello {name}'))
print(sub('your favorite color is {color}'))

import string

name = 'Guido'
n = 37

s = string.Template('$name has $n message')

print(s.substitute(vars()))  # substitute 替代
