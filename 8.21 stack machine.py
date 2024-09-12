class NodeVisitor:
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        method = getattr(self, method_name, None)
        if method is None:
            method = self.generic_visit

        return method(node)

    def generic_visit(self, node):
        raise RuntimeError('No method'.format('visit_' + type(node).__name__))


class StackCode(NodeVisitor):
    """将表达式翻译为指令序列"""

    def generate_code(self, node):
        self.instructions = []  # instruction: 命令，指示
        self.visit(node)
        return self.instructions

    def visit_Number(self, node):
        self.instructions.append(('PUSH', node.value))

    def binop(self, node, instruction):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append((instruction,))

    def visit_Add(self, node):
        self.binop(node, 'ADD')

    def visit_Sub(self, node):
        self.binop(node, 'SUB')

    def visit_Mul(self, node):
        self.binop(node, 'MUL')

    def visit_Div(self, node):
        self.binop(node, 'DIV')

    def visit_Negate(self, node):
        self.binop(node, 'NEG')

class Node:
    pass


class UnaryOperator(Node):
    """一元操作"""

    def __init__(self, operand):
        """operand: 操作对象"""
        self.operand = operand


class BinaryOperator(Node):
    """二元操作"""

    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    """subtract: 减法"""
    pass


class Mul(BinaryOperator):
    """multiply: 乘法"""
    pass


class Div(BinaryOperator):
    """divide: 除法"""
    pass


class Negate(UnaryOperator):
    """negate · vt. 否定；取消"""
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


# 用这些类来构建嵌套式的数据结构
# Representation of 1 + 2 * (3 - 4) / 5
t1 = Sub(Number(3), Number(4))
t2 = Mul(Number(2), t1)
t3 = Div(t2, Number(5))
t4 = Add(Number(1), t3)

s = StackCode()
print(s.generate_code(t4))