from datetime import datetime, timedelta

from django import template

from api.models import Habit
from frontend import utils

register = template.Library()


@register.filter(name="contains_date", is_safe=False)
def contains_date(habit: Habit, date: datetime):
    return habit.contains_date(date)


@register.filter(name="parse_date", is_safe=False)
def parse_date(date: datetime):
    return utils.date_format_to_string(date)


@register.filter(name="reversed", is_safe=False)
def reversed(items: list):
    return items[::-1]


@register.filter(name="get_cal_num", is_safe=False)
def get_cal_num(today: datetime, xy):
    xy = xy.split(',')
    x = xy[0]
    y = xy[1]
    i = today.day - today.weekday()
    
    last_month = today.month - 1
    if last_month is 0:
        last_month=12
    DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    while i > 0:
        i = i - 7
        
    i = i + int(x) + 7 * int(y)
    
    if i < 1:
        i = DAYS[last_month] + i
    
    return i


@register.filter(name="range", is_safe=False)
def filter_range(n):
    return list(range(int(n)))


@register.filter(name="join", is_safe=False)
def join(x, y):
    return str(x) + ',' + str(y)