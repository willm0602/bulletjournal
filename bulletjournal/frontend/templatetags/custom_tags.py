from datetime import datetime
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