s = 'p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n'  # python是令人惊叹的

remap = {ord('\f'): ' ',  # 替换成空格
         ord('\t'): ' ',  # 替换成空格
         ord('\r'): None}  # 删除\r

a = s.translate(remap)
print(a.__repr__())

import unicodedata
import sys

# 构建Unicode组合字符的字典，值统一为None
cmd_chrs = dict.fromkeys(x for x in range(sys.maxunicode) if unicodedata.combining(chr(x)))

# NFD 表示组合字符，每个字符完全分解开
b = unicodedata.normalize('NFD', a)
print(b.__repr__())
print(b.translate(cmd_chrs).__repr__())

import unicodedata
import sys

#构建一个映射表，Unicode十进制数字转换为对应的ASCII版本
digitmap = {c: ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd'}
print(len(digitmap))

x ='\u0661\u0662\u0663' # 不知道哪个国家的123字符，打印出来是：١٢٣
print(x.translate(digitmap))


a = 'p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n'  # python是令人惊叹的
b = unicodedata.normalize('NFD', a)
result = b.encode('ascii', 'ignore').decode('ascii')
print(result)

