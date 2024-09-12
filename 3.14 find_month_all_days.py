from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    """获取月份的开始和结束日期"""
    if start_date is None:
        start_date = date.today().replace(day=1)  # 获取当前月份的第一天
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)  # 获取下个月的第一天
    # end_date = start_date + timedelta(days=days_in_month) - timedelta(days=1)  # 获取当前月份最后一天
    return start_date, end_date


print(get_month_range())


def date_range(start, end, step=timedelta(days=1)):
    """指定间隔来获取日期范围"""
    while start < end:
        yield start
        start += step


for day in date_range(*get_month_range(), step=timedelta(days=10)):
    print(day)
