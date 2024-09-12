import ast


class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Delete):
            self.deleted.add(node.id)


if __name__ == '__main__':
    # python 代码
    code = """
for i in range(5):
    print(i)
del i
    """
    # 解析为AST 抽象语法树
    top = ast.parse(code, mode='exec')
    # 分析代码使用
    c = CodeAnalyzer()
    c.visit(top)

    print('Loaded: ', c.loaded)
    print('Stored: ', c.stored)
    print('Deleted: ', c.deleted)

    # 通过compile()函数进行编译并执行
    exec(compile(top, '<stdin>', 'exec'))
