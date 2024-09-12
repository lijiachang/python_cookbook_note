import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    """打开一个文件，返回一个mmap对象"""
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


# 创建一个初始文件,并为之填充一些数据
size = 1000000
with open('data', 'wb') as f:
    f.seek(size - 1)
    f.write(b'\x00')

# 开始对文件内容做内存映射操作
m = memory_map('data')
print(len(m))
print(m[0:10])
print(m[0])

# reassign a slice  重新分配一个切片(内存映射对象的切片赋值会直接修改文件内容)
m[0:11] = b'Hello World'
m.close()

# 验证文件内容
with open('data', 'rb') as f:
    print(f.read(11))
