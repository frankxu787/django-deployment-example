from django import template

register = template.Library()

@register.filter(name='trim')
def trim(value, arg):
    # This trims out all values of arg from the string!
    return value.replace(arg, '')

# register.filter('trim', trim)