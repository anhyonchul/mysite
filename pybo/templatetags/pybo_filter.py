from django import template
import markdown
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg

# 기존값 value에서 입력으로 반은값 arg를 빼서 반환한다.

@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))

