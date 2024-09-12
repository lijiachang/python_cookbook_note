import opcode


def generate_opcodes(code_bytes):
    """生成器，接受原始字节码序列，并将其转换为对应的操作代码和参数"""
    extended_arg = 0
    i = 0
    n = len(code_bytes)

    while i < n:
        op = code_bytes[i]
        i += 1
        if op >= opcode.HAVE_ARGUMENT:
            op_arg = code_bytes[i] + code_bytes[i + 1] * 256 + extended_arg
            extended_arg = 0
            i += 2
            if op == opcode.EXTENDED_ARG:
                extended_arg = op_arg * 65536
                continue
        else:
            op_arg = None

        yield (op, op_arg)


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('blastoff(发射)!')


for op, op_arg in generate_opcodes(countdown.__code__.co_code):
    print(op, opcode.opname[op], op_arg)
