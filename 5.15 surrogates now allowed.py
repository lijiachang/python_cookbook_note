def bad_filename(filename):
    return repr(filename)[1:-1]  # repr() 函数将对象转化为供解释器读取的形式

try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))