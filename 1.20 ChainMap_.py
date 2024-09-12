from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)

c['z'] = 888
del c['x']

print(a)
print(b)

values = ChainMap()
values['x'] = 1
values = values.new_child()  # add a new mapping
values['x'] = 2
values = values.new_child()  # add a new mapping
values['x'] = 3
print(values)

print(values['x'])
values = values.parents  # discard last mapping
print(values['x'])
values = values.parents  # discard last mapping
print(values['x'])

print(values)
