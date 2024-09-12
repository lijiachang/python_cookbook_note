def add(x, y):
    return x + y


c = add.__code__
print(c)
print(c.co_code)

import types

new_byte_code = b'xxxxxxx'
nc = types.CodeType(
    c.co_argcount,
    c.co_posonlyargcount,  # added in Python 3.8
    c.co_kwonlyargcount,
    c.co_nlocals,
    c.co_stacksize,
    c.co_flags,
    new_byte_code,
    c.co_consts,
    c.co_names,
    c.co_varnames,
    c.co_filename,
    c.co_name,
    c.co_firstlineno,
    c.co_lnotab,
    c.co_freevars,  # added for completeness
    c.co_cellvars  # added for completeness
)
print(nc)

add.__code__ = nc
add(2, 3)