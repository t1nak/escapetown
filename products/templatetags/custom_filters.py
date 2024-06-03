from django import template
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify

import markdown
register = template.Library()

from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

@register.filter
@stringfilter
def render_markdown(value):
    md = markdown.Markdown(extensions=["fenced_code"])
    return mark_safe(md.convert(value))