from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

d = datetime.now()
print(d)

# 得到下一个周五Friday
print(d + relativedelta(weekday=FR))

# 得到上一个Friday
print(d + relativedelta(weekday=FR(-1)))