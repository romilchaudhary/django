from django import template

register = template.Library()

@register.filter()
def custom_currency(value):
	return f"{value}rs"
