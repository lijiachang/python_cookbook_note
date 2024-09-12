import os

fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)  # |运算符是 __or__ 方法,os.O_WRONLY 代表整数1,os.O_CREAT 代表整数512

f = open(fd, 'wt', closefd=False)  # closefd=False 表示不关闭文件描述符
f.write('hello world')
f.close()