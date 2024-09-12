import ast
import inspect
from _ast import FunctionDef
from typing import Any


class NameLower(ast.NodeVisitor):
    def __init__(self, lowered_names):
        self.lowered_names = lowered_names

    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        code = '__globals = globals()\n'
        code += '\n'.join("{0} = __globals['{0}']".format(name) for name in self.lowered_names)
        code_ast = ast.parse(code, mode='exec')

        # 注入新的语句到函数体
        node.body[:0] = code_ast.body

        # 保存函数对象
        self.func = node


# 一个装饰器，转换全局变量名称到局部变量
def lower_names(*namelist):
    def lower(func):
        srclines = inspect.getsource(func).splitlines()
        # 跳过源行在lower_names装饰器装饰之前的
        for n, line in enumerate(srclines):
            if '@lower_names' in line:
                break

        src = '\n'.join(srclines[n + 1:])
        # 处理缩进代码
        if src.startswith((' ', '\t')):
            src = 'if 1:\n' + src
        top = ast.parse(src, mode='exec')

        # 改变 AST
        cl = NameLower(namelist)
        cl.visit(top)

        # 执行修改后的AST
        temp = {}
        exec(compile(top, '', 'exec'), temp, temp)

        # put out 修改后的代码对象
        func.__code__ = temp[func.__name__].__code__
        return func

    return lower


INCR = 1


@lower_names('INCR')
def countdown(n):
    __globals = globals()
    INCR = __globals['INCR']
    while n > 0:
        n -= INCR
        print(n)


countdown(5)
