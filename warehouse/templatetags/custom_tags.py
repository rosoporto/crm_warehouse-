from datetime import datetime
from django import template


register = template.Library()


@register.simple_tag
def show_time():
    """Return the current time in the format H:M:S"""
    dt = datetime.now(tz='Europe/Moscow')
    if dt is None:
        raise ValueError("datetime.now(tz='Europe/Moscow') returned None")
    return dt.strftime("%H:%M:%S")


@register.simple_tag
def show_date():
    return datetime.now().strftime("%d.%m.%Y")
