from inspect import signature
def spam(x,y,z=42):
    pass

sig = signature(spam)
print(sig)
print(sig.parameters)

print(sig.parameters['z'].name)
print(sig.parameters['z'].default)
print(sig.parameters['z'].kind)

bound_types = sig.bind_partial(int, z=int)
print(bound_types)
print(bound_types.arguments)