from django import template

register = template.Library()

@register.filter(name='word_excerpt')
def word_excerpt(value, arg):
    try:
        arg = int(arg)
        words = value.split()
        if len(words) <= arg:
            return value
        return ' '.join(words[:arg]) + '...'
    except:
        return value
