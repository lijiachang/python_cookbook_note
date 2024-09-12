import os
import fnmatch  # 通配符匹配
import gzip
import bz2
import re


def gen_find(file_pattern, top):
    """遍历目录下所有符合规则的文件"""
    for path, dirlist, filelist in os.walk(top):  # 遍历目录下的内容
        for name in fnmatch.filter(filelist, file_pattern):  # 实现列表特殊字符的过滤,返回符合匹配模式的字符列表
            yield os.path.join(path, name)  # 拼接路径


def gen_opener(filenames):
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')  # t: text mode(default)
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    """连接多个可迭代对象"""
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


# 把这些生成器函数堆叠起来形成一个处理数据的管道。找出包含python的日志行
lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)
