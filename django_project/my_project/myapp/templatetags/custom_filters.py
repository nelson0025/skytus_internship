from django import template

register=template.Library()

@register.filter
def add_hello(value):
    return "hello " + value
