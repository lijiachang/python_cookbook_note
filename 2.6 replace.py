import re

date = '11/27/2012'
# “11/27/2012”改为“2012-11-27”

result = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', date)
print(result)

date = '11/27/2012'

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
result, n = datepat.subn(r'\3-\1-\2', date)
print(result)
print(n)

from calendar import month_abbr


def change_date(m):
    """这里的m是re.compile(r'(\d+)/(\d+)/(\d+)')的结果"""
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


print(datepat.sub(change_date, date))
