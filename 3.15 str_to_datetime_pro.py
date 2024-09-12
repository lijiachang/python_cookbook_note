from datetime import datetime


def parse_ymd(s):
    """将字符串转换为日期格式
    知道日期格式是YYYY-MM-DD形式"""
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
