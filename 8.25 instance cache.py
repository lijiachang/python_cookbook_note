import logging

a = logging.getLogger('foo')
b = logging.getLogger('bar')

print(a is b)

c = logging.getLogger('foo')
print(c is a)
