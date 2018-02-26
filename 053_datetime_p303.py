# !usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import datetime
from datetime import timedelta
from datetime import timezone
import re

# 内建模块

# 1 datetime: 处理日期和时间的标准库
# 1.1 获取当前日期和时间
print('========1.1========')

now = datetime.now()  # 返回当前日期和时间，其类型是datetime
print(now)
print(type(now))

# 1.2 指定某个日期和时间
print('========1.2========')

dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
print(dt)

# 1.3 datetime转化为timestamp(当前时间相对epochtime的秒数）: timestamp()
print('========1.3========')

dt = datetime(2015, 4, 19, 12, 20)
print(dt.timestamp())  # 把datetime转换为timestamp

# 1.4 timestamp转化为datetime: datetime.fromtimestamp()
print('========1.4========')

t = 1429417200.0
print(datetime.fromtimestamp(t))  # datetime有时区概念，默认为当前操作系统设定的时区
print(datetime.utcfromtimestamp(t))  # 输出UTC标准时区的时间

# 1.5 str转化为datetime: datetime.strptime()
print('========1.5========')

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# 1.6 datetime转化为str: strftime()
print('========1.6========')

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))  # a b c d...各自代表不同的含义

# 1.7 datetime加减： timedelta类
print('========1.7========')

now = datetime.now()
print(now)

n1 = now + timedelta(hours=10)
print(n1)

n2 = now - timedelta(days=1)
print(n2)

n3 = now + timedelta(days=2, hours=12)
print(n3)

# 1.8 本地时间转换为UTC标准时间
print('========1.8========')

tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
now = datetime.now()
print('tz=', now)

dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00,如果系统时区不是的话，就无法强制设置
print(dt)

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)  # 拿到UTC时间并强制设置为UTC+0
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  # 转化时区为北京时间
print(bj_dt)

tk_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))  # 转化时区为东京时间
print(tk_dt)

tk_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))  # 将北京时间转化为东京时间
print(tk_dt2)

# E.1 编写一个函数，将用户输入的str 日期和时间以及时区信息转化为timestamp
print('========E.1========')

dt_str = '2015-1-21 9:01:30'
tz_str = 'UTC+5:00'


def dt2stamp(dtstr, tzstr):
    dt = datetime.strptime(dtstr, '%Y-%m-%d %H:%M:%S')
    tz = re.match(r'^UTC\s?([+|-]\d{1,2}):00$', tzstr).group(1)
    tz_utc = timezone(timedelta(hours=int(tz)))
    dt_utc = dt.replace(tzinfo=tz_utc)
    return dt_utc.timestamp()


print(dt2stamp(dt_str, tz_str))
