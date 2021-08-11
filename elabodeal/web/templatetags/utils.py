from django import template
from django.shortcuts import reverse
from django.templatetags.static import static
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag
def absolute_static(path):
	return mark_safe(f'http://localhost:8000{static(path)}')


@register.simple_tag
def absolute_url(view_name):
	return mark_safe(f'http://localhost:8000{reverse(view_name)}')