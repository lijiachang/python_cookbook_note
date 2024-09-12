from datetime import datetime
from pytz import timezone

day = datetime(2012, 12, 21, 9, 30, 0)
print(day)

# 本地化时间为芝加哥时间
central = timezone('US/Central')  # central: 中心
local_day = central.localize(day)
print(local_day)

# 一旦做了本地化处理，就可以转换为其他的时区。
# 要知道印度的时间：
bang_day = local_day.astimezone(timezone('Asia/Kolkata'))
print(bang_day)
