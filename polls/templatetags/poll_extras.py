from django import template
from jalali_date import date2jalali

register = template.Library()


@register.filter(name='get_persian_date')
def get_persian_date(value):
    return date2jalali(value).strftime('%Y/%m/%d')


@register.filter(name='price_separator')
def price_separator(price: int):
    return '{:,}'.format(price) + ' تومان'

# @register.simple_tag()
# def getFinalPrice(qty, price):
#     return qty * price
