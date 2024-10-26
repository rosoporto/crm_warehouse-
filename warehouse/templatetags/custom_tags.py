from datetime import datetime
from django import template
import pytz


register = template.Library()


@register.simple_tag
def show_time():
    """Return the current time in the format H:M:S"""
    moscow_tz = pytz.timezone('Europe/Moscow')
    dt = datetime.now(moscow_tz)
    return dt.strftime("%H:%M:%S")


@register.simple_tag
def show_date():
    return datetime.now().strftime("%d.%m.%Y")
