from django import template
from decimal import Decimal
import datetime

register = template.Library()

def valid_numeric(arg):
    if isinstance(arg, (int, float, Decimal)):
        return arg
    try:
        return int(arg)
    except ValueError:
        return float(arg)

@register.filter
def sub(value, arg):
    try:
        return valid_numeric(value) - valid_numeric(arg)
    except (ValueError, TypeError):
        try:
            return value - arg
        except Exception:
            return ''
sub.is_safe = False

def formatDate(arg):
    format = ('%d/%m/%Y')
    arg = arg.strftime(format)
    return arg

def formatDate1(arg):
    format = ('%Y')
    arg = arg.strftime(format)
    return arg

@register.filter
def suma(value, arg):
    try:
        return valid_numeric(value) + valid_numeric(arg)
    except (ValueError, TypeError):
        try:
            return value + arg
        except Exception:
            return ''
suma.is_safe = False

@register.filter
def cutstring(value, arg):
    string = value
    cut_string = string.split(arg)
    new_string = cut_string[0]
    return new_string

@register.filter
def dateF(value, arg):
	y = int(arg['y'])
	m = int(arg['m'])
	n = datetime.date(y, m, value)
	return n

@register.filter
def dateF1(value):
    return formatDate(value)

@register.filter
def dateF2(value):
    return formatDate1(value)

@register.filter
def total(value, arg):
    y = arg['y']
    m = arg['m']
    d = str(value.day)
    h = '15:00:00'
    s = y + '-' + m + '-' + d + ' ' + h
    s = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    r = value - s
    return r