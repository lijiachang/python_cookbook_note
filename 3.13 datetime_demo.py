from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    """获取以前日期，比如获取上周一的日期
    previous：以前的"""
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()  # 获取当前日期是星期几 1-7
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    return start_date - timedelta(days=days_ago)


print(get_previous_byday('Monday'))
print(get_previous_byday('Tuesday', start_date=datetime(2012, 12, 21)))