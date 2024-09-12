from decimal import localcontext, Decimal

a = Decimal('1.3')
b = Decimal('1.7')

print(a / b)  # 默认精度

with localcontext() as ctx:
    ctx.prec = 3  # 设置精度
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50  # 设置精度
    print(a / b)
