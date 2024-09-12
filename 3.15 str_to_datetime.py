from datetime import datetime, timedelta

text = '2018-01-01'
y = datetime.strptime(text, '%Y-%m-%d')  # 将字符串转换为日期格式
print(y)

print(datetime.now() - y)  # 得到两个日期的间隔

nice_day = datetime.strftime(datetime.now(), '%A %B %d, %Y')  # 将日期格式转换为字符串
print(nice_day)