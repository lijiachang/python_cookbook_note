import ipaddress

net = ipaddress.ip_network("123.45.67.64/27")
print(net)

for n in net:
    print(n)

net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
for n in net6:
    print(n)


# network对象也支持索引操作
print(net.num_addresses)
print(net[0])
print(net[-1])

# 还可以检查成员归属情况
a = ipaddress.ip_address("123.45.67.69")
print(a in net)

# IP地址加上网络号还可以用来指定一个IP接口（interface）
inet = ipaddress.ip_interface('123.45.67.73/27')
print(inet.network)
print(inet.ip)