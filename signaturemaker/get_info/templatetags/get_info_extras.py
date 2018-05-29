from django import template
register = template.Library()

@register.inclusion_tag('user_template.html')
def user_vars(user_object):
    return user_object.vars