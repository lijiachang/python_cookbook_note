import types


# 这部分没有变化
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


# 下面是开始变化的部分
class NodeVisitor:
    """通过生成器实现"""

    def visit(self, node):
        stack = [node]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()

            except StopIteration:
                stack.pop()
        return last_result

    def _visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        yield (yield node.left) + (yield node.right)

    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)

    def visit_Mul(self, node):
        yield (yield node.left) * (yield node.right)

    def visit_Div(self, node):
        yield (yield node.left) / (yield node.right)

    def visit_Negate(self, node):
        yield -(yield node.operand)


a = Number(0)
for n in range(1, 100000):
    a = Add(a, Number(n))

e = Evaluator()
print(e.visit(a))
