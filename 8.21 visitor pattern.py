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

