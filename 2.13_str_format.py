text = 'hello python'
print(text.ljust(20, '='))  # 居左显示，使用=填充
print(text.rjust(20, '-'))  # 居右显示，使用-填充
print(text.center(20))  # 居中显示

text = 'hello python'
print(format(text, '=<20'))  # 居左显示，使用=填充
print(format(text, '->20'))  # 居右显示，使用-填充
print(format(text, '^20'))  # 居中显示

# 可以使用format方法格式化多个值, 冒号左边是常用的定位序号，可以为空
print('{:*>20} {:->20}'.format('ni', 'hao'))

text = 'hello python'.format()
print('%-20s' % text)  # 居左显示
print('%20s' % text)  # 居右显示
