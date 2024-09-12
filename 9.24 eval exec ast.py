import ast

ex = ast.parse('2 + 3*4 + x', mode='eval')
print(ex)
print(ast.dump(ex))

top = ast.parse('for x in range(5): print(x)', mode='exec')
print(top)
print(ast.dump(top))
