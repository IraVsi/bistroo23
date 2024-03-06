from datetime import datetime, date
from django import template

register = template.Library()


@register.filter
def is_menu_old(menu_date):
    # menu_date on kujul d.m.Y
    date_object = datetime.strptime(menu_date,'%d.%m.%Y').date()
    today = date.today()  # tänane kuupäev
    return date_object < today  # True või False
