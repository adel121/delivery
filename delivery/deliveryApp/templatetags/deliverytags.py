from django import template
import datetime
import string
register = template.Library()

def to_date(value):
	return str(value.date())

def to_str(value):
	return str(value)

def get_year(value):
	string = str(value).strip()
	lst=string.split('-')
	print(lst)
	return int(lst[0])

def get_month(value):
	string = str(value).strip()
	lst=string.split('-')
	print(lst)
	return int(lst[1])

def get_day(value):
	string = str(value).strip()
	lst=string.split('-')
	print(lst)
	return int(lst[2])

register.filter('to_str',to_str)
register.filter('to_date',to_date)
register.filter('get_day', get_day)
register.filter('get_month',get_month)
register.filter('get_year',get_year)
