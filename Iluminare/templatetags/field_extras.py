from django import template
from django.forms import DateField

register = template.Library()

@register.filter(name='is_date_field')
def is_date_field(field):
    return field and hasattr(field, 'field') and isinstance(field.field, DateField)