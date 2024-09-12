from datetime import datetime

import pytz
from pytz import timezone

day = datetime(2013, 12, 21, 9, 30, 0)
print(day)

# 本地化时间为芝加哥时间
central = timezone('US/Central')  # central: 中心
local_day = central.localize(day)
print(local_day)

# 转换为UTC时间
utc_day = local_day.astimezone(pytz.utc)
print(utc_day)

print(pytz.country_timezones['IN'])
print(pytz.country_timezones['CN'])
